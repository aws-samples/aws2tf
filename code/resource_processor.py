"""Resource discovery and boto3 dispatch for aws2tf."""

import boto3
import botocore
import sys
import os
import context
import logging
import inspect
import resources
from timed_interrupt import stop_timer
from module_registry import AWS_RESOURCE_MODULES
from import_writer import write_import
from error_handler import handle_error, handle_error2
from cmd_runner import log_warning

log = logging.getLogger('aws2tf')


# Import needed dicts from module_registry
from module_registry import aws_no_import, aws_not_implemented, needid_dict


def call_resource(type, id):
   if type in context.all_extypes:
      log.debug("Common Excluding: %s %s", type, id)
      if id is not None:
         context.rproc[type+"."+id] = True
      return
   
   if type in aws_no_import.noimport:
      log_warning("WARNING: Can not import type: " + type)
      if id is not None:
         with open('not-imported.log', 'a') as f2:
            f2.write(type + " : " + str(id) + "\n")
         context.rproc[type+"."+id] = True
      return

   if type in aws_not_implemented.notimplemented:
      log_warning("Not supported by aws2tf currently: " + type +
            " please submit github issue to request support")
      return

   elif type == "aws_null":
      with open('stack-null.err', 'a') as f3:
         f3.write("-->> called aws_null for: "+id+"\n")
      return

   log.debug("---->>>>> "+type+"   "+str(id))
   if id is not None:
      ti = type+"."+id
      try:
         if context.rproc[ti]:
            log.debug("Already processed " + ti)
            log.debug("Already processed " + ti)
            return
      except:
         pass
   else:
      if type in needid_dict.aws_needid:
         log_warning("WARNING: " + type + " can not have null id must pass parameter " +
               needid_dict.aws_needid[type]['param'])
         return

   rr = False
   sr = False
   clfn, descfn, topkey, key, filterid = resources.resource_data(type, id)
   if key == "NOIMPORT":
      log_warning("WARNING: Can not import type: " + type)
      return

   if clfn is None:
        log.error("ERROR: clfn is None with type="+type)
        log.info("exit 016")
        stop_timer()
        exit()

   try:
            if context.debug:
               log.debug("calling specific common.get_"+type+" with type="+type+" id="+str(id)+"   clfn=" +
                    clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)

            mclfn = clfn.replace("-", "_")
            
            module = AWS_RESOURCE_MODULES.get(clfn) or AWS_RESOURCE_MODULES.get(mclfn)
            
            if module is None:
                if context.debug:
                    log.debug(f"Module not found in registry for clfn={clfn}, will try generic handler")
                sr = False
            else:
                getfn = getattr(module, "get_"+type)
                sr = getfn(type, id, clfn, descfn, topkey, key, filterid)

   except AttributeError as e:
      if context.debug:
         log.debug("AttributeError: name 'getfn' - no aws_"+clfn+".py file ?")
         log.debug(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.debug("%s %s %s %s",  exc_type, fname, exc_tb.tb_lineno)
      pass

   except SyntaxError:
      log.debug("SyntaxError: name 'getfn' - no aws_"+clfn+".py file ?")
      pass

   except NameError as e:
      if context.debug:
         log.debug("WARNING: NameError: name 'getfn' - no aws_"+clfn+".py file ?")
         log.debug(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.debug("%s %s %s %s",  exc_type, fname, exc_tb.tb_lineno)
      pass

   except Exception as e:
      handle_error(e, str(inspect.currentframe().f_code.co_name),
                   clfn, descfn, topkey, id)

   if not sr:
      try:
         if context.debug:
               log.debug("calling generic getresource with type="+type+" id="+str(id)+"   clfn="+clfn +
               " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
         rr = getresource(type, id, clfn, descfn, topkey, key, filterid)
      except Exception as e:
         log.error(f"{e=}")

         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.error("%s %s %s %s",  exc_type, fname, exc_tb.tb_lineno)
         if rr is False:
            log.error("--->> Could not get resource "+type+" id="+str(id))
            pass


   with open('processed-resources.log', 'a') as f4:
      f4.write(str(type) + " : " + str(id)+"\n")


def get_test(type, id, clfn, descfn, topkey, key, filterid):
   log.debug("in get_test")
   log.debug("--> In get_test doing "+ type + ' with id ' + str(id))   
   return


def getresource(type, id, clfn, descfn, topkey, key, filterid):
   if context.debug: log.debug("-1-> In getresource doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   if type in str(context.types): 
      log.info("Found "+type+"in types skipping ...")
      return True
   try:
      if id is not None:
         pt=type+"."+id
         if pt in context.rproc:
            if context.rproc[pt] is True:
               log.info("Found "+pt+" in processed skipping ...") 
               return True
      response=call_boto3(type,clfn,descfn,topkey,key,id)   
      if str(response) != "[]":
            for item in response:
               if id is None or filterid=="":
                  if context.debug: log.debug("--"+str(item))
                  try:
                     if "aws-service-role" in str(item["Path"]): 
                        if context.debug:  log.debug("Skipping service role " + str(item[key])) 
                        continue
                  except:
                     pass

                  try:
                     theid=item[key]
                  except TypeError:
                     log.error("ERROR: getresource TypeError: "+str(response)+" key="+key+" type="+type,descfn)
                     with open('boto3-error.err', 'a') as f:
                        f.write("ERROR: getresource TypeError: type="+type+" key="+key+" descfn="+descfn+"\n"+str(response)+"\n")
                     continue
                  pt=type+"."+theid
                  if pt not in context.rproc:
                     write_import(type,theid,None)
                  else:
                     if context.rproc[pt] is True:
                        log.info("Found "+pt+" in processed skipping ...") 
                        continue
               else:  
                  if context.debug: 
                     log.debug("-gr31-"+"filterid="+str(filterid)+" id="+str(id)+"  key="+key)
                     log.debug(str(item))
                  if "." not in filterid:
                     try:
                        if id == str(item[filterid]):
                           theid=item[key]
                           write_import(type,theid,None)
                        elif filterid != key:
                           if context.debug:
                              log.debug("id="+id+" filterid="+filterid)
                              log.debug("item="+str(item))
                           theid=item[filterid]
                           write_import(type,theid,None)
                     except Exception as e:
                        log.error(f"{e=}")
                        if context.mopup.get(type) is not None:
                           if id.startswith(context.mopup[type]):
                              write_import(type,id,None)
                              return True

                        else:
                           with open('missed-getresource.log', 'a') as f4:
                              f4.write("Could have done write_import "+type+" id="+id+" filterid="+filterid+"/n")
                           return False
                  else:
                     log.debug(str(item))
                     log.debug("id="+id+" filterid="+filterid)
                     filt1=filterid.split('.')[1]
                     filt2=filterid.split('.')[3]
                     log.debug("filt1="+filt1+" filt2="+filt2)
                     dotc=len(item[filt1])
                     log.debug("dotc="+str(dotc))

                     for j in range(0,dotc):
                        try:
                           val=str(item[filt1][j][filt2])
                           log.debug("val="+val + " id=" + id)
                           if id == val:
                              theid=item[key]
                              if dotc>1: theid=id+"/"+item[key]
                              write_import(type,theid,None)
                        except:
                           log.error("-------- error on processing")
                           log.error(str(item))
                           log.error("filterid="+filterid)
                           log.error("----------------------------")
                           pass
      else:
         if id is not None:
            if context.debug: log.debug("No "+type+" "+id+" found - empty response (common)") 
            pkey=type+"."+id  
            context.rproc[pkey]=True      
         else:
            if context.debug: log.debug("No "+type+" found - empty response (common)")
            return True
   
   except Exception as e:
      handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True               


def call_boto3(type, clfn, descfn, topkey, key, id): 
   try:
      if context.debug: 
         log.debug("call_boto3 clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
      response=[]
      if response == []:
         client = boto3.client(clfn) 
         try:
            paginator = client.get_paginator(descfn)
    
            if "apigatewayv2" in str(type):
               for page in paginator.paginate(ApiId=id): 
                  response.extend(page[topkey]) 
               pkey=type+"."+id
               context.rproc[pkey]=True

            elif descfn == "describe_launch_templates":
               if id is not None:
                  if id.startswith("lt-"):
                     for page in paginator.paginate(LaunchTemplateIds=[id]): response.extend(page[topkey])
                  else:
                     for page in paginator.paginate(LaunchTemplateNames=[id]): response.extend(page[topkey])
               else:
                  for page in paginator.paginate(): response.extend(page[topkey])

            elif descfn == "describe_instances":
               if id is not None:
                  if "i-" in id:
                     for page in paginator.paginate(InstanceIds=[id]): response.extend(page[topkey][0]['Instances'])
               else:
                  for page in paginator.paginate(): 
                     if len(page[topkey])==0:
                        continue
                     response.extend(page[topkey][0]['Instances'])

            elif descfn == "describe_pod_identity_association" or descfn == "list_fargate_profiles" or descfn == "list_nodegroups" or descfn == "list_identity_provider_configs" or descfn == "list_addons":
               for page in paginator.paginate(clusterName=id): response.extend(page[topkey])
            
            elif descfn == "list_access_keys" and id is not None:
               for page in paginator.paginate(UserName=id): response.extend(page[topkey])
            
            elif clfn=="kms" and descfn=="list_aliases" and id is not None:
               if id.startswith("k-"): id=id[2:]
               for page in paginator.paginate(KeyId=id): response.extend(page[topkey])
               return response
            
            elif clfn=="lambda" and descfn=="list_aliases" and id is not None:
               for page in paginator.paginate(FunctionName=id): response.extend(page[topkey])
               return response
                
            elif clfn=="describe_config_rules" and id is not None:
               for page in paginator.paginate(ConfigRuleNames=id): response.extend(page[topkey])
               return response
            
            elif clfn=="describe_log_groups" and id is not None:
               if "arn:" in id:  
                  for page in paginator.paginate(): response.extend(page[topkey])
                  return response
               else:
                  for page in paginator.paginate(logGroupNamePattern=id): response.extend(page[topkey])
                  return response            
            
            else:
               if context.debug: log.debug("--1b")
               for page in paginator.paginate(): 
                  response.extend(page[topkey])

               if id is not None:
                  fresp=response
                  if context.debug:log.debug("--2")
                  response=[]
                  if context.debug: log.debug(str(fresp))
                  for i in fresp:
                     if context.debug: 
                        try:
                           log.debug("%s %s %s",  i[key], id)
                        except TypeError:
                           log.debug("%s %s %s",  i, id)
                     try:
                        if id in i[key]:
                           response=[i]
                           break
                     except TypeError:
                        if id in i:
                           response=[i]
                           break

         except botocore.exceptions.ParamValidationError as e:
            log.error("ParamValidationError 1 in common.call_boto3: type="+type+" clfn="+clfn)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.error(f"{e=} [pv1] %s %s", fname, exc_tb.tb_lineno)
            with open('boto3-error.err', 'a') as f:
                     f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
                     f.write(f"{e=} [pv1] \n")
                     f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
                     f.write("-----------------------------------------------------------------------------\n")
            return []

         except botocore.exceptions.OperationNotPageableError as err:
               if context.debug:
                  log.debug(f"{err=}")
                  log.debug("calling non paginated fn "+str(descfn)+" id="+str(id))
               try:
                  getfn = getattr(client, descfn)                     
                  response1 = getfn()
                  response1=response1[topkey]
                  if context.debug: log.debug("Non-pag response1="+str(response1))
                  if id is None:
                     if context.debug: log.debug("id None")
                     response=response1
                     if context.debug: log.debug("Non-pag response no ID ="+str(response))
                  else:
                     for j in response1:
                        if id==j[key]:
                           response=[j]
                           if context.debug: log.debug("Non-pag response with ID ="+str(response))

               except botocore.exceptions.ParamValidationError as e:
                  log.error("ParamValidationError 2 in common.call_boto3: type="+type+" clfn="+clfn)
                  exc_type, exc_obj, exc_tb = sys.exc_info()
                  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                  log.error(f"{e=} [pv2] %s %s", fname, exc_tb.tb_lineno)    
                  with open('boto3-error.err', 'a') as f:
                     f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
                     f.write(f"{e=} [pv2] \n")
                     f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
                     f.write("-----------------------------------------------------------------------------\n")
                  return []

         except Exception as e:
            handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

         rl=len(response)
         if rl==0:
            if context.debug: log.debug("** zero response length for "+ descfn + " in call_boto3 returning .. []")
            return []

         if context.debug:
            log.debug("response length="+str(len(response)))
            for item in response:
               log.debug(item)
            log.debug("--------------------------------------")
   
      else:
         return response
      
   except Exception as e:
      handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return response
