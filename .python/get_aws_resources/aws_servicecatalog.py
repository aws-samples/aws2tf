import common
import boto3
import globals
import inspect


def get_aws_servicecatalog_portfolio(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                theid=j[key]
                common.write_import(type,theid,None) 
                common.add_dependancy("aws_servicecatalog_product", theid)
                common.add_dependancy("aws_servicecatalog_constraint", theid)
                common.add_dependancy("aws_servicecatalog_principal_portfolio_association", theid)

        else:      
            response = client.describe_portfolio(Id=id)
            if response['PortfolioDetail'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['PortfolioDetail']
            theid=j[key]
            common.write_import(type,theid,None) 
            common.add_dependancy("aws_servicecatalog_product", theid)
            common.add_dependancy("aws_servicecatalog_constraint", theid)
            common.add_dependancy("aws_servicecatalog_principal_portfolio_association", theid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_servicecatalog_product(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
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
                print("Empty response for "+type+ " id="+str(id)+" returning"); 
                return True
            for j in response:
                theid=j['ProductViewSummary'][key]
                common.write_import(type,theid,None) 

        else:      
            response = client.search_products_as_admin(PortfolioId=id)
            if response[topkey] == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning"); 
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                theid=j['ProductViewSummary'][key]
                common.write_import(type,theid,None) 
            pkey=type+"."+id
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


#aws_servicecatalog_constraint#
def get_aws_servicecatalog_constraint(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass PortfolioId for get_aws_servicecatalog_constraint")
            return True
        else:
            response = client.list_constraints_for_portfolio(PortfolioId=id)
            if response[topkey] == []:
                print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                theid=j[key]
                common.write_import(type, theid, None)
            pkey=type+"."+id
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_servicecatalog_principal_portfolio_association(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass PortfolioId for get_aws_servicecatalog_constraint")
            return True

        else:
            response = client.list_principals_for_portfolio(PortfolioId=id)
            if response[topkey] == []:
                print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            
            for j in response[topkey]:
                theid=j[key]
                tkey="en,"+theid+","+id+","+j['PrincipalType']
                common.write_import(type, tkey, None)
            pkey=type+"."+id
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

#aws_servicecatalog_product_portfolio_association#
def get_aws_servicecatalog_product_portfolio_association(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
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
                print("Empty response for "+type+ " id="+str(id)+" returning");
                return True
            for j in response:
                theid=j[key]
                common.write_import(type, theid, None)

        else:
            response = client.describe_portfolio(Id=id)
            if response['PortfolioDetail'] == []:
                print("Empty response for "+type+ " id="+str(id)+" returning");
                return True
            j=response['PortfolioDetail']
            theid=j[key]
            common.write_import(type, theid, None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True





