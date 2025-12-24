import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_waf_web_acl(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            

            response = client.list_web_acls()
                
            if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                #print(str(response))
            for j in response[topkey]:
                    idd=j[key]
                    pkey=idd
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
 
        else: 

            client = boto3.client(clfn)
            response = client.get_web_acl(WebACLId=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['WebACL']
            pkey=j[key]
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True