import globals
import os
import sys
import boto3
import base64
import resources
import common

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
    if globals.debug:
        print(ttft+" fixtf "+tf+".out") 
   
    try:
        f1 = open(rf, 'r')
    except:
        print("no "+rf)
        return
    
    clfn, descfn, topkey, key, filterid = resources.resource_data(ttft, None)
    if clfn is None:
        print("ERROR: clfn is None with type="+ttft)
        exit()

    clfn=clfn.replace('-','_')
    callfn="fixtf_"+clfn
    if globals.debug: print("callfn="+callfn+" ttft="+ttft)
    globals.lbc=0
    Lines = f1.readlines()
    #print("getfn for fixtf2."+ttft+" "+tf2)
    #with open(tf2, "a") as f2:
    with open(tf2, "w") as f2:
        skip=0
        flag1=False
        flag2=tf
        nofind=0
        f2.write("##START,"+ttft+"\n")
        for t1 in Lines:
            skip=0
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip().strip('\"')
            except:
                tt2=""
 
            try:    
                #print("trying "+callfn+" "+ttft)
                getfn = getattr(eval(callfn), ttft)           
                #getfn = getattr(fixtf2, ttft)
            except Exception as e:
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print("** no fixtf2 for "+ttft+" calling generic fixtf2.aws_resource")
                #print("t1="+t1) 
                nofind=1
                
          
            try:
                skip,t1,flag1,flag2=getfn(t1,tt1,tt2,flag1,flag2)
            except Exception as e:
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

                print("-- no fixtf for "+tf+" calling generic fixtf2.aws_resource callfn="+callfn)
                #print("t1="+t1) 
                nofind=2
                skip,t1,flag1,flag2=aws_resource(t1,tt1,tt2,flag1,flag2)

            ####
            
            # common replacement code here
            # rhs=account number
            # rhs is still an arn
            # : in tt1 for quote it
                
            #### 

            if skip == 0:
                f2.write(t1)
        if nofind > 0:
           print("WARNING: No fixtf for "+tf+" calling generic fixtf2.aws_resource nofind="+str(nofind))
           

def aws_resource(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 

def globals_replace(t1,tt1,tt2):
    #print("policy " + globals.acc + " "+ tt2)
    ends=""
    while ":"+globals.acc+":" in tt2:
            #print("--> 5")
            r1=tt2.find(":"+globals.region+":")
            a1=tt2.find(":"+globals.acc+":")
            #print("--> r1="+ str(r1) + " ")
            #print("--> a1="+ str(a1) + " ")
            if r1>0 and r1 < a1:
                    #print("--> 6a")
                    ends=ends+",data.aws_region.current.name"
                    tt2=tt2[:r1]+":%s:"+tt2[r1+globals.regionl+2:]

            a1=tt2.find(":"+globals.acc+":")
            tt2=tt2[:a1]+":%s:"+tt2[a1+14:]
            ends=ends+'",data.aws_caller_identity.current.account_id'
         
            t1 = tt1+' = format("'+tt2+ends+')\n'
    if tt1 == "managed_policy_arns":
        tt2=tt2.replace('[','')
        tt2=tt2.replace(']','')
        tt2=tt2.replace('"','')
        t1 = tt1+' = [format("'+tt2+'"'+ends+')]\n'
    return t1


def deref_array(t1,tt1,tt2,ttft,prefix,skip):
    if tt2 == "null" or tt2 == "[]":
        skip=1
        return t1,skip
    tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
    cc=tt2.count(',')
    subs=""
    if globals.debug: 
        print("-->> " + tt1 + ": "  + tt2 + " count=" + str(cc))
    if cc > 0:
        for i in range(cc+1):
            subn=tt2.split(',')[i]
            subs=subs + ttft + "." + subn + ".id,"
            common.add_dependancy(ttft,subn)

            
    if cc == 0 and prefix in tt2: 
        subs=subs + ttft + "." + tt2 + ".id,"
        common.add_dependancy(ttft,tt2)
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')
    return t1,skip

def deref_role_arn(t1,tt1,tt2):
    ##tt2=tt2.strip('\"')
    if ":role" in tt2:
        tt2=tt2.split('/')[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)
    return t1

def deref_kms_key(t1,tt1,tt2):
    print("deref_kms_key 1: " + tt2)
    if "arn:aws:kms:" in tt2:
        print("deref_kms_key 2: " + tt2)
        t1=globals_replace(t1,tt1,tt2)
    return t1



 #if tt1 == "security_groups": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
def deref_role_arn_array(t1,tt1,tt2):
    if tt2 == "null" or tt2 == "[]": return t1
    tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
    cc=tt2.count(',')
    subs=""
    if cc > 0:
        for i in range(cc+1):
            subn=tt2.split(',')[i]
            subn=subn.strip('/')[-1]
            subs=subs + "aws_iam_role." + subn + ".arn,"
            common.add_dependancy("aws_iam_role",subn)

            
    if cc == 0:
        tt2=tt2.split('/')[-1]
        subs=subs + "aws_iam_role." + tt2 + ".arn,"
        common.add_dependancy("aws_iam_role",tt2)
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')

    return t1



