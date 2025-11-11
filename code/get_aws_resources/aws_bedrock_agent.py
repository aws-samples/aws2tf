import common
import boto3
import context
import inspect

def get_aws_bedrockagent_agent(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            #print(str(response))
            for j in response:
                aid=j[key]
                common.write_import(type,j[key],"r-"+aid) 
                resp2=client.list_agent_versions(agentId=aid)
                for k in resp2['agentVersionSummaries']:
                    av=k['agentVersion']
                    theid=aid+","+av
                    if av=="DRAFT":
                        common.add_dependancy("aws_bedrockagent_agent_knowledge_base_association",theid)
                        common.add_dependancy("aws_bedrockagent_agent_action_group",theid)
                common.add_dependancy("aws_bedrockagent_agent_alias",aid)

        else:      
            response = client.get_agent(agentId=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['agent']
            aid=j['agentId']
      
            common.write_import(type,aid,None)
            resp2=client.list_agent_versions(agentId=aid)
            for k in resp2['agentVersionSummaries']:
                av=k['agentVersion']
                theid=aid+","+av
                if av=="DRAFT":
                    common.add_dependancy("aws_bedrockagent_agent_knowledge_base_association",theid)
                    common.add_dependancy("aws_bedrockagent_agent_action_group",theid)
            common.add_dependancy("aws_bedrockagent_agent_alias",aid)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_bedrockagent_knowledge_base(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],"r-"+j[key]) 

        else:      
            response = client.get_knowledge_base(knowledgeBaseId=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['knowledgeBase']
            common.write_import(type,j[key],"r-"+j[key])
            common.add_dependancy("aws_bedrockagent_data_source", j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_bedrockagent_agent_knowledge_base_association
def get_aws_bedrockagent_agent_knowledge_base_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("ERROR: id is None with type="+type)
            return True

        else:
            if "," in id: 
                aid, vid = id.split(",")
                pkey=type+"."+id
                response = client.list_agent_knowledge_bases(agentId=aid, agentVersion=vid)
                if response == []: 
                    if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                    context.rproc[pkey] = True
                    return True
                for j in response['agentKnowledgeBaseSummaries']:
                    kid=j['knowledgeBaseId']
                    theid=aid+","+vid+","+kid
                    common.write_import(type, theid, None)
                    common.add_dependancy("aws_bedrockagent_knowledge_base", kid)
                context.rproc[pkey] = True
            else:
                print("ERROR: with id - expected agentid,versionid got",id)


    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

#aws_bedrockagent_data_source
def get_aws_bedrockagent_data_source(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("ERROR: id is None with type="+type)
            return True

        else:
            pkey=type+"."+id
            response = client.list_data_sources(knowledgeBaseId=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                context.rproc[pkey] = True
                return True
            for j in response[topkey]:
                theid=j[key]+","+id
                common.write_import(type, theid, None)
            context.rproc[pkey] = True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

def get_aws_bedrockagent_agent_alias(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("ERROR: id is None with type="+type)
            return True

        else:
            pkey=type+"."+id
            response = client.list_agent_aliases(agentId=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                context.rproc[pkey] = True
                return True
            for j in response[topkey]:
                theid=j[key]+","+id
                common.write_import(type, theid, None)
            context.rproc[pkey] = True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
    

def get_aws_bedrockagent_agent_action_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("ERROR: id is None with type="+type)
            return True

        else:
            if "," in id: 
                aid, vid = id.split(",")
                pkey=type+"."+id
                response = client.list_agent_action_groups(agentId=aid,agentVersion=vid)
                if response == []: 
                    if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                    context.rproc[pkey] = True
                    return True
                for j in response['actionGroupSummaries']:
                    gid=j['actionGroupId']
                    theid=gid+","+aid+","+vid
                    common.write_import(type, theid, None)
                context.rproc[pkey] = True
            else:
                print("ERROR: with id - expected agentid,versionid got",id)


    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True