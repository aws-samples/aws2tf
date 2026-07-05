"""Shell command execution and utilities for aws2tf."""

import subprocess
import os
import re
import shlex
import shutil
import sys
import glob
import context
import logging
import boto3
from io import StringIO
from tqdm import tqdm
from timed_interrupt import stop_timer
from file_ops import safe_write_file

log = logging.getLogger('aws2tf')


# Conditional warning function
def log_warning(message, *args, **kwargs):
    """
    Log warning only if warnings are enabled via -w flag.
    Always logs in debug mode.
    """
    if context.warnings or context.debug:
        log.warning(message, *args, **kwargs)


def rc(cmd):
    """
    Execute a command safely without shell=True.
    
    Args:
        cmd: Either a string (for backwards compatibility, will be parsed) 
             or a list of command arguments
    
    Returns:
        subprocess.CompletedProcess object
    """
    # If cmd is a string, parse it into a list for safe execution
    if isinstance(cmd, str):
        # For simple commands, split on spaces
        # For complex commands with pipes/redirects, we need special handling
        if '>' in cmd or '|' in cmd or '&&' in cmd or ';' in cmd:
            # These require shell, but we'll use shell=True only for these cases
            # and log a warning
            if context.debug:
                log.debug(f"WARNING: Command requires shell features: {cmd[:100]}")
            out = subprocess.run(cmd, shell=True, capture_output=True)
        else:
            # Safe to split and run without shell
            try:
                cmd_list = shlex.split(cmd)
                out = subprocess.run(cmd_list, capture_output=True, shell=False)
            except Exception as e:
                # Fallback to shell if parsing fails
                log.warning(f"Command parsing failed, using shell: {e}")
                out = subprocess.run(cmd, shell=True, capture_output=True)
    else:
        # cmd is already a list
        out = subprocess.run(cmd, capture_output=True, shell=False)
    
    ol = len(out.stdout.decode('utf-8').rstrip())
    el = len(out.stderr.decode().rstrip())
    if el != 0:
         errm = out.stderr.decode().rstrip()
         # log.error(errm)
         # exit(1)

    return out


def fix_imports():
   x = glob.glob("aws_*__*.tf")
   context.esttime=len(x)/4
   awsf=len(x)
   y = glob.glob("import__*.tf")
   impf=len(y)
   log.info("\nFix Import Intervention")



   #more import files than aws files - picked up via dependancies
   #if impf > awsf:
   for fil2 in y:  # all import files  
         impok=False
         for fil in x: # all aws_ files
            
            tf=fil.split('.tf',1)[0]
            iseg=fil2.replace("import__","").replace(".tf", "")
            if tf == iseg:
                  #com = "mv "+fil2+" imported/"+fil2
                  #rc(com)
                  impok=True
                  break
         
         ## out of for loop
         # got an import file we 
         if impok is False:
            com = "mv "+fil2+" "+fil2.replace(".tf",".err")
            log.warning(fil2.replace(".tf",".err"))
            rc(com)

   y = glob.glob("import__*.tf")
   impf=len(y)  


def ctrl_c_handler(signum, frame):
  log.info("Ctrl-C pressed.")
  log.info("exit 036")
  stop_timer()
  exit()


def check_python_version():
   version = sys.version_info
   major = version.major
   minor = version.minor
   bv = str(boto3.__version__)
   log.info("boto3 version: %s", bv)
   if major < 3 or (major == 3 and minor < 8):
      log.error("This program requires Python 3.8 or later.")
      sys.exit(1)
# check boto3 version
   if boto3.__version__ < '1.42.16':
      bv = str(boto3.__version__)
      log.info("boto3 version: %s", bv)
      vs = bv.split(".")
      v1 = int(vs[0])*100000+int(vs[1])*1000+int(vs[2])
      if v1 < 142016:
         log.error("boto3 version: %s", bv)
         log.error("This program requires boto3 1.42.16 or later.")
         log.error("Try: pip install boto3  -or-  pip install boto3==1.42.16")
         log.info("exit 037")
         stop_timer()
         sys.exit(1)


def aws_tf(region, args):
   # os.chdir(context.path1)
   #if not os.path.isfile("aws.tf"):

   with open("provider.tf", 'w') as f3:
      f3.write('terraform {\n')
      f3.write('  required_version = "> 1.10.4"\n')
      f3.write('  required_providers {\n')
      f3.write('    aws = {\n')
      f3.write('      source  = "hashicorp/aws"\n')
      # f3.write('      version = "5.48.0"\n')
      f3.write('      version = "'+context.tfver+'"\n')
      f3.write('    }\n')
      f3.write('  }\n')
      f3.write('}\n')
      f3.write('provider "aws" {\n')
      f3.write('  region                   = "' + region + '"\n')
      if args.profile is not None:
         f3.write('  profile                  = "' + context.profile + '"\n')
      if not context.serverless: f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
      f3.write('}\n')

   com = "cp provider.tf imported/provider.tf"
   rout = rc(com)
   if not os.path.isfile("data-aws.tf"):   
      with open("data-aws.tf", 'w') as f3:
         f3.write('data "aws_region" "current" {}\n')
         f3.write('data "aws_caller_identity" "current" {}\n')
         f3.write('data "aws_availability_zones" "az" {\n')
         f3.write('state = "available"\n')
         f3.write('}\n')
   if not context.merge:
      #log.info("terraform init")
      com = "terraform init -no-color -upgrade"
      rout = rc(com)
      el = len(rout.stderr.decode().rstrip())
      if el != 0:
         log.error(rout.stdout.decode().rstrip())
         log.error(str(rout.stderr.decode().rstrip()))
   else:
      log.info("skipping terraform init")


# split resources.out
def splitf_old(file):
   lhs = 0
   rhs = 0
   if os.path.isfile(file):
      if context.debug: log.debug("split file:" + file)
      with open(file, "r") as f:
         Lines = f.readlines()
      for tt1 in Lines:
         if "{" in tt1: lhs = lhs+1
         if "}" in tt1: rhs = rhs+1
         if lhs > 1:
               if lhs == rhs:
                  try:
                     f2.write(tt1+"\n")
                     f2.close()
                     lhs = 0
                     rhs = 0
                     continue
                  except:
                     pass

         if tt1.startswith("resource"):
               ttft = tt1.split('"')[1]
               taddr = tt1.split('"')[3]
               # if context.acc in taddr:
               #   a1=taddr.find(context.acc)
               #   taddr=taddr[:a1]+taddr[a1+12:]


               f2 = open(ttft+"__"+taddr+".out", "w")
               f2.write(tt1)

         elif tt1.startswith("#"):
               continue
         elif tt1 == "" or tt1 == "\n":
               continue
         else:
               try:
                  f2.write(tt1)
               except:
                  log.warning("tried to write to closed file: >" + tt1 + "<")
   else:
      log.error("could not find expected resources.out file")

   # moves resources.out to imported
   f2.close()
   shutil.move(file, "imported/"+file)


#################################

def splitf(input_file):
   # Compile regex patterns for better performance
   resource_pattern = re.compile(r'resource "(\w+)" "(.+?)"')
   comment_pattern = re.compile(r'^\s*#')
   if context.debug: log.debug("split file: " + input_file)
   # Read the entire file content at once
   with open(input_file, 'r') as f:
        content = f.read()
   
   # generate-config-out can emit a provider-invalid stickiness { duration = 0 }
   # (valid range is 1-604800); sanitize 0 -> 1 before splitting so the
   # per-resource .out validates.
   content = re.sub(r'(\n[ \t]*)duration = 0(?=\n)', r'\g<1>duration = 1', content)

    # Use a more efficient splitting method
   resource_blocks = re.split(r'(?=\nresource ")', '\n' + content)

   for block in resource_blocks[1:]:  # Skip the first (empty) block
        match = resource_pattern.search(block)
        if match:
            resource_type = match.group(1)
            resource_name = match.group(2)

            # Create filename
            resource_name_safe = resource_name.replace('/', '__')
            # Security Fix #3: Sanitize filename
            resource_name_safe = re.sub(r'[^\w\-\.]', '_', resource_name_safe)
            filename = f"{resource_type}__{resource_name_safe}.out"

            # Use StringIO for efficient string operations
            output = StringIO()

            for line in block.split('\n'):
                if not comment_pattern.match(line):
                    output.write(line + '\n')

            # Write the filtered resource block to a new file
            
            if len(filename) > 255: filename=filename[:250]+".out"
            try:
               # Security Fix #3: Use safe file write
               safe_write_file(filename, output.getvalue().strip() + '\n')
            except ValueError as e:
               log.error(f"ERROR: Path validation failed: {e}")
               log.info("exit 038")
               stop_timer()
               exit()
            except Exception as e:
               log.error(f"ERROR: could not write to file: {filename} - {e}")
               log.info("exit 038")
               stop_timer()
               exit()
   shutil.move(input_file,"imported/"+input_file)
