"""Terraform CLI execution and progress tracking for aws2tf."""

import subprocess
import os
import json
import time
import glob
import shutil
import threading
import sys
import context
import manifest
import logging
from datetime import datetime
from tqdm import tqdm
from timed_interrupt import stop_timer
from cmd_runner import rc, splitf, fix_imports
from file_ops import safe_write_file, secure_terraform_files
import fixtf

log = logging.getLogger('aws2tf')


def run_terraform_plan_with_progress(command, description="Terraform plan", record_time=False):
    """
    Run terraform plan command and show estimated progress with adaptive learning.
    """
    # Count import files to estimate total
    import_files = glob.glob("import__*.tf")
    total_resources = len(import_files)
    
    if total_resources == 0 or context.debug:
        return rc(command)
    
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        estimated_rate = context.terraform_plan_rate
        estimated_time = total_resources / estimated_rate
        
        with tqdm(total=100, 
                 desc=description,
                 unit="%",
                 leave=False,
                 bar_format='{desc}: {percentage:3.0f}%|{bar}| [{elapsed}<{remaining}]') as pbar:
            
            start = time.time()
            
            while process.poll() is None:
                elapsed = time.time() - start
                if elapsed < estimated_time:
                    progress = int((elapsed / estimated_time) * 75)
                else:
                    overtime = elapsed - estimated_time
                    additional = 3 * (1 - (1 / (1 + overtime / 20)))
                    progress = 75 + int(additional)
                
                pbar.n = progress
                pbar.refresh()
                time.sleep(0.5)
            
            pbar.n = 100
            pbar.refresh()
            
            actual_time = time.time() - start
            actual_rate = total_resources / actual_time if actual_time > 0 else estimated_rate
            
            if context.terraform_plan_samples == 0:
                context.terraform_plan_rate = actual_rate
            else:
                context.terraform_plan_rate = (context.terraform_plan_rate * 0.7) + (actual_rate * 0.3)
            
            context.terraform_plan_samples += 1
            
            if record_time:
                context.last_plan_time = actual_time
            
            if context.debug:
                log.debug(f"Terraform plan rate updated: {context.terraform_plan_rate:.2f} resources/sec (sample #{context.terraform_plan_samples})")
                if record_time:
                    log.debug(f"Recorded plan time: {actual_time:.2f} seconds")
        
        stdout, stderr = process.communicate()
        
        class Result:
            def __init__(self, returncode, stdout, stderr):
                self.returncode = returncode
                self.stdout = stdout.encode()
                self.stderr = stderr.encode()
        
        return Result(process.returncode, stdout, stderr)
    
    except Exception as e:
        if context.debug:
            log.debug(f"Progress tracking failed, using regular execution: {e}")
        return rc(command)


def run_terraform_command_with_spinner(command, description="Running terraform"):
    """Run terraform command with a simple spinner (for commands without progress)."""
    return rc(command)


def get_import_count_from_plan(plan_file='plan2.json'):
    """Get number of resources to import from terraform plan JSON."""
    try:
        with open(plan_file) as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get('type') == 'change_summary':
                        return data['changes'].get('import', 0)
                except (json.JSONDecodeError, KeyError):
                    continue
    except FileNotFoundError:
        pass
    return 0


def run_terraform_apply_with_progress(tfplan_file, plan_json='plan2.json'):
    """Run terraform apply command and show estimated progress with adaptive learning."""
    total_resources = get_import_count_from_plan(plan_json)
    
    if total_resources == 0 or context.debug:
        command = f"terraform apply -no-color {tfplan_file}"
        return rc(command)
    
    try:
        command = f"terraform apply -no-color -json {tfplan_file}"
        
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        estimated_rate = context.terraform_apply_rate
        estimated_time = total_resources / estimated_rate
        
        stdout_lines = []
        stderr_lines = []
        imported_count = 0
        
        with tqdm(total=100,
                 desc="Importing resources",
                 unit="%",
                 leave=False,
                 bar_format='{desc}: {percentage:3.0f}%|{bar}| [{elapsed}<{remaining}]') as pbar:
            
            start = time.time()
            
            def update_progress():
                while process.poll() is None:
                    elapsed = time.time() - start
                    if elapsed < estimated_time:
                        progress = int((elapsed / estimated_time) * 75)
                    else:
                        overtime = elapsed - estimated_time
                        additional = 3 * (1 - (1 / (1 + overtime / 20)))
                        progress = 75 + int(additional)
                    pbar.n = progress
                    pbar.refresh()
                    time.sleep(0.5)
            
            progress_thread = threading.Thread(target=update_progress, daemon=True)
            progress_thread.start()
            
            for line in process.stdout:
                stdout_lines.append(line)
                try:
                    if line.strip():
                        data = json.loads(line)
                        event_type = data.get('type', '')
                        if event_type == 'apply_complete':
                            imported_count += 1
                except (json.JSONDecodeError, KeyError, AttributeError):
                    pass
            
            stderr_output = process.stderr.read()
            if stderr_output:
                stderr_lines.append(stderr_output)
            
            process.wait()
            progress_thread.join(timeout=1)
            
            pbar.n = 100
            pbar.refresh()
            
            actual_time = time.time() - start
            actual_count = imported_count if imported_count > 0 else total_resources
            actual_rate = actual_count / actual_time if actual_time > 0 else estimated_rate
            
            if context.terraform_apply_samples == 0:
                context.terraform_apply_rate = actual_rate
            else:
                context.terraform_apply_rate = (context.terraform_apply_rate * 0.7) + (actual_rate * 0.3)
            
            context.terraform_apply_samples += 1
            
            if context.debug:
                log.debug(f"Terraform apply rate updated: {context.terraform_apply_rate:.2f} resources/sec (sample #{context.terraform_apply_samples})")
        
        class Result:
            def __init__(self, returncode, stdout, stderr):
                self.returncode = returncode
                self.stdout = stdout.encode()
                self.stderr = stderr.encode()
        
        return Result(process.returncode, ''.join(stdout_lines), ''.join(stderr_lines))
    
    except Exception as e:
        if context.debug:
            log.debug(f"Apply progress tracking failed, using regular execution: {e}")
        command = f"terraform apply -no-color {tfplan_file}"
        return rc(command)


def move_to_notimported(pattern):
   """shutil.move does not expand wildcards - glob and move each match."""
   os.makedirs("notimported", exist_ok=True)
   for f in glob.glob(pattern):
      log.error("ERROR: moved "+f+" to notimported/")
      shutil.move(f, os.path.join("notimported", f))


def tfplan1(mymess):

   rf = "resources.out"

   if not glob.glob("import*.tf"):
      log.info("INFO: No import*.tf files found - nothing to import, exiting ....")
      log.info("INFO: Confirm the resource type exists in your account: "+context.acc+" & region: "+context.region)
      context.tracking_message="No import*.tf files found for this resource, exiting ...."
      stop_timer()
      sys.exit(0)

   com = "cp imported/provider.tf provider.tf"
   rout = rc(com)

   com = "mv aws_*.tf imported"
   rout = rc(com)

   com = "terraform plan -generate-config-out=" + \
       rf + " -out tfplan -json > plan1.json"
   if not context.fast: log.info(com)
   
   rout = run_terraform_plan_with_progress(com, "Terraform plan "+mymess)
      
   file = "plan1.json"
   f2 = open(file, "r")
   plan2 = True

   while True:
      line = f2.readline()
      if not line:
         break
      if '@level": "error"' in line:
         if context.debug is True:
            log.debug("Error" + line)
         try:
               mess = f2.readline()
               try:
                  if "VPC Lattice" in mess and "404" in mess:
                     log.error("ERROR: VPC Lattice 404 error - see plan1.json")
                     i = mess.split('(')[1].split(')')[0].split('/')[-1]
                     if i != "":
                        log.error("ERROR: Removing "+i +
                              " import files - plan errors see plan1.json [p1]")
                        context.badlist = context.badlist+[i]
                        move_to_notimported("import__*"+i+"*.tf")

                  elif "Error: Cannot import non-existent remote object" in mess:
                     log.error(
                         "ERROR: Cannot import non-existent remote object - see plan1.json")
                     i = mess.split('(')[1].split(')')[0].split('/')[-1]
                     if i != "":
                        log.error("ERROR: Removing "+i +
                              " import files - plan errors see plan1.json [p2]")
                        context.badlist = context.badlist+[i]
                        move_to_notimported("import__*"+i+"*.tf")

               except:
                  pass

               try:
                  i = mess.split('(')[2].split(')')[0]
                  if i != "":
                     log.error("ERROR: Removing "+i +
                           " files - plan errors see plan1.json [p3]")
                     context.badlist = context.badlist+[i]
                     move_to_notimported("import__*"+i+"*.tf")
                     move_to_notimported("aws_*"+i+"*.tf")

               except:
                  if context.debug is True:
                     log.debug(mess.strip())
                  context.plan2 = True

         except:
               log.error("Error - no error message, check plan1.json")
               dt = datetime.now().isoformat(timespec='seconds')
               com = "cp plan1.json plan1.json."+dt
               log.info(com)
               rout = rc(com)
               log.info("exit 018")
               stop_timer()
               exit()

   if not os.path.isfile("resources.out"):
         log.error("could not find expected resources.out file after Plan 1 - exiting")
         dt = datetime.now().isoformat(timespec='seconds')
         com = "cp plan1.json plan1.json."+dt
         log.info(com)
         rout = rc(com)

   return


def tfplan2():
   if not os.path.isfile("resources.out"):
         log.error("could not find expected resources.out file in tfplan2 - exiting")
         return

   splitf("resources.out")  # generated *.out files
   # zap the badlist
   for i in context.badlist:
      log.error("ERROR: Removing "+i+" files - plan errors see plan1.json [p4]")
      move_to_notimported("aws_*"+i+"*.tf")
      move_to_notimported("aws_*"+i+"*.out")

   # copy all imported/aws_*.tf to here ?
   com = "cp imported/aws_*.tf ."
   rout = rc(com)

   # Process .out files with fixtf (fix terraform files)
   x = glob.glob("aws_*__*.out")
   
   if len(x) > 0:
      for fil in tqdm(x, desc="Fixing terraform files", unit="file", leave=False):
         type = fil.split('__')[0]
         tf = fil.split('.')[0]
         fixtf.fixtf(type, tf)
   
   com = "mv aws_*.out imported"
   rout = rc(com)

   com = "terraform fmt"
   rout = rc(com)


def tfplan3():

   #### move tfproto files
   x=glob.glob("data*.tfproto")
   for fil in x:
      tf=fil.split('.tfproto',1)[0]
      com = "mv "+fil +" "+ tf+".tf"
      log.debug(com)
      rout = rc(com)

   context.tracking_message="Validate and Test Plan  ..."
   log.info("\nValidate and Test Plan  ... ")
   if context.merge:
      com = "cp imported/aws_*.tf ."
      rout = rc(com)
   if not glob.glob("aws_*.tf"):
      log.error("No aws_*.tf files found for this resource, exiting ....")
      log.info("exit 019")
      stop_timer()
      exit()

   rf = "resources.out"
   com = "cp imported/provider.tf provider.tf"
   rout = rc(com)

   com = "terraform validate -no-color"
   rout = rc(com)
   el = len(rout.stderr.decode().rstrip())
   if el != 0:
      errm = rout.stderr.decode().rstrip()
      log.error(errm)
      com = "terraform validate -no-color -json > validate2.json"
      rout = rc(com)

   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      log.error(str(rout.stdout.decode().rstrip()))
      log.error("Validation after fix failed - exiting")
      context.tracking_message="Validation after fix failed - exiting"
      log.info("exit 020 %s", str(context.aws2tfver))
      stop_timer()
      exit()

   else:
      log.info("Valid Configuration.")
      if context.validate:
         log.info("Validate Only..")
         return
   zeroi=0    

################################################################################
   x = glob.glob("aws_*__*.tf")
   context.esttime=len(x)/4
   awsf=len(x)
   y = glob.glob("import__*.tf")
   impf=len(y)

   if awsf != impf:
      if context.workaround=="":
         if not context.merge:
            log.error("ERROR: "+str(awsf)+ "x aws_*.tf and " + str(impf) +"x import__*.tf file counts do not match")      
            fix_imports()
      else:
         log.info("INFO: "+str(awsf)+ "x aws_*.tf and " + str(impf) +"x import__*.tf file counts do not match")
         log.info("INFO: Continuing due to workaround "+context.workaround)
   else:
      log.info("PASSED: aws_*.tf and import__*.tf file counts match = %s", awsf)

################################################################################

   context.plan2=True

   if context.plan2:

      log.info("Stage 7 of 10, Penultimate Terraform Plan ... ")
      context.tracking_message="Stage 7 of 10, Penultimate Terraform Plan ..."

      com="ls imported/import*"
      rout = rc(com)
      print(rout.stdout.decode().rstrip())

      com = "rm -f resources.out tfplan"
      rout = rc(com)
      
      com = "terraform plan -generate-config-out=" + \
          rf + " -out tfplan -json > plan2.json"
      if not context.fast: log.info(com)
      
      # Patterns that indicate transient network errors (worth retrying)
      _TRANSIENT_ERROR_PATTERNS = (
          "no such host",
          "dial tcp",
          "connection reset",
          "connection refused",
          "TLS handshake timeout",
          "request send failed",
          "i/o timeout",
      )
      
      def _run_plan2():
          return run_terraform_plan_with_progress(com, "Terraform plan (validation)", record_time=True)
      
      def _check_plan2_for_errors():
          """Check plan2.json for errors. Returns (has_fatal_error, has_transient_error)."""
          has_fatal = False
          has_transient = False
          with open('plan2.json', 'r') as f:
             for line in f.readlines():
                if '@level":"error"' in line:
                  if "Error: Conflicting configuration arguments" in line and "aws_security_group_rule." in line:
                     log.warning(
                         "WARNING: Conflicting configuration arguments in aws_security_group_rule")
                  elif "Operation not supported on Multi Dialect Views" in line:
                     log.warning(
                         "WARNING: Glue Multi Dialect View detected - skipping (Terraform provider limitation)")
                  else:
                      # Check if this is a transient network error
                      is_transient = any(p in line.lower() for p in _TRANSIENT_ERROR_PATTERNS)
                      if is_transient:
                          has_transient = True
                      else:
                          has_fatal = True
                      
                      try:
                          error_obj = json.loads(line)
                          error_message = error_obj.get('@message', 'Unknown error')
                          error_detail = error_obj.get('diagnostic', {}).get('detail', '')
                          
                          log.error("=" * 80)
                          log.error("TERRAFORM PLAN ERROR DETECTED:")
                          log.error("-" * 80)
                          log.error("Error Message: %s", error_message)
                          if error_detail:
                              log.error("Error Detail: %s", error_detail)
                          log.error("=" * 80)
                          
                          print("\n" + "=" * 80)
                          print("TERRAFORM PLAN ERROR DETECTED:")
                          print("-" * 80)
                          print(f"Error Message: {error_message}")
                          if error_detail:
                              print(f"Error Detail: {error_detail}")
                          print("=" * 80 + "\n")
                          
                      except json.JSONDecodeError:
                          if context.debug is True:
                             log.debug("Error parsing JSON: " + line)
                          log.error("Error line (raw): %s", line.strip())
                          print(f"\nError line (raw): {line.strip()}\n")
          
          return has_fatal, has_transient
      
      rout = _run_plan2()
      
      zerod = False
      zeroc = False
      zeroa = False
      zeroi = -1
      planList = []
      planDict = {}
      changeList = []
      with open('plan2.json') as f:
         for jsonObj in f:
            planDict = json.loads(jsonObj)
            planList.append(planDict)
      for pe in planList:
         if pe['type'] == "change_summary":  
            zeroi=pe['changes']['import']
            zeroa=pe['changes']['add']
            zeroc=pe['changes']['change']
            zerod=pe['changes']['remove']

      log.info("Plan: %s to import, %s to add, %s to change, %s to destroy", zeroi, zeroa, zeroc, zerod)

      has_fatal, has_transient = _check_plan2_for_errors()
      
      if has_transient and not has_fatal:
          # Transient network error — retry once after a short delay
          log.warning("Transient network error detected — retrying plan in 10 seconds...")
          time.sleep(10)
          
          com2 = "rm -f resources.out tfplan"
          rc(com2)
          
          rout = _run_plan2()
          
          # Re-parse plan2.json
          planList = []
          with open('plan2.json') as f:
             for jsonObj in f:
                planDict = json.loads(jsonObj)
                planList.append(planDict)
          for pe in planList:
             if pe['type'] == "change_summary":  
                zeroi=pe['changes']['import']
                zeroa=pe['changes']['add']
                zeroc=pe['changes']['change']
                zerod=pe['changes']['remove']
          
          log.info("Retry Plan: %s to import, %s to add, %s to change, %s to destroy", zeroi, zeroa, zeroc, zerod)
          
          has_fatal, has_transient = _check_plan2_for_errors()
          if has_fatal or has_transient:
              log.error("-->> Plan 2 errors persist after retry - check plan2.json - or run terraform plan")
              log.info("exit 021 %s", str(context.aws2tfver))
              stop_timer()
              exit()
          else:
              log.info("Retry succeeded - transient error resolved")
      
      elif has_fatal:
          log.error("-->> Plan 2 errors exiting - check plan2.json - or run terraform plan")
          log.info("exit 021 %s", str(context.aws2tfver))
          stop_timer()
          exit()

      if zerod != 0:
         log.error("-->> plan will destroy resources! - unexpected, is there existing state ?")
         log.error("-->> look at plan2.json - or run terraform plan")
         log.info("exit 022")
         stop_timer()
         sys.exit(1)

      if zeroc != 0:
         planList = []
         planDict = {}
         changeList = []
         allowedchange = False
         nchanges = 0
         nallowedchanges = 0
         all_force_destroy_only = True

         force_destroy_only_addrs = set()
         computed_only_addrs = set()
         try:
            _show = subprocess.run(['terraform', 'show', '-json', 'tfplan'],
                                   capture_output=True, text=True)
            _sp = json.loads(_show.stdout)
            for _rc in _sp.get('resource_changes', []):
               _ch = _rc.get('change', {})
               if _ch.get('actions') == ['update']:
                  _before = _ch.get('before', {}) or {}
                  _after = _ch.get('after', {}) or {}
                  if _before == _after:
                     computed_only_addrs.add(_rc['address'])
                  else:
                     diff_keys = [k for k in set(list(_before.keys()) + list(_after.keys())) 
                                 if _before.get(k) != _after.get(k)]
                     if diff_keys == ['force_destroy']:
                        force_destroy_only_addrs.add(_rc['address'])
         except Exception as _e:
            if context.debug:
               log.debug("force_destroy detection skipped: %s", _e)
         
         with open('plan2.json') as f:
            for jsonObj in f:
               planDict = json.loads(jsonObj)
               planList.append(planDict)
         for pe in planList:
            if pe['type'] == "planned_change" and pe['change']['action'] == "update":
               nchanges = nchanges+1
               ctype = pe['change']['resource']['resource_type']
               caddr = pe['change']['resource']['addr']
               
               force_destroy_only = caddr in force_destroy_only_addrs
               if not force_destroy_only:
                  all_force_destroy_only = False
               
               if ctype == "aws_lb_listener" or ctype == "aws_cognito_user_pool_client" \
                  or ctype=="aws_bedrockagent_agent" or ctype=="aws_bedrockagent_agent_action_group" \
                  or ctype=="aws_ssm_parameter" or ctype=="aws_s3tables_table_bucket" \
                  or ctype=="aws_s3vectors_vector_bucket" \
                  or caddr in computed_only_addrs \
                  or force_destroy_only:
                  
                  changeList.append(pe['change']['resource']['addr'])
                  log.info("Planned changes found in Terraform Plan for type: " +
                        str(pe['change']['resource']['resource_type'])+" "+str(pe['change']['resource']['addr']))
                  allowedchange = True
                  nallowedchanges = nallowedchanges+1
               else:
                  all_force_destroy_only = False
                  log.warning("Unexpected plan changes found in Terraform Plan for resource: " +
                        str(pe['change']['resource']['addr']))
         if nchanges == nallowedchanges:
            log.info("\n-->> plan will change " + str(nchanges) +
                  " resources! - these are expected changes only (should be non-consequential)")
            ci = 1

            log.info(
                "-->> Check the planned changes in these resources listed below by running: terraform plan\n")

            for i in changeList:
               log.info(str(ci)+": "+str(i))
               ci = ci+1
            log.info("\n")

            if all_force_destroy_only and nchanges > 0:
               log.info("All changes are force_destroy only - automatically continuing")
               context.expected = True

            if context.expected is False:
               log.info("You can check the changes by running 'terraform plan' in %s\n", context.path1)
               log.info("Then rerun the same ./aws2tf.py command and add the '-a' flag to accept these plan changes and continue to import")
               log.info("exit 023")
               stop_timer()
               exit()

            if context.debug is True:
               log.debug("\n-->> Then if happy with the output changes for the above resources, run this command to complete aws2tf-py tasks:")
               log.info("exit 024")
               stop_timer()
               log.info("terraform apply -no-color tfplan")
               exit()
         else:
            log.error("-->> plan will change resources! - unexpected")
            log.error("-->> look at plan2.json - or run terraform plan")
            log.info("exit 025 %s", str(context.aws2tfver))
            stop_timer()
            exit()

      if zeroa !=0:
         log.error("-->> plan will add resources! - unexpected")
         log.error("-->> look at plan2.json - or run terraform plan")
         log.info("exit 026")
         stop_timer()
         exit()

      log.debug("Plan complete")

   # Update manifest with Stage 7 plan results
   manifest.update_resource_counts(
      plan_to_import=zeroi if zeroi != -1 else 0,
      plan_to_add=zeroa if zeroa else 0,
      plan_to_change=zeroc if zeroc else 0,
      plan_to_destroy=zerod if zerod else 0,
      aws_tf_files=awsf,
      import_tf_files=impf,
   )

   if not context.merge:
      if zeroi == awsf:
         log.info("PASSED: import count = file counts = %s", str(zeroi))
         context.stage7_clean = True
         manifest.stage_complete(7, {"plan_summary": {"to_import": zeroi, "to_add": zeroa, "to_change": zeroc, "to_destroy": zerod}})
      elif zeroi == 0 and zeroa == 0 and zeroc == 0 and zerod == 0:
         # All resources already in state (e.g. --resume after successful import)
         log.info("PASSED: All resources already imported (0 changes in plan) — nothing to do")
         context.stage7_clean = True
         manifest.stage_complete(7, {"plan_summary": {"to_import": 0, "to_add": 0, "to_change": 0, "to_destroy": 0}, "note": "all_already_in_state"})
      else:
         log.info("INFO: import count "+str(zeroi) +" != file counts "+ str(awsf))
         if context.workaround=="":
            manifest.stage_failed(7, f"import count {zeroi} != file counts {awsf}")
            log.error("\nLikely import error [2] - do the following and report errors in github issue")
            log.info("cd "+context.path1)
            log.info("terraform plan -generate-config-out=resources.out")
            log.info("exit 027")
            stop_timer()
            exit()
         else:
            log.info("INFO: Continuing due to workaround "+context.workaround)
         
   if context.merge:
         log.info("Merge check")
         if zeroi==0:
            log.info("Nothing to merge exiting ...")
            log.info("exit 028")
            stop_timer()
            exit()
         x = glob.glob("imported/import__*.tf")
         preimpf=len(x)
         log.info("previous imports %s",str(preimpf))
         toimp=awsf-preimpf
         com = "terraform state list | grep ^aws_ | wc -l"
         rout = rc(com)
         stc=int(rout.stdout.decode().rstrip())

         if preimpf != stc:
            log.error("Miss-matched previous imports %s and state file resources %s exiting", str(preimpf), str(stc))
            log.info("exit 029")
            stop_timer()
            exit() 
         else:
            log.info("Existing import file = Existing state count = %s", str(stc))
         if toimp != zeroi:
            log.warning("Unexpected import number exiting")
         else:
            log.info("PASSED: importing expected number of resources = %s", str(toimp))    

   if not os.path.isfile("tfplan"):
      log.error("Plan - could not find expected tfplan file - exiting")
      log.info("exit 031")
      stop_timer()
      sys.exit(1)


def wrapup():
   log.info("Stage 8 of 10, Final Terraform Validation")
   manifest.stage_start(8, "Final Terraform Validation")
   context.tracking_message="Stage 8 of 10, Final Terraform Validation"
   com = "terraform validate -no-color"
   rout = rc(com)
   el = len(rout.stderr.decode().rstrip())
   if el != 0:
      errm = rout.stderr.decode().rstrip()
      log.error(errm)
   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      log.error(str(rout.stdout.decode().rstrip()))
      manifest.stage_failed(8, "Validation failed")
      log.info("exit 032")
      stop_timer()
      exit()
   else:
      log.info("PASSED: Valid Configuration.")
      manifest.stage_complete(8)

   if context.merge:
      log.info("Pre apply merge check")
      if not os.path.isfile("plan2.json"):
         log.error("ERROR: Could not find plan2.json, unexpected on merge - exiting ....")
         log.info("exit 033")
         stop_timer()
         exit()
      
   log.info("Stage 9 of 10, Terraform import via apply of tfplan....")
   manifest.stage_start(9, "Terraform import via apply")
   context.tracking_message="Stage 9 of 10, Terraform import via apply of tfplan...."
   
   rout = run_terraform_apply_with_progress("tfplan")
   
   zerod = False
   zeroc = False
   if "Error" in str(rout.stderr.decode().rstrip()):
      log.error("ERROR: problem in apply ... further checks ....")
      errs=str(rout.stderr.decode().rstrip())
      log.info("\nPost Error Import Plan Check .....")
      com = "terraform plan -no-color -out tfplan"
      rout = run_terraform_command_with_spinner(com, "Post-error validation")
      
      if "No changes. Your infrastructure matches the configuration" not in str(rout.stdout.decode().rstrip()):
         log.error(errs)
         log.error("ERROR: unexpected final plan stuff - exiting")

         if "aws_bedrockagent_agent" not in errs:
            log.info("exit 034")
            stop_timer()
            exit()
         else:
            log.warning("WARNING: aws_bedrockagent_agent - continuing")
      else:
         log.info("PASSED: No changes in plan")
         patterns = ["import__aws_*.tf", "*.out", "*.json"]
         files_to_move = [f for pattern in patterns for f in glob.glob(pattern)]
         if files_to_move:
            for tf in tqdm(files_to_move, desc="Moving files to imported/", unit="file", leave=False):
               try:
                     shutil.move(tf, f"imported/{tf}")
               except (FileNotFoundError, shutil.Error):
                     pass
         x = glob.glob("aws_*.tf")        
         if len(x) > 0:
            for tf in tqdm(x, desc=f"Moving files", unit="file", leave=False):
               try:
                  shutil.copy(tf, f"imported/{tf}")
               except (FileNotFoundError, shutil.Error):
                  pass
         
         secure_terraform_files('.')
         manifest.stage_complete(9, {"note": "apply_error_but_plan_clean"})
         manifest.stage_complete(10, {"note": "skipped_post_error_clean"})
         return

   log.info("\nStage 10 of 10, Post Import Plan Check .....")
   manifest.stage_complete(9)
   manifest.stage_start(10, "Post Import Plan Check")
   context.tracking_message="Stage 10 of 10, Post Import Plan Check ....."

   if hasattr(context, 'stage7_clean') and context.stage7_clean:
      log.info("Stage 10 of 10, Skipping post-import plan check - Stage 7 was clean")
      context.tracking_message="Stage 10 of 10, Skipped - Stage 7 was clean"
      
      patterns = ["import__aws_*.tf", "*.out", "*.json"]
      files_to_move = [f for pattern in patterns for f in glob.glob(pattern)]
      if files_to_move:
         for tf in tqdm(files_to_move, desc="Moving files to imported/", unit="file", leave=False):
            try:
                  shutil.move(tf, f"imported/{tf}")
            except (FileNotFoundError, shutil.Error):
                  pass
      x = glob.glob("aws_*.tf")        
      if len(x) > 0:
         for tf in tqdm(x, desc=f"Moving files", unit="file", leave=False):
            try:
               shutil.copy(tf, f"imported/{tf}")
            except (FileNotFoundError, shutil.Error):
               pass
      secure_terraform_files('.')
      manifest.stage_complete(10, {"note": "skipped_stage7_clean"})
      return

   com = "terraform plan -no-color -out tfplan -json > final.json"
   plan2_size = os.path.getsize('plan2.json') if os.path.exists('plan2.json') else 0
   
   if plan2_size > 0 and not context.debug:
       process = subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       with tqdm(total=100, desc="Post-import validation", unit="%", bar_format='{desc}: {percentage:3.0f}%|{bar}| [{elapsed}]') as pbar:
           start_time = time.time()
           max_wait = plan2_size / 50000
           while process.poll() is None:
               elapsed = time.time() - start_time
               if os.path.exists('final.json'):
                   current_size = os.path.getsize('final.json')
                   size_progress = min(75, int((current_size / plan2_size) * 75))
                   pbar.n = size_progress
               else:
                   time_progress = min(50, int((elapsed / max_wait) * 50))
                   pbar.n = time_progress
               pbar.refresh()
               time.sleep(0.5)
           pbar.n = 100
           pbar.refresh()
       stdout, stderr = process.communicate()
       class Result:
           def __init__(self, returncode, stdout, stderr):
               self.returncode = returncode
               self.stdout = stdout
               self.stderr = stderr
       rout = Result(process.returncode, stdout, stderr)
   else:
       rout = rc(com)

   com = "sync"
   rout = rc(com)
   zeroi=0
   zeroa=0
   zeroc=0
   zerod=0
   planList = []
   planDict = {}
   changeList = []
   with open('final.json','r') as f:
        for jsonObj in f:
            planDict = json.loads(jsonObj)
            planList.append(planDict)
   with open('final.warn', 'w') as f:
      for pe in planList:
         if pe['type'] == "change_summary":  
            zeroi=int(pe['changes']['import'])
            zeroa=int(pe['changes']['add'])
            zeroc=int(pe['changes']['change'])
            zerod=int(pe['changes']['remove'])
            json.dump(pe, f, indent=2, default=str)
         elif pe['type'] == "diagnostic":
            json.dump(pe, f, indent=2, default=str)


   log.info("Plan: %s to import, %s to add, %s to change, %s to destroy", zeroi, zeroa, zeroc, zerod)
   nchged=zeroi+zeroa+zeroc+zerod
   if nchged == 0:
      context.tracking_message="Stage 10 of 10, Passed post import check - No changes in plan"
      log.info("Stage 10 of 10, Passed post import check - No changes in plan")

      patterns = ["import__aws_*.tf", "*.out", "*.json"]
      files_to_move = [f for pattern in patterns for f in glob.glob(pattern)]
      if files_to_move:
         for tf in tqdm(files_to_move, desc="Moving files to imported/", unit="file", leave=False):
            try:
                  shutil.move(tf, f"imported/{tf}")
            except (FileNotFoundError, shutil.Error):
                  pass

      x = glob.glob("aws_*.tf")        
      if len(x) > 0:
         for tf in tqdm(x, desc=f"Moving files", unit="file", leave=False):
            try:
               shutil.copy(tf, f"imported/{tf}")
            except (FileNotFoundError, shutil.Error):
               pass
      
      secure_terraform_files('.')
      manifest.stage_complete(10, {"final_plan": {"import": zeroi, "add": zeroa, "change": zeroc, "destroy": zerod}})

   else:
      known_drift_types = {"aws_ssm_parameter", "aws_s3tables_table_bucket", 
                          "aws_s3vectors_vector_bucket", "aws_lb_listener",
                          "aws_cognito_user_pool_client", "aws_bedrockagent_agent",
                          "aws_bedrockagent_agent_action_group", "aws_s3tables_table"}
      all_known_drift = True
      for pe in planList:
         if pe['type'] == "planned_change" and pe['change']['action'] == "update":
            ctype = pe['change']['resource']['resource_type']
            if ctype not in known_drift_types:
               all_known_drift = False
               break
      
      if all_known_drift and zeroc > 0 and zeroa == 0 and zerod == 0:
         log.warning("WARNING: %s known-drift changes detected (non-consequential) - continuing", zeroc)
         context.tracking_message="Stage 10 of 10, Passed post import check - known drift only"
         log.info("Stage 10 of 10, Passed post import check - known drift only")
         
         patterns = ["import__aws_*.tf", "*.out", "*.json"]
         files_to_move = [f for pattern in patterns for f in glob.glob(pattern)]
         if files_to_move:
            for tf in tqdm(files_to_move, desc="Moving files to imported/", unit="file", leave=False):
               try:
                     shutil.move(tf, f"imported/{tf}")
               except (FileNotFoundError, shutil.Error):
                     pass
         x = glob.glob("aws_*.tf")        
         if len(x) > 0:
            for tf in tqdm(x, desc=f"Moving files", unit="file", leave=False):
               try:
                  shutil.copy(tf, f"imported/{tf}")
               except (FileNotFoundError, shutil.Error):
                  pass
         secure_terraform_files('.')
         manifest.stage_complete(10, {"final_plan": {"import": zeroi, "add": zeroa, "change": zeroc, "destroy": zerod}, "note": "known_drift_only"})
      else:
         log.error("ERROR: unexpected final plan failure")
         out1=str(rout.stdout.decode().rstrip())
         log.error(out1)
         log.error(str(rout.stderr.decode().rstrip()))
         manifest.stage_failed(10, "unexpected final plan failure")
         log.info("exit 035")
         stop_timer()
         exit()
