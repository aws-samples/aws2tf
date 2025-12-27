import common
import logging
log = logging.getLogger('aws2tf')
from common import log_warning
import botocore
from botocore.config import Config
import context
import inspect


def get_aws_vpclattice_service_network(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        if id is None:
            client = common.boto3.client(clfn)
            response = []
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response.extend(page[topkey])
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                return True

            for j in response:
               retid = j['id']
               sarn = j['arn']
               common.write_import(type, retid, None)
               common.add_dependancy("aws_vpclattice_resource_policy", sarn)
               common.add_dependancy("aws_vpclattice_service_network_vpc_association", retid)
               common.add_dependancy("aws_vpclattice_service_network_service_association", retid)
        else:
            response = client.get_service_network(serviceNetworkIdentifier=id)
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response
            common.write_import(type, j[key], None)
            common.add_dependancy("aws_vpclattice_resource_policy", sarn)
            common.add_dependancy("aws_vpclattice_service_network_vpc_association", j[key])
            common.add_dependancy("aws_vpclattice_service_network_service_association", j[key])

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_vpclattice_service(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        if id is None:
            client = common.boto3.client(clfn)
            response = []
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response.extend(page[topkey])
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                return True

            for j in response:
                retid = j['id']
                sarn = j['arn']
                common.write_import(type, retid, None)
                common.add_dependancy("aws_vpclattice_listener", retid)
                common.add_dependancy("aws_vpclattice_resource_policy", sarn)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_vpclattice_service_network_vpc_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_vpclattice_service_network_vpc_association doing " + type + ' with id ' +
              str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    get_aws_vpc_lattice(type, id, clfn, descfn, topkey, key, filterid)
    return True


def get_aws_vpclattice_service_network_service_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_vpclattice_service_network_service_association doing " + type + ' with id ' +
              str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    get_aws_vpc_lattice(type, id, clfn, descfn, topkey, key, filterid)
    return True

def get_aws_vpclattice_service_network_resource_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_vpclattice_service_network_service_association doing " + type + ' with id ' +
              str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    get_aws_vpc_lattice(type, id, clfn, descfn, topkey, key, filterid)
    return True


def get_aws_vpclattice_access_log_subscription(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_vpclattice_service_network_vpc_association doing " + type + ' with id ' +
              str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    get_aws_vpc_lattice(type, id, clfn, descfn, topkey, key, filterid)
    return True


def get_aws_vpclattice_auth_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_vpclattice_auth_policy doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    client = common.boto3.client(clfn)
    if context.debug:
        log.debug("--client")
    response = []

    if context.debug:
        log.debug("Paginator")

    try:
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response.extend(page[topkey])
    except botocore.exceptions.OperationNotPageableError as err:
        # print(f"{err=}")
        getfn = getattr(client, descfn)
        response = getfn(resourceIdentifier=id)  # special
        # response=response1[topkey]
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    if response == []:
        if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
        return True

    else:
        log.info("**********************VPC Lattice auth policy"+str(response))
    for j in response:
        # retid=j['id']
        # theid=retid
        # turn id into an arn ?
        thearn = "arn:aws:vpclattice:"+context.region+":"+context.acc+":auth-policy/"+id
        # can use the arn - wants to import with id

        common.write_import(type, id, None)
        # common.add_dependancy("aws_vpclattice_listener_rule",theid)
        # context.rproc["aws_vpclattice_listener."+id]=True

    return True


def get_aws_vpclattice_target_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    client = common.boto3.client(clfn)
    response = []

    if id is None:
        try:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response.extend(page[topkey])
        except Exception as e:
            common.handle_error(
                e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
        if response == []:
            if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
            return True
        for j in response:
            theid = j[key]
            common.write_import(type, theid, None)
            #common.add_dependancy("aws_vpclattice_target_group_attachment",theid)
            context.rproc["aws_vpclattice_target_group."+theid] = True

    else:
        if id.startswith("tg-"):
            try:
                response1 = client.get_target_group(targetGroupIdentifier=id)
            except Exception as e:
                common.handle_error(
                    e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

            common.write_import(type, id, None)
            #common.add_dependancy("aws_vpclattice_target_group_attachment",id)
            context.rproc["aws_vpclattice_target_group."+id] = True

    return True


def get_aws_vpclattice_target_group_attachment(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    client = common.boto3.client(clfn)
    response = []

    if id is None:
      log.warning("Must pass target group id")
      return True
    else:
        if id.startswith("tg-"):
            try:
                response1 = client.get_target_group(targetGroupIdentifier=id)
            except Exception as e:
                common.handle_error(
                    e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
            ## doesn't work
            #common.write_import(type, id, None)
            context.rproc["aws_vpclattice_target_group_attachment."+id] = True

    return True



def get_aws_vpclattice_resource_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    client = common.boto3.client(clfn)
    response = []

    if id is None:
        log_warning("WARNING: must pass ARN of service network or service")
        return True

    else:
        if id.startswith("arn:"):
            try:
                response = client.get_resource_policy(resourceArn=id)
            except Exception as e:
                common.handle_error(
                    e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

            common.write_import(type, id, None)
            context.rproc["aws_vpclattice_resource_policy."+id] = True

    return True


def get_aws_vpclattice_listener(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    client = common.boto3.client(clfn)
    if context.debug:
        log.debug("--client")
    response = []

    if context.debug:
        log.debug("Paginator")
    if id is None:
        log_warning("WARNING must provide serviceIdentifier as parameter for get_aws_vpclattice_listener")
    else:
        try:
            getfn = getattr(client, descfn)
            response1 = getfn(serviceIdentifier=id)  # special

            response = response1[topkey]
        except Exception as e:
            common.handle_error(
                e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    if response == []:
        if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
        return True

    for j in response:
        retid = j['id']
        theid = id+"/"+retid
        common.write_import(type, theid, None)
        common.add_dependancy("aws_vpclattice_listener_rule", theid)
        context.rproc["aws_vpclattice_listener."+id] = True

    return True


#  need to deal with id  svc/ruleid - extract ruleid
def get_aws_vpclattice_listener_rule(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    client = common.boto3.client(clfn)
    if context.debug:
        log.debug("--client")
    response = []

    if context.debug:
        log.debug("Paginator")

    if id is None:
        log_warning("WARNING must provide serviceIdentifier/ListenerId as parameter for get_aws_vpclattice_listener_rule")
    else:
        try:
            if "/" in id:  # print(f"{err=}")
                svid = id.split("/")[0]
                rlid = id.split("/")[1]
                #print(f"{svid=},{rlid=}")
                getfn = getattr(client, descfn)
                response1 = getfn(serviceIdentifier=svid,
                                  listenerIdentifier=rlid)  # special
                response = response1[topkey]
            else:
                log.info(
                    "WARNING must provide serviceIdentifier/ListenerId as parameter for get_aws_vpclattice_listener_rule")
        except Exception as e:
            common.handle_error(
                e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    if response == []:
        if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
        return True

    for j in response:
        retid = j['id']
        theid = svid+"/"+rlid+"/"+retid
        common.write_import(type, theid, None)
    context.rproc["aws_vpclattice_listener_rule."+id] = True

    return True

# Generic


def get_aws_vpc_lattice(type, id, clfn, descfn, topkey, key, filterid):
   if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      client = common.boto3.client(clfn)
      response = []
      if id is None:
         log_warning("WARNING: must provide id for "+type)
         return True

      if id.startswith("sn-"):
         try:
               paginator = client.get_paginator(descfn)
               for page in paginator.paginate(serviceNetworkIdentifier=id):
                  response.extend(page[topkey])
         except botocore.exceptions.OperationNotPageableError as err:
               # print(f"{err=}")
               getfn = getattr(client, descfn)
               response1 = getfn(serviceNetworkIdentifier=id)  # special
               response = response1[topkey]

      else:
         log_warning("WARNING: No id or invalid id provided for "+type, id)
         return True

      #print(str(response))
      if response == []:
         if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
         pkey = type+"."+id
         context.rproc[pkey] = True
         return True

      for j in response:
         #print("j=", str(j))
         retid = j['id']
         theid = retid
         common.write_import(type, theid, None)
      pkey = type+"."+id
      context.rproc[pkey] = True

   except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

   return True

# aws_vpclattice_resource_gateway

def get_aws_vpclattice_resource_gateway(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        #client = common.boto3.client(clfn,config=config)
        client = common.boto3.client(clfn)
        if id is None:
            log.info("pag")
            paginator = client.get_paginator(descfn)
            log.info("for")
            for page in paginator.paginate(status="ACTIVE"):
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 
                common.add_dependancy("aws_vpclattice_resource_configuration", j[key])

        else:      
            response = client.get_resource_gateway(resourceGatewayIdentifier=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_vpclattice_resource_configuration", j[key])
            pkey=type+"."+id
            context.rproc[pkey] = True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_vpclattice_resource_configuration
def get_aws_vpclattice_resource_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10, 'mode': 'standard'})
        #client = common.boto3.client(clfn, config=config)
        client = common.boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)

        else:
            if id.startswith("rcfg-"):
                response = client.get_resource_configuration(resourceConfigurationIdentifier=id)
                if response == []:
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                j=response
                common.write_import(type, j[key], None)
                pkey=type+"."+id
                context.rproc[pkey] = True
            elif id.startswith("rgw-"):
                response = client.list_resource_configurations(resourceGatewayIdentifier=id)
                if response == []:
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                j=response
                common.write_import(type, j[key], None)
                pkey=type+"."+id
                context.rproc[pkey] = True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True



