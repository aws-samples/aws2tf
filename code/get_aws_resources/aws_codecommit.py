import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect


def get_aws_codecommit_repository(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
          " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []:
            if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
            return True
        for j in response:
            if id is None:
                common.write_import(type, j[key], None)
            elif "-" in id:
                if id == j['repositoryId']:
                    common.write_import(type, j[key], None)
            else:
                if id == j['repositoryName']:
                    common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
