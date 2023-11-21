import common
import globals

def get_aws_kms_key(type,id,clfn,descfn,topkey,key,filterid):
    #if globals.debug: print("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    print("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response=common.call_boto3(clfn,descfn,topkey,id)
    #print("-9a->"+str(response))
    if response == []: 
        print("empty response returning") 
        return   
    try:
        for j in response: 
            theid=j[key]
            ka="k-"+theid
            #print(ka)
            if id is not None and id != theid:
                continue
            else:
                common.write_import(type,theid,ka) 
    except Exception as e:
        print(f"{e=}")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno) 

    return