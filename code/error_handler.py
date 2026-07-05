"""Error handling utilities for aws2tf."""

import sys
import os
import context
import logging
from timed_interrupt import stop_timer

log = logging.getLogger('aws2tf')


def handle_error(e, frame, clfn, descfn, topkey, id):
   
   exc_type, exc_obj, exc_tb = sys.exc_info()
   exn=str(exc_type.__name__)
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   if exn == "EndpointConnectionError":
      log.debug("No endpoint in this region for "+descfn+" - returning")
      return
   elif exn in ("SSLError", "ConnectionError", "ConnectionClosedError", "ConnectTimeoutError", "ReadTimeoutError"):
      log.warning("Transient connection error ("+exn+") for "+descfn+" clfn="+clfn+" - skipping this resource type")
      return
   elif exn == "UnsupportedCommandException":
      log.warning(descfn+" not supported in this region for "+clfn+" - returning")
      return
   elif exn=="ClientError":
      if "does not exist" in str(e):
         log.warning(id+" does not exist " + fname + " " + str(exc_tb.tb_lineno) )
         return
      log.debug("Exception message :"+str(e))
      return
   elif exn=="ForbiddenException":
      log.debug("Call Forbidden exception for "+fname+" - returning")
      return
   elif exn == "ParamValidationError" or exn=="ValidationException" or exn=="InvalidRequestException" or exn =="InvalidParameterValueException" or exn=="InvalidParameterException":
      log.warning(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return
   elif exn == "BadRequestException" and clfn=="guardduty":
      log.warning(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return  
   
   elif exn=="AccessDeniedException":
      log.warning("AccessDeniedException exception for "+fname+" - returning")
      return


   elif "NotFoundException" in exn:
      if frame.startswith("get_"):
         log.debug("NOT FOUND: "+frame.split("get_")[1]+" "+str(id)+" check if it exists and what references it - returning")
         pkey=frame.split("get_")[1]+"."+str(id)
         if "aws_glue_catalog_database" in pkey:
            pkey=frame.split("get_")[1]+"."+context.acc+":"+id
         context.rproc[pkey]=True
      else:
         log.debug("NOT FOUND: "+frame+" "+id+" check if it exists - returning")
      return    

   elif exn=="ResourceNotFoundException" or exn=="EntityNotFoundException" or exn=="NoSuchEntityException" or exn=="NotFoundException" or exn=="LoadBalancerNotFoundException" or exn=="NamespaceNotFound" or exn=="NoSuchHostedZone":
      if frame.startswith("get_"):
         log.debug("NOT FOUND: "+frame.split("get_")[1]+" "+str(id)+" check if it exists and what references it - returning")
         pkey=frame.split("get_")[1]+"."+str(id)
         context.rproc[pkey]=True
      else:
         log.debug("RESOURCE NOT FOUND: "+frame+" "+str(id)+" check if it exists - returning")
      return    
   
   elif exn == "KeyError":
      if "kms" in str(exc_obj):
         log.warning("KeyError can not find key for " +fname+" id="+str(id)+" - returning")
         return
      
      if clfn=="sqs":
         log.warning("KeyError can not find queue url for " +fname+" id="+str(id)+" - returning")
         return
      
   elif exn == "InvalidDocument":
      if clfn=="ssm":
         log.warning("KeyError can not find ssm document for " +fname+" id="+str(id)+" - returning")
         return

   elif exn == "AWSOrganizationsNotInUseException" or exn =="OrganizationAccessDeniedException":
      log.warning("NO ORG: "+frame+" this account doesn't appear to be in an AWS Organisation (or you don't have org permissions) - returning")
      return

   elif "NoSuch" in exn and clfn=="cloudfront":
      log.warning(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return

   elif exn == "TooManyRequestsException" or exn == "ThrottlingException" or exn == "Throttling":
      log.warning("Throttled: "+frame+" clfn="+clfn+" id="+str(id)+" - returning")
      return

   elif exn == "ConnectionError" or exn == "ConnectionResetError":
      log.warning("ConnectionError: "+frame+" clfn="+clfn+" id="+str(id)+" - retrying after backoff")
      import time
      time.sleep(2)
      return
   
   elif "BadRequest" in exn:
      if "The requested feature is not enabled for this AWS account" in str(exc_obj):
            log.warning(descfn + " returned feature not enabled for this account - returning")
            return
      elif "Your account isn't authorized to call this operation" in str(exc_obj):
            log.warning(descfn + " returned Your account isn't authorized to call this operation - returning")
            return
      log.error(exn)
      log.error(str(exc_obj)+" for "+frame+" id="+str(id)+" - exit")
      log.info("exit 040")
      #stop_timer() # as it is multi-threaded
      exit()


   elif "InvalidAccessException" in exn:
      if "is not subscribed" in str(exc_obj):
         log.warning(descfn + " returned Not subscribed "+clfn+" - returning")
         return
      log.info("exit 041")
      stop_timer()
      exit()
      



   log.error("\nERROR: in "+frame+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
   try:   
      log.error(f"{e=} [e1]")
      log.error(f"{exn=} [e1]")
      log.error("%s %s", fname, exc_tb.tb_lineno)
   except:
      log.error("except err")
      pass
   with open('boto3-error.err', 'a') as f:
      f.write("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
      f.write(f"{e=} [e1] \n")
      f.write(f"{fname=} {exc_tb.tb_lineno=} [e1] \n")
      f.write("-----------------------------------------------------------------------------\n")
   log.error("stopping process ...")
   #threading.
   stop_timer()
   sys.exit(1)
   

def handle_error2(e, frame, id):
   log.error("\nERROR: in "+frame)
   log.error("id="+str(id))
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   exn=str(exc_type.__name__)
   if exn == "EndpointConnectionError":
      log.debug("No endpoint in this region - returning")
      return
   log.error(f"{e=} [e2] %s %s", fname, exc_tb.tb_lineno)
   with open('boto3-error.err', 'a') as f:
      f.write("id="+str(id)+"\n")
      f.write(f"{e=} [e2] ")
      f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
      f.write("-----------------------------------------------------------------------------\n")
   log.info("exit 042")
   stop_timer()
   sys.exit(1)
