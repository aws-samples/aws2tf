import common
import boto3
import globals
import inspect

def get_aws_wafv2_ip_set(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            sc="CLOUDFRONT"
            if globals.region == "us-east-1":
                response = client.list_ip_sets(Scope=sc)
                if response == []: 
                    if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                for j in response[topkey]:
                    idd=j["Id"]
                    nm=j["Name"]
                    sc="CLOUDFRONT"
                    pkey=idd+"/"+nm+"/"+sc
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
            else:
                print("WARNING:Can only import CLOUDFRONT ip sets from us-east-1 region")
 
            sc="REGIONAL"
            response = client.list_ip_sets(Scope=sc)
            #print(str(response))
            if response[topkey] == []:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            
            #print(str(response))
            for j in response[topkey]:
                idd=j["Id"]
                nm=j["Name"]
                pkey=idd+"/"+nm+"/"+sc
                common.write_import(type, pkey, "w-"+pkey.replace("/", "_"))


        else: 
            if "|" in id:
                nm=id.split("|")[0]
                idd=id.split("|")[1]
                sc=id.split("|")[2]  
            else:
                print("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            response = client.get_ip_set(Scope=sc,Name=nm,Id=idd)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['IPSet']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_wafv2_web_acl(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            sc="CLOUDFRONT"
            if globals.region == "us-east-1":
                #client = boto3.client(clfn, region_name=globals.region)

            #my_session = boto3.setup_default_session(region_name='us-east-1',profile_name=globals.profile)
                response = client.list_web_acls(Scope=sc)
                #my_session = boto3.setup_default_session(region_name=globals.region,profile_name=globals.profile)
                if response == []: 
                    if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                #print(str(response))
                for j in response[topkey]:
                    idd=j["Id"]
                    nm=j["Name"]
                    sc="CLOUDFRONT"
                    pkey=idd+"/"+nm+"/"+sc
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
            else:
                print("WARNING:Can only import CLOUDFRONT web ACL's from us-east-1 region")
 
            sc="REGIONAL"
            response = client.list_web_acls(Scope=sc)
            if response[topkey] == []:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            
            #print(str(response))
            for j in response[topkey]:
                idd=j["Id"]
                nm=j["Name"]
                pkey=idd+"/"+nm+"/"+sc
                common.write_import(type, pkey, "w-"+pkey.replace("/", "_"))

        else: 
            if "|" in id:
                nm=id.split("|")[0]
                idd=id.split("|")[1]
                sc=id.split("|")[2]  
            else:
                print("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            client = boto3.client(clfn)
            response = client.get_web_acl(Scope=sc,Name=nm,Id=idd)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['WebACL']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_wafv2_rule_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            sc="CLOUDFRONT"
            if globals.region == "us-east-1":
                response = client.list_rule_groups(Scope=sc)
                if response == []: 
                    if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                for j in response[topkey]:
                    idd=j["Id"]
                    nm=j["Name"]
                    sc="CLOUDFRONT"
                    pkey=idd+"/"+nm+"/"+sc
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
            else:
                print("WARNING:Can only import CLOUDFRONT web ACL's from us-east-1 region")
 
            sc="REGIONAL"
            response = client.list_rule_groups(Scope=sc)
            if response[topkey] == []:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            
            #print(str(response))
            for j in response[topkey]:
                idd=j["Id"]
                nm=j["Name"]
                pkey=idd+"/"+nm+"/"+sc
                common.write_import(type, pkey, "w-"+pkey.replace("/", "_"))

        else: 
            if "|" in id:
                nm=id.split("|")[0]
                idd=id.split("|")[1]
                sc=id.split("|")[2]  
            else:
                print("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            client = boto3.client(clfn)
            response = client.get_rule_group(Scope=sc,Name=nm,Id=idd)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['RuleGroup']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

