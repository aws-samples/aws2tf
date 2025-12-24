import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect


def get_aws_appmesh_virtual_service(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_virtual_services()
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualServiceName']
                common.write_import(type,pkey,None) 
            pkey="aws_appmesh_virtual_service."+j['meshName']
            context.rproc[pkey]=True

        else:          
            response = client.list_virtual_services(meshName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualServiceName']
                common.write_import(type,pkey,None)
            pkey="aws_appmesh_virtual_service."+id
            context.rproc[pkey]=True
            
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_appmesh_virtual_router(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_virtual_routers()
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualRouterName']
                common.write_import(type,pkey,None) 
            pkey="aws_appmesh_virtual_router."+j['meshName']
            context.rproc[pkey]=True

        else:      
            response = client.list_virtual_routers(meshName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualRouterName']
                common.write_import(type,pkey,None)
            pkey="aws_appmesh_virtual_router."+id
            context.rproc[pkey]=True
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_appmesh_virtual_node(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_virtual_nodes()
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualNodeName']
                common.write_import(type,pkey,None) 
            pkey="aws_appmesh_virtual_node."+j['meshName']
            context.rproc[pkey]=True

        else:      
            response = client.list_virtual_nodes(meshName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualNodeName']
                common.write_import(type,pkey,None)
            pkey="aws_appmesh_virtual_node."+id
            context.rproc[pkey]=True
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_appmesh_virtual_gateway(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_virtual_gateways()
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualGatewayName']
                common.write_import(type,pkey,None) 
            pkey="aws_appmesh_virtual_gateway."+j['meshName']
            context.rproc[pkey]=True

        else:      
            response = client.list_virtual_gateways(meshName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=j['meshName']+"/"+j['virtualGatewayName']
                common.write_import(type,pkey,None)
                common.add_dependancy("aws_appmesh_gateway_route",pkey)
            pkey="aws_appmesh_virtual_gateway."+id
            context.rproc[pkey]=True
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_appmesh_gateway_route(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("ERROR: must pass mesh name/gateway name")
            return True

        else:  
            if "/" in id:    
                mn=id.split("/")[0]
                gwn=id.split("/")[1]
            else:
                log.info("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            response = client.list_gateway_routes(meshName=mn,virtualGatewayName=gwn)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=mn+"/"+gwn+"/"+j['gatewayRouteName']
                common.write_import(type,pkey,None)
                common.add_dependancy("aws_appmesh_gateway_route",pkey)
            pkey="aws_appmesh_gateway_route."+mn+"/"+gwn
            context.rproc[pkey]=True
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True