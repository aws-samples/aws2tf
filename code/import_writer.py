"""Import generation and references for aws2tf."""

import os
import re
import glob
import context
import logging
import inspect
from io import StringIO
from timed_interrupt import stop_timer
from file_ops import safe_write_file
from error_handler import handle_error2

log = logging.getLogger('aws2tf')


def ref_skipped(type, name):
   # True if a referenced resource was excluded (-e/--exclude) or skipped
   # (--skipname). In that case the target resource is never generated, so deref
   # handlers must keep the attribute as a literal id/ARN string rather than emit
   # a dangling Terraform reference to a resource that does not exist.
   if type in context.all_extypes:
       return True
   if context.skipname and name is not None and context.skipname.lower() in str(name).lower():
       return True
   return False


def is_self_ref(type, name):
   # True if a deref target is the resource currently being generated. Building a
   # reference to it would create an illegal self-reference (Terraform rejects a
   # block that refers to itself, e.g. a role whose trust policy lists its own ARN).
   return context.current_tf == type + "__" + name


def tfname(theid):
   # Sanitize an identifier the same way write_import generates a resource label,
   # so cross-resource references (e.g. aws_iam_user.<name>.id) match the declared
   # resource name. Names containing '.', '@', spaces etc. would otherwise produce
   # references Terraform parses as attribute access (aws_iam_user.first.last.id).
   tfid=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")
   tfid = re.sub(r'[^A-Za-z0-9_-]', '_', tfid)  # any remaining char invalid in a TF label -> _
   if tfid[:1].isdigit(): tfid="r-"+tfid
   tfid = re.sub(r'\.\.', '_', tfid)
   tfid = tfid.replace('/', '_')
   return tfid


#generally pass 3rd param as None - unless overriding
def write_import(type, theid, tfid):
   try:
      if not isinstance(theid, str):
         log.error("write_import: non-string id for type=%s (%s=%r) - skipping this resource", type, theid.__class__.__name__, theid)
         return
      ## todo -  if theid starts with a number or is an od (but what if its hexdecimal  ?)

      if tfid is None:
            tfid=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")
      else:
            tfid=tfid.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")

      tfid = re.sub(r'[^A-Za-z0-9_-]', '_', tfid)  # any remaining char invalid in a TF label -> _

         #catch tfid starts with number
      if tfid[:1].isdigit(): tfid="r-"+tfid

      # Security Fix #3: Additional sanitization to prevent path traversal
      tfid = re.sub(r'\.\.', '_', tfid)  # Remove any remaining ..
      tfid = tfid.replace('/', '_')  # Ensure no path separators

      if "!" in theid:
         fn="notimported/import__"+type+"__"+tfid+".tf"
         log.error("ERROR: Not importing "+type+" "+theid)
         log.error("ERROR: Invalid character ! in name")
      else:
         fn="import__"+type+"__"+tfid+".tf"

      #fn=fn.replace(context.acc,"012345678912")

      if context.debug: log.debug(fn)
         
         # check if file exists:
         #
      if context.merge:   
         #y = glob.glob("imported/import__*.tf")
         if os.path.isfile("imported/"+fn):
            return
         
      if os.path.isfile(fn):
            if context.debug: log.debug("File exists: " + fn)
            pkey=type+"."+tfid
            context.rproc[pkey]=True
            return

      done_data=False
      done_data=do_data(type,theid)

      if not done_data:
         output = StringIO()
         output.write('import {\n')
         output.write('  to = ' +type + '.' + tfid + '\n')
         output.write('  id = "'+ theid + '"\n')
         output.write('}\n')

                  # Write the filtered resource block to a new file
         
         if len(fn) > 255: fn=fn[:250]+".tf"
         #if context.merge:   print("Merge import",fn)
         try:
            # Security Fix #3: Use safe file write with path validation
            safe_write_file(fn, output.getvalue().strip() + '\n')
         except ValueError as e:
            log.error(f"ERROR: Path validation failed: {e}")
            log.info("exit 039")
            stop_timer()
            exit()
         except Exception as e:
            log.error(f"ERROR: could not write to file: {fn} - {e}")
            log.info("exit 039")
            stop_timer()
            exit()


      pkey=type+"."+tfid
      context.rproc[pkey]=True
      pkey=type+"."+theid
      context.rproc[pkey]=True


   except Exception as e:  
      handle_error2(e,str(inspect.currentframe().f_code.co_name),id)    

   return


def do_data(type, theid):
   if context.dnet:
      if type == "aws_vpc" or type=="aws_subnet":
         fn="data-"+type+"_"+theid+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "'+theid+'" {\n')
            f3.write(' id = "'+theid+'"\n')
            f3.write('}\n')
         return True
      
   if context.dsgs:
      if type=="aws_security_groups":
         fn="data-"+type+"_"+theid+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "'+theid+'" {\n')
            f3.write(' id = "'+theid+'"\n')
            f3.write('}\n')
         return True
   if context.dkms:
      if type == "aws_kms_key":
         fn="data-"+type+"_"+theid+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "k-'+theid+'" {\n')
            f3.write(' key_id = "'+theid+'"\n')
            f3.write('}\n')
         return True
   if context.dkey:
      if type == "aws_key_pair":
         tfil=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
         fn="data-"+type+"_"+tfil+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "'+tfil+'" {\n')
            f3.write(' key_name = "'+theid+'"\n')
            f3.write('}\n')
         return True


   return False
