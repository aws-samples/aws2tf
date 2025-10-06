import globals
import os
import sys
import boto3
import base64
import resources
import common
import shutil
import inspect
from timed_interrupt import timed_int

from fixtf_aws_resources import arn_dict
from fixtf_aws_resources import aws_common
from fixtf_aws_resources import fixtf_accessanalyzer
from fixtf_aws_resources import fixtf_acm
from fixtf_aws_resources import fixtf_acm_pca
from fixtf_aws_resources import fixtf_amp
from fixtf_aws_resources import fixtf_amplify
from fixtf_aws_resources import fixtf_apigateway
from fixtf_aws_resources import fixtf_apigatewayv2
from fixtf_aws_resources import fixtf_appconfig
from fixtf_aws_resources import fixtf_appflow
from fixtf_aws_resources import fixtf_appintegrations
from fixtf_aws_resources import fixtf_application_autoscaling
from fixtf_aws_resources import fixtf_application_insights
from fixtf_aws_resources import fixtf_appmesh
from fixtf_aws_resources import fixtf_apprunner
from fixtf_aws_resources import fixtf_appstream
from fixtf_aws_resources import fixtf_appsync
from fixtf_aws_resources import fixtf_athena
from fixtf_aws_resources import fixtf_auditmanager
from fixtf_aws_resources import fixtf_autoscaling
from fixtf_aws_resources import fixtf_autoscaling_plans
from fixtf_aws_resources import fixtf_backup
from fixtf_aws_resources import fixtf_batch
from fixtf_aws_resources import fixtf_bedrock
from fixtf_aws_resources import fixtf_bedrock_agent
from fixtf_aws_resources import fixtf_billingconductor
from fixtf_aws_resources import fixtf_budgets
from fixtf_aws_resources import fixtf_ce
from fixtf_aws_resources import fixtf_chime
from fixtf_aws_resources import fixtf_chime_sdk_media_pipelines
from fixtf_aws_resources import fixtf_chime_sdk_voice
from fixtf_aws_resources import fixtf_cleanrooms
from fixtf_aws_resources import fixtf_cloud9
from fixtf_aws_resources import fixtf_cloudcontrol
from fixtf_aws_resources import fixtf_cloudformation
from fixtf_aws_resources import fixtf_cloudfront
from fixtf_aws_resources import fixtf_cloudhsmv2
from fixtf_aws_resources import fixtf_cloudsearch
from fixtf_aws_resources import fixtf_cloudtrail
from fixtf_aws_resources import fixtf_logs
from fixtf_aws_resources import fixtf_codeartifact
from fixtf_aws_resources import fixtf_codebuild
from fixtf_aws_resources import fixtf_codecatalyst
from fixtf_aws_resources import fixtf_codecommit
from fixtf_aws_resources import fixtf_codedeploy
from fixtf_aws_resources import fixtf_codeguru_reviewer
from fixtf_aws_resources import fixtf_codeguruprofiler
from fixtf_aws_resources import fixtf_codepipeline
from fixtf_aws_resources import fixtf_codestar_connections
from fixtf_aws_resources import fixtf_codestar_notifications
from fixtf_aws_resources import fixtf_cognito_identity
from fixtf_aws_resources import fixtf_cognito_idp
from fixtf_aws_resources import fixtf_comprehend
from fixtf_aws_resources import fixtf_config
from fixtf_aws_resources import fixtf_connect
from fixtf_aws_resources import fixtf_controltower
from fixtf_aws_resources import fixtf_cur
from fixtf_aws_resources import fixtf_customer_profiles
from fixtf_aws_resources import fixtf_dataexchange
from fixtf_aws_resources import fixtf_datapipeline
from fixtf_aws_resources import fixtf_datasync
from fixtf_aws_resources import fixtf_datazone
from fixtf_aws_resources import fixtf_dax
from fixtf_aws_resources import fixtf_detective
from fixtf_aws_resources import fixtf_devicefarm
from fixtf_aws_resources import fixtf_directconnect
from fixtf_aws_resources import fixtf_dlm
from fixtf_aws_resources import fixtf_dms
from fixtf_aws_resources import fixtf_docdb
from fixtf_aws_resources import fixtf_docdb_elastic
from fixtf_aws_resources import fixtf_ds
from fixtf_aws_resources import fixtf_dynamodb
from fixtf_aws_resources import fixtf_ebs
from fixtf_aws_resources import fixtf_ec2
from fixtf_aws_resources import fixtf_ecr_public
from fixtf_aws_resources import fixtf_ecr
from fixtf_aws_resources import fixtf_ecs
from fixtf_aws_resources import fixtf_efs
from fixtf_aws_resources import fixtf_eks
from fixtf_aws_resources import fixtf_elasticache
from fixtf_aws_resources import fixtf_elasticbeanstalk
from fixtf_aws_resources import fixtf_elastictranscoder
from fixtf_aws_resources import fixtf_elb
from fixtf_aws_resources import fixtf_elbv2
from fixtf_aws_resources import fixtf_emr
from fixtf_aws_resources import fixtf_emr_containers
from fixtf_aws_resources import fixtf_emrserverless
from fixtf_aws_resources import fixtf_es
from fixtf_aws_resources import fixtf_events
from fixtf_aws_resources import fixtf_evidently
from fixtf_aws_resources import fixtf_finspace
from fixtf_aws_resources import fixtf_firehose
from fixtf_aws_resources import fixtf_fis
from fixtf_aws_resources import fixtf_fms
from fixtf_aws_resources import fixtf_fsx
from fixtf_aws_resources import fixtf_gamelift
from fixtf_aws_resources import fixtf_glacier
from fixtf_aws_resources import fixtf_globalaccelerator
from fixtf_aws_resources import fixtf_glue
from fixtf_aws_resources import fixtf_grafana
from fixtf_aws_resources import fixtf_guardduty
from fixtf_aws_resources import fixtf_iam
from fixtf_aws_resources import fixtf_identitystore
from fixtf_aws_resources import fixtf_imagebuilder
from fixtf_aws_resources import fixtf_inspector
from fixtf_aws_resources import fixtf_inspector2
from fixtf_aws_resources import fixtf_internetmonitor
from fixtf_aws_resources import fixtf_iot
from fixtf_aws_resources import fixtf_ivs
from fixtf_aws_resources import fixtf_ivschat
from fixtf_aws_resources import fixtf_kafka
from fixtf_aws_resources import fixtf_kafkaconnect
from fixtf_aws_resources import fixtf_kendra
from fixtf_aws_resources import fixtf_keyspaces
from fixtf_aws_resources import fixtf_kinesis
from fixtf_aws_resources import fixtf_kinesisanalytics
from fixtf_aws_resources import fixtf_kinesisanalyticsv2
from fixtf_aws_resources import fixtf_kinesisvideo
from fixtf_aws_resources import fixtf_kms
from fixtf_aws_resources import fixtf_lakeformation
from fixtf_aws_resources import fixtf_lambda
from fixtf_aws_resources import fixtf_lex
from fixtf_aws_resources import fixtf_lexv2_models
from fixtf_aws_resources import fixtf_license_manager
from fixtf_aws_resources import fixtf_lightsail
from fixtf_aws_resources import fixtf_location
from fixtf_aws_resources import fixtf_macie2
from fixtf_aws_resources import fixtf_mediaconvert
from fixtf_aws_resources import fixtf_medialive
from fixtf_aws_resources import fixtf_mediapackage
from fixtf_aws_resources import fixtf_mediastore
from fixtf_aws_resources import fixtf_memorydb
from fixtf_aws_resources import fixtf_mq
from fixtf_aws_resources import fixtf_mwaa
from fixtf_aws_resources import fixtf_neptune
from fixtf_aws_resources import fixtf_network_firewall
from fixtf_aws_resources import fixtf_networkmanager
from fixtf_aws_resources import fixtf_opensearch
from fixtf_aws_resources import fixtf_opsworks
from fixtf_aws_resources import fixtf_organizations
from fixtf_aws_resources import fixtf_outposts
from fixtf_aws_resources import fixtf_pinpoint
from fixtf_aws_resources import fixtf_pipes
from fixtf_aws_resources import fixtf_polly
from fixtf_aws_resources import fixtf_pricing
from fixtf_aws_resources import fixtf_qldb
from fixtf_aws_resources import fixtf_quicksight
from fixtf_aws_resources import fixtf_ram
from fixtf_aws_resources import fixtf_rds
from fixtf_aws_resources import fixtf_redshift
from fixtf_aws_resources import fixtf_redshift_data
from fixtf_aws_resources import fixtf_redshift_serverless
from fixtf_aws_resources import fixtf_resource_explorer_2
from fixtf_aws_resources import fixtf_resource_groups
from fixtf_aws_resources import fixtf_resourcegroupstaggingapi
from fixtf_aws_resources import fixtf_rolesanywhere
from fixtf_aws_resources import fixtf_route53
from fixtf_aws_resources import fixtf_route53_recovery_control_config
from fixtf_aws_resources import fixtf_route53_recovery_readiness
from fixtf_aws_resources import fixtf_route53domains
from fixtf_aws_resources import fixtf_route53resolver
from fixtf_aws_resources import fixtf_rum
from fixtf_aws_resources import fixtf_s3
from fixtf_aws_resources import fixtf_s3control
from fixtf_aws_resources import fixtf_s3outposts
from fixtf_aws_resources import fixtf_s3tables
from fixtf_aws_resources import fixtf_sagemaker
from fixtf_aws_resources import fixtf_scheduler
from fixtf_aws_resources import fixtf_schemas
from fixtf_aws_resources import fixtf_secretsmanager
from fixtf_aws_resources import fixtf_securityhub
from fixtf_aws_resources import fixtf_securitylake
from fixtf_aws_resources import fixtf_serverlessrepo
from fixtf_aws_resources import fixtf_servicecatalog
from fixtf_aws_resources import fixtf_servicediscovery
from fixtf_aws_resources import fixtf_servicequotas
from fixtf_aws_resources import fixtf_ses
from fixtf_aws_resources import fixtf_sesv2
from fixtf_aws_resources import fixtf_shield
from fixtf_aws_resources import fixtf_signer
from fixtf_aws_resources import fixtf_simpledb
from fixtf_aws_resources import fixtf_sns
from fixtf_aws_resources import fixtf_sqs
from fixtf_aws_resources import fixtf_ssm
from fixtf_aws_resources import fixtf_ssm_contacts
from fixtf_aws_resources import fixtf_ssm_incidents
from fixtf_aws_resources import fixtf_sso_admin
from fixtf_aws_resources import fixtf_stepfunctions
from fixtf_aws_resources import fixtf_storagegateway
from fixtf_aws_resources import fixtf_sts
from fixtf_aws_resources import fixtf_swf
from fixtf_aws_resources import fixtf_synthetics
from fixtf_aws_resources import fixtf_timestreamwrite
from fixtf_aws_resources import fixtf_transcribe
from fixtf_aws_resources import fixtf_transfer
from fixtf_aws_resources import fixtf_vpc_lattice
from fixtf_aws_resources import fixtf_waf
from fixtf_aws_resources import fixtf_waf_regional
from fixtf_aws_resources import fixtf_wafv2
from fixtf_aws_resources import fixtf_worklink
from fixtf_aws_resources import fixtf_workspaces
from fixtf_aws_resources import fixtf_xray


##############################################


def fixtf(ttft,tf):
  
    rf=tf+".out"
    tf2=tf+".tf"

#### Optimisation ???????
    #if os.path.isfile("imported/"+tf2):
    #    com = "cp imported/"+tf2+" ."
    #    rout = common.rc(com)
    #    com = "mv rf imported/"+rf
    #    rout = common.rc(com)

    ## will this check break things ?
    # check if aws_*.tf exists already
    if os.path.isfile(tf2):
         if globals.debug:
            print("File exists: " + tf2+ " skipping ...")                 
         return 
    else:
        if globals.debug:  print("processing "+tf2)


    if globals.debug:
        print(ttft+" fixtf "+tf+".out") 
   
# open the *.out file

    try:
        f1 = open(rf, 'r')
    except:
        print("no "+rf)
        return
    
    clfn, descfn, topkey, key, filterid = resources.resource_data(ttft, None)
    if clfn is None:
        print("ERROR: clfn is None with type="+ttft)
        print("exit 015")
        timed_int.stop()
        exit()

    clfn=clfn.replace('-','_')
    callfn="fixtf_"+clfn
    if globals.debug: print("callfn="+callfn+" ttft="+ttft)

    Lines = f1.readlines()
    f1.close()
    #print("getfn for fixtf2."+ttft+" "+tf2)
    #with open(tf2, "a") as f2:

    ##
    ## Prescan blocks   
    ##
    globals.elastirep=False
    globals.elastigrep=False
    globals.elasticc=False
    globals.kinesismsk=False
    globals.destbuck=False


    if ttft=="aws_s3_bucket_replication_configuration":
        for t1 in Lines:
            t1=t1.strip()
            if globals.debug5: print("DEBUG5: pre scan block1 : t1=", t1)
            skip=0
            tt1=t1.split("=")[0].strip()
            if tt1=="bucket":
                try:
                    tt2=t1.split("=")[1].strip().strip('\"')
                    if "arn:aws:s3" in tt2:
                        tt2=tt2.split(":")[-1]
                        if globals.debug5: print("DEBUG5: pre scan block 2: common.add_dep bucket_name=", tt2)
                        common.add_dependancy("aws_s3_bucket", tt2)
                except:
                    tt2=""

    if ttft=="aws_elasticache_cluster":
        for t1 in Lines:
            t1=t1.strip()
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
            if tt1=="replication_group_id":
                if tt2 != "null": 
                    globals.elastirep=True
                    if globals.debug5: print("***** set true *****")

    if ttft=="aws_elasticache_replication_group":
        for t1 in Lines:
            t1=t1.strip()
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
            if tt1=="global_replication_group_id":
                if tt2 != "null": 
                    globals.elastigrep=True
                    #print("***** set true *****")
            elif tt1=="num_cache_clusters":
                if tt2 != "null": 
                    globals.elasticc=True


    if ttft=="aws_kinesis_firehose_delivery_stream":
        for t1 in Lines:
            t1=t1.strip()
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
            if "msk_source_configuration" in tt1:
                    globals.kinesismsk=True
                    #print("***** set true *****")



    if ttft=="aws_db_instance":
        for t1 in Lines:
            t1=t1.strip()
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
            if tt1=="replicate_source_db":
                if tt2 != "null": globals.repdbin=True

    elif ttft=="aws_lambda_event_source_mapping":
        for t1 in Lines:
            t1=t1.strip()
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
            if tt1=="destination_arn":
                if tt2 == "null": globals.levsmap=True

    accessl=0
    cnxl=0
    globals.lbskipaacl=False
    globals.lbskipcnxl=False
    globals.mskcfg=False

    if ttft=="aws_lb":
        for t1 in Lines:
            t1=t1.strip()
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
            if tt1=="access_logs": accessl=1;cnxl=0
            if tt1=="connection_logs": accessl=0;cnxl=1
            if tt1=="enabled":
                if tt2 == "false" and accessl==1: globals.lbskipaacl=True
                if tt2 == "false" and cnxl==1: globals.lbskipcnxl=True
                else: globals.lbenabled=True

    ##
    ## Block stripping init
    ##
    globals.lbc=0
    globals.rbc=0
    globals.stripblock=""
    globals.stripblock2=""
    globals.stripstart=""
    globals.stripend=""
    #if ttft=="aws_lb_listener_rule" or ttft=="aws_lb_listener":
    #    globals.stripblock="forward {"
    #    globals.stripstart="{"
    #    globals.stripend="}"
    if ttft=="aws_lb":
        globals.stripblock="subnet_mapping {"
        globals.stripstart="{"
        globals.stripend="}"


    if ttft=="aws_msk_cluster":
        globals.stripblock="configuration_info {"
        globals.stripstart="{"
        globals.stripend="}"


    if ttft=="aws_lambda_event_source_mapping" and globals.levsmap:
        globals.stripblock="destination_config {"
        globals.stripstart="{"
        globals.stripend="}"

    if ttft=="aws_wafv2_web_acl":
        globals.stripblock="rule {"
        globals.stripstart="{"
        globals.stripend="}"

    if ttft=="aws_instance":
        globals.stripblock="primary_network_interface {"
        globals.stripstart="{"
        globals.stripend="}"

    if ttft=="aws_kinesis_firehose_delivery_stream":
        if globals.kinesismsk:
            globals.stripblock="server_side_encryption {"
            globals.stripstart="{"
            globals.stripend="}"

    globals.gulejobmaxcap=False
    globals.ec2ignore=False
    globals.secid=""
    globals.secvid=""
    globals.dzd=""
    globals.connectinid=""

    #if globals.acc in tf2:
    #    tf2=tf2.replace(globals.acc, "__")


########################                       
###Generic block remover 
########################
    
    with open(tf2, "w") as f2:
        skip=0
        flag1=False
        flag2=tf
        nofind=0
        f2.write("##START,"+ttft+"\n")
        
        # And off we go around the out file again
        for t1 in Lines:
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
 
            try:   
                # does fixtf_aws_rsource exist ??
                getfn = getattr(eval(callfn), ttft)           
                #getfn = getattr(fixtf2, ttft)
            except Exception as e:
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print("** no fixtf2 for "+ttft+" calling generic fixtf2.aws_resource")
                nofind=1
                
            try:
                ####
                # common replacement code here
                # rhs=account number
                # rhs is still an arn
                # : in tt1 for quote it

                #call aws_common. fixtf
                skip,t1,flag1,flag2=aws_common.aws_common(ttft,t1,tt1,tt2,flag1,flag2)

                # call fixtf_aws_rsource if skip=0
                if skip==0:                
                    skip,t1,flag1,flag2=getfn(t1,tt1,tt2,flag1,flag2)

                #####
                ## block strip sections - 
                ####
                
                if globals.stripblock != "":
                    if globals.stripblock in t1: globals.lbc=1
                    elif globals.stripstart in t1 and globals.lbc>0: globals.lbc=globals.lbc+1
                    
                    if globals.stripend in t1 and globals.lbc>0:
                        globals.lbc=globals.lbc-1
                        skip=1
                    elif globals.lbc > 0: skip=1
                
                #print("t1="+t1)
	            #print("lbc="+str(globals.lbc)+" rbc="+str(globals.rbc)+" skip="+str(skip))

                #print("t1="+t1)
            except Exception as e:
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print("** error in "+ttft+" "+callfn+" OR .....")
                print("-- no fixtf for type:"+ttft+" callfn:"+callfn)
                print("-- no fixtf for "+tf+" calling generic fixtf2.aws_resource callfn="+callfn)
                print("t1="+str(t1)) 
                nofind=2
                skip,t1,flag1,flag2=aws_resource(t1,tt1,tt2,flag1,flag2)           
            #### 

            if skip == 0:
                f2.write(t1)



        # extra block removals in aws_lb
        if type=="aws_lb":
            if globals.lbskipaacl:
                shutil.move(tf2, tf2+".saved")
                globals.stripblock="access_logs"
                with open(tf2+".saved", "e") as f1:
                    Lines = f1.readlines()
                with open(tf2, "w") as f2:
                    for t1 in Lines:
                        t1=t1.strip()
                        tt1=t1.split("=")[0].strip()
                        if globals.stripblock != "":
                            if globals.stripblock in t1: globals.lbc=1
                            elif globals.stripstart in t1 and globals.lbc>0: globals.lbc=globals.lbc+1
                            
                            if globals.stripend in t1 and globals.lbc>0:
                                globals.lbc=globals.lbc-1
                                skip=1
                            elif globals.lbc > 0: skip=1
            if globals.lbskipcnxl:
                shutil.move(tf2, tf2+".saved")
                globals.stripblock="connection_logs"
                with open(tf2+".saved", "e") as f1:
                    Lines = f1.readlines()
                with open(tf2, "w") as f2:
                    for t1 in Lines:
                        t1=t1.strip()
                        tt1=t1.split("=")[0].strip()
                        if globals.stripblock != "":
                            if globals.stripblock in t1: globals.lbc=1
                            elif globals.stripstart in t1 and globals.lbc>0: globals.lbc=globals.lbc+1
                            
                            if globals.stripend in t1 and globals.lbc>0:
                                globals.lbc=globals.lbc-1
                                skip=1
                            elif globals.lbc > 0: skip=1



        if nofind > 0:
           print("WARNING: No fixtf for "+tf+" calling generic fixtf2.aws_resource nofind="+str(nofind))
        
        
        
        ## move *.out to impoted
        #shutil.move(rf, "imported/"+rf)

def remove_block():





    return        

def aws_resource(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 


# generic replace of acct and region in arn
def globals_replace(t1,tt1,tt2):
    if globals.debug: print("GR start:",t1)
    if "format(" in tt2: return t1
    ends=""
    tt2=tt2.replace("%", "%%")
    if tt2.startswith('[') and tt1 != "managed_policy_arns" and "," in tt2:
        tt2=tt2.replace('[','').replace(']','').replace('"','').replace(' ','')
        arns=tt2.split(',')
        if globals.debug: print("Globals replace an array:"+str(arns))
        fins=""
        for arn in arns:
            tt2=str(arn)
            
            ends=""
            if ":"+globals.acc+":" in tt2:
                #print("Globals replace arn:"+str(tt2))
                while ":"+globals.acc+":" in tt2:
                    r1=tt2.find(":"+globals.region+":")
                    a1=tt2.find(":"+globals.acc+":")
                    #print("--> r1="+ str(r1) + " ")
                    #print("--> a1="+ str(a1) + " ")
                    if r1>0 and r1 < a1:
                            #print("--> 6a")
                            ends=ends+",data.aws_region.current.region"
                            tt2=tt2[:r1]+":%s:"+tt2[r1+globals.regionl+2:]

                    a1=tt2.find(":"+globals.acc+":")
                    tt2=tt2[:a1]+":%s:"+tt2[a1+14:]
                    
                    ends=ends+",data.aws_caller_identity.current.account_id"
                    #if "\\" not in tt2:
                    #    tt2=tt2.replace('"', '\\"')
            
                    #print("t1="+t1)
                    #print("tt2="+tt2)
                    
                    t2 = 'format("'+tt2+ '"' +ends+'),'
                    fins=fins+t2
            else:
                return t1
        if fins=="":return t1
        fins=fins.rstrip(',')
        fins="["+fins+"]\n"
        fins=tt1+" = "+fins
        #print("fins=",str(fins))
        t1=fins

    else:
        if ":"+globals.acc+":" in tt2:
            while ":"+globals.acc+":" in tt2:
                    #print("--> 5")
                    r1=tt2.find(":"+globals.region+":")
                    a1=tt2.find(":"+globals.acc+":")
                    #print("--> r1="+ str(r1) + " ")
                    #print("--> a1="+ str(a1) + " ")
                    if r1>0 and r1 < a1:
                            #print("--> 6a")
                            ends=ends+",data.aws_region.current.region"
                            tt2=tt2[:r1]+":%s:"+tt2[r1+globals.regionl+2:]

                    a1=tt2.find(":"+globals.acc+":")
                    tt2=tt2[:a1]+":%s:"+tt2[a1+14:]
                    
                    ends=ends+",data.aws_caller_identity.current.account_id"
                    #if "\\" not in tt2:
                    #    tt2=tt2.replace('"', '\\"')
            
                    #print("t1="+t1)
                    
                    if globals.debug: print("out tt2="+tt2)
                    if "[" in tt2:
                        tt2=tt2.lstrip("[").rstrip("]").lstrip('"').rstrip('"')
                        if globals.debug: print("in tt2="+tt2)
                        t1 = tt1+' = [format("' + tt2 + '"' + ends +')]\n'
                    else:
                        t1 = tt1+' = format("'+tt2+ '"' +ends+')\n'
                    
    
    #if tt1 == "managed_policy_arns":
    #    tt2=tt2.replace('[','')
    #    tt2=tt2.replace(']','')
    #    tt2=tt2.replace('"','')
    #    t1 = tt1+' = [format("' + tt2 + '"' + ends +')]\n'
    
    if globals.debug: print("GR finish:="+t1)
    return t1



def rhs_replace(t1,tt1,tt2):
    ends=""

    if "{" not in tt2 and "[" not in tt2:  # so probably not a policy 

        while globals.acc in tt2:
                    #print("--> 5b",tt2)
                    r1=tt2.find(globals.region)
                    a1=tt2.find(globals.acc)
                    #print("--> r1="+ str(r1) + " ")
                    #print("--> a1="+ str(a1) + " ")
                    if r1>0 and a1>0 and r1 < a1: # there is region and it comes 1st
                            #print("--> 6a")
                            ends=ends+",data.aws_region.current.region"
                            tt2=tt2[:r1]+"%s"+tt2[r1+globals.regionl:]
                            a1=tt2.find(globals.acc)
                            tt2=tt2[:a1]+"%s"+tt2[a1+12:]
                            ends=ends+",data.aws_caller_identity.current.account_id"
                    if r1>0 and a1>0 and r1 > a1: # there is region and it comes 2nd
                            #print("--> 6b")
                            ends=ends+",data.aws_caller_identity.current.account_id"         
                            tt2=tt2[:r1]+"%s"+tt2[r1+globals.regionl:]
                            a1=tt2.find(globals.acc)
                            tt2=tt2[:a1]+"%s"+tt2[a1+12:]
                            ends=ends+",data.aws_region.current.region"
                
                    t1 = tt1+' = format("'+tt2+ '"' +ends+')\n'
        #print("t1="+t1)

    return t1


def deref_array(t1,tt1,tt2,ttft,prefix,skip):

    try:
        if tt2 == "null" or tt2 == "[]":
            skip=1
            return t1,skip
        tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
        cc=tt2.count(',')
        subs=""
        #if globals.debug: 
        if cc > 0:
            for i in range(cc+1):
                subn=tt2.split(',')[i]
                # aws_subnet
                if ttft == "aws_subnet": 
                    try:
                        if globals.subnetlist[subn]:
                            if not globals.dnet:
                                subs=subs + ttft + "." + subn + ".id,"
                                common.add_dependancy(ttft,subn)
                            else:
                                subs=subs + "data."+ttft + "." + subn + ".id,"
                                common.add_dependancy(ttft,subn)
                        else:
                            print("WARNING: subnet not in subnetlist" + subn)
                            subs=subs+'"'+subn+'"'+","
                    except KeyError:
                        print("WARNING: subnet not in subnet list " + subn+ " Resource may be referencing a subnet that no longer exists")
                        subs=subs+'"'+subn+'"'+","
                
                # security_group
                elif ttft == "aws_security_group": 
                    try:
                        if globals.sglist[subn]:
                            if not globals.dsgs:
                                subs=subs + ttft + "." + subn + ".id,"
                                common.add_dependancy(ttft,subn)
                            else:
                                subs=subs + "data."+ttft + "." + subn + ".id,"
                                common.add_dependancy(ttft,subn)
                        else:
                            print("WARNING: security group not in sg list" + subn)
                            subs=subs+'"'+subn+'"'+","
                    except KeyError:
                        print("WARNING: security group not in sg list " + subn+ " Resource may be referencing a security group that no longer exists")
                        subs=subs+'"'+subn+'"'+","
                #
                else:
                    subs=subs + ttft + "." + subn + ".id,"
                    common.add_dependancy(ttft,subn)

                
        elif cc == 0 and prefix in tt2:
            if ttft == "aws_subnet":
                try:
                    if globals.subnetlist[tt2]:
                        if not globals.dnet:
                            subs=ttft + "." + tt2 + ".id"
                            common.add_dependancy(ttft, tt2)
                        else:
                            subs="data."+ttft + "." + tt2 + ".id"
                            common.add_dependancy(ttft, tt2)
                    else:
                        print("WARNING: subnet not in subnet list" + tt2)
                        subs='"'+tt2+'"'
                except KeyError:
                    print("WARNING: subnet not in subnet list " + tt2+ " Resource may be referencing a subnet that no longer exists")
                    subs='"'+tt2+'"'

            elif ttft == "aws_security_group":
                try:
                    if globals.sglist[tt2]:
                        if not globals.dsgs:
                            subs=ttft + "." + tt2 + ".id"
                            common.add_dependancy(ttft, tt2)
                        else:
                            subs="data."+ttft + "." + tt2 + ".id"
                            common.add_dependancy(ttft, tt2)
                    else:
                        print("WARNING: security group not in sg list" + tt2)
                        subs='"'+tt2+'"'
                except KeyError:
                    print("WARNING: security group not in sg list " + tt2+ " Resource may be referencing a security group that no longer exists")
                    subs='"'+tt2+'"'
            else:
                subs=ttft + "." + tt2 + ".id"
                common.add_dependancy(ttft,tt2)

        
        if subs !="":       
            t1=tt1 + " = [" + subs + "]\n"
            t1=t1.replace(',]',']')
        
    
    except Exception as e:  
      print("t1=",t1)
      common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id) 
    
    return t1,skip



def deref_role_arn(t1,tt1,tt2):
    if tt2 == "null" or tt2 == "[]": return t1

    if tt2.startswith("arn:aws:events:"): print(tt2)

    if tt2.startswith("arn:aws:s3:::"):
        bn=tt2.split(":::")[-1]
        try:
            if globals.bucketlist[bn]:
                t1=tt1 + " = aws_s3_bucket.b-" + bn + ".arn\n"
                common.add_dependancy("aws_s3_bucket",bn)
        except KeyError as e:
            return t1
        
    elif tt2.startswith("arn:aws:elasticloadbalancing"):
        tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")
        t1=tt1 + " = aws_lb." + tarn + ".arn\n"
        common.add_dependancy("aws_lb",tt2)
    elif tt2.startswith("arn:aws:wafv2") and ":regional/webacl" in tt2:
        tarn=tt2.split("/webacl/")[-1]
        wn=tarn.split("/")[0]
        wi=tarn.split("/")[-1]
        tarn2="w-"+wi+"_"+wn+"_REGIONAL"
        t1=tt1 + " = aws_wafv2_web_acl." + tarn2 + ".arn\n"


    elif tt2.startswith("arn:aws:events:") and ":rule/" in tt2 and ":rule/aws.partner" not in tt2:
        rn=tt2.split("/")[-1]
        t1=tt1 + " = aws_cloudwatch_event_rule.default_" + rn + ".arn\n"
        #### TODO - note assumption it's on default event bus !
        common.add_dependancy("aws_cloudwatch_event_rule",rn)

    elif ":role/aws-service-role" in tt2:	
        t1=globals_replace(t1,tt1,tt2)
    elif ":role/" in tt2:
        if tt2.endswith("*"): return t1
        if tt2.startswith("arn:"): tt2=tt2.split('/')[-1]
        if tt2 in globals.rolelist:
            t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
            common.add_dependancy("aws_iam_role",tt2)
            
    # it's not an arn - just a name
    elif ":" not in tt2 and tt2 != "null": # assume it's a role name
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role", tt2)

    return t1

def deref_kms_key(t1,tt1,tt2):
    print("deref_kms_key 1: " + tt2)
    if "arn:aws:kms:" in tt2:
        print("deref_kms_key 2: " + tt2)
        t1=globals_replace(t1,tt1,tt2)
    return t1


def deref_s3(t1, tt1, tt2):
    if tt2.startswith("s3://"):
        sc=tt2.count("/")
        if sc>=3:
            bn=tt2.split("/",3)[2] 
            tn=tt2.split("/",3)[3] 
            #print("s3:",bn,tn)
            try:
                if globals.bucketlist[tt2]:
                    bv = "aws_s3_bucket.b-" + bn + ".bucket"
                    if tn !="":
                        t1=tt1 + ' = format("s3://%s/%s",'+bv+',"'+tn+'")\n'
                    else:
                        t1=tt1 + ' = format("s3://%s/",'+bv+')\n'
            except KeyError as e:
                return t1

    return t1



 #if tt1 == "security_groups": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
def deref_role_arn_array(t1,tt1,tt2):

    if tt2 == "null" or tt2 == "[]": return t1
    tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
    cc=tt2.count(',')
    subs=""
    if cc > 0:
        for i in range(cc+1):
            if ":role/" in tt2:
                subn=tt2.split(',')[i]
                subn=subn.strip('/')[-1]
                subs=subs + "aws_iam_role." + subn + ".arn,"
                common.add_dependancy("aws_iam_role",subn)

            
    if cc == 0:
        if ":role/" in tt2:
            tt2=tt2.split('/')[-1]
            subs=subs + "aws_iam_role." + tt2 + ".arn,"
            common.add_dependancy("aws_iam_role",tt2)
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')

    return t1

def deref_secret_arn_array(t1,tt1,tt2):
    if tt2 == "null" or tt2 == "[]": return t1
    tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
    cc=tt2.count(',')
    subs=""
    if cc > 0:
        for i in range(cc+1):
            if ":secret:" in tt2:
                subn=tt2.split(',')[i]
                sarn=subn
                tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
                subs=subs + "aws_secretsmanager_secret." + tarn + ".arn,"
                common.add_dependancy("aws_secretsmanager_secret",sarn)

            
    if cc == 0:
        if ":secret:" in tt2:
            sarn=tt2
            tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
            subs=subs + "aws_secretsmanager_secret." + tarn + ".arn,"
            common.add_dependancy("aws_secretsmanager_secret",sarn)
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')

    return t1



def deref_elb_arn_array(t1,tt1,tt2):
    if tt2 == "null" or tt2 == "[]": return t1
    tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
    cc=tt2.count(',')
    subs=""
    if cc > 0:
        for i in range(cc+1):
            subn=tt2.split(',')[i]
            tarn=subn
            rarn=tarn.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_")

            subn=subn.strip('/')[-1]
            subs=subs + "aws_lb." + rarn + ".arn,"
            common.add_dependancy("aws_lb",tarn)

            
    if cc == 0:
        tarn=tt2
        rarn=tarn.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_")
        tt2=tt2.split('/')[-1]
        subs=subs + "aws_lb." + rarn + ".arn,"
        common.add_dependancy("aws_lb",tarn)
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')

    return t1

#### other arn derefs here
def generic_deref_arn(t1, tt1, tt2):
    if globals.debug: print("Here",t1)
    try:
        if tt2.endswith("*"): return t1
        if globals.debug: print("*** generic "+t1)
        isstar=False
    
        if tt2 == "null" or tt2 == "[]": return t1
        tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
        cc=tt2.count(',')
        subs=""
        print("generic",tt2," cc= ",cc)
        if tt2.endswith("*"): isstar=True

        if cc==0 and ":log-stream:" in tt2:
            #print("log-stream")
            logr=tt2.split(':')[3]
            if logr==globals.region:
                logn=tt2.split(':log-stream:')[0].split(':')[-1]
                common.add_dependancy("aws_cloudwatch_log_group", logn)
                logn2=logn.replace("/", "_")
                streamn=tt2.split(':log-stream:')[1]
                if isstar: streamn=streamn.rstrip("*")
                #print(logn2, streamn, logr)
                if isstar:
                    period="."
                    arnadr="aws_cloudwatch_log_stream."+logn2+"_"+streamn+".arn"
                    print(arnadr)
                    t1=tt1 + ' = [format("%s*",'+arnadr+')]\n'
                    #t1=tt1 + ' = ["' + 'format("%s*",'+arnadr+')"]\n'
                
                else:
                    t1=tt1 + " = aws_cloudwatch_log_stream."+logn2+"_"+streamn+".arn\n" 

        if cc==0 and ":role/" in tt2 and "arn:aws:iam" in tt2:
            #print("log-stream")

            if "/aws_service_role" not in tt2:

                roln=tt2.split('/')[-1]
                if not roln.endswith("*"):
                    common.add_dependancy("aws_iam_role", roln)
                    arnadr="aws_iam_role."+roln+".arn"
                    print(arnadr)
                    t1=tt1 + ' = [format("%s*",'+arnadr+')]\n'
                


    except Exception as e:  
      common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)     
    print("generic out =", t1)
    return t1
    if cc == 0:
        tarn=tt2
        arn_list=tarn.split(':')[0:3] 
        arn_fragment=':'.join(arn_list)
        
        if arn_fragment in arn_dict: 
            subtype=arn_dict[arn_fragment]['subtype']
            if arn_dict[arn_fragment]['named']:
                subn=tt2.split('/')[-1]
                subs=subs + subtype+"." + subn + ".arn,"
            else:
                rarn=tarn.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_")
                subs=subs + subtype+"." + rarn + ".arn,"
            common.add_dependancy(subtype,tarn)





    if cc > 0:
        for i in range(cc+1):
            subn=tt2.split(',')[i]
            tarn=subn
            arn_list=tarn.split(':')[0:3]
            arn_fragment=':'.join(arn_list)

            if arn_fragment in arn_dict: 
                subtype=arn_dict[arn_fragment]['subtype']
                if arn_dict[arn_fragment]['named']:
                    subn=tt2.split('/')[-1]
                    subs=subs + subtype+"." + subn + ".arn,"
                else:
                    rarn=tarn.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_")
                    subs=subs + subtype+"." + rarn + ".arn,"
                common.add_dependancy(subtype,tarn)
                        
    if subs == "": return t1
    
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')

    print("exit t1="+t1)
    return t1



