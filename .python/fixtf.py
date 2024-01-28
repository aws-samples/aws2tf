import globals
import os
import sys
import boto3
import base64
import resources
import common

from aws_resources import fixtf_accessanalyzer
from aws_resources import fixtf_acm
from aws_resources import fixtf_acm_pca
from aws_resources import fixtf_amp
from aws_resources import fixtf_amplify
from aws_resources import fixtf_apigateway
from aws_resources import fixtf_apigatewayv2
from aws_resources import fixtf_appconfig
from aws_resources import fixtf_appflow
from aws_resources import fixtf_appintegrations
from aws_resources import fixtf_application_autoscaling
from aws_resources import fixtf_application_insights
from aws_resources import fixtf_appmesh
from aws_resources import fixtf_apprunner
from aws_resources import fixtf_appstream
from aws_resources import fixtf_appsync
from aws_resources import fixtf_athena
from aws_resources import fixtf_auditmanager
from aws_resources import fixtf_autoscaling
from aws_resources import fixtf_autoscaling_plans
from aws_resources import fixtf_backup
from aws_resources import fixtf_batch
from aws_resources import fixtf_bedrock
from aws_resources import fixtf_billingconductor
from aws_resources import fixtf_budgets
from aws_resources import fixtf_ce
from aws_resources import fixtf_chime
from aws_resources import fixtf_chime_sdk_media_pipelines
from aws_resources import fixtf_chime_sdk_voice
from aws_resources import fixtf_cleanrooms
from aws_resources import fixtf_cloud9
from aws_resources import fixtf_cloudcontrol
from aws_resources import fixtf_cloudformation
from aws_resources import fixtf_cloudfront
from aws_resources import fixtf_cloudhsmv2
from aws_resources import fixtf_cloudsearch
from aws_resources import fixtf_cloudtrail
from aws_resources import fixtf_logs
from aws_resources import fixtf_codeartifact
from aws_resources import fixtf_codebuild
from aws_resources import fixtf_codecatalyst
from aws_resources import fixtf_codecommit
from aws_resources import fixtf_codedeploy
from aws_resources import fixtf_codeguru_reviewer
from aws_resources import fixtf_codeguruprofiler
from aws_resources import fixtf_codepipeline
from aws_resources import fixtf_codestar_connections
from aws_resources import fixtf_codestar_notifications
from aws_resources import fixtf_cognito_identity
from aws_resources import fixtf_cognito_idp
from aws_resources import fixtf_comprehend
from aws_resources import fixtf_config
from aws_resources import fixtf_connect
from aws_resources import fixtf_controltower
from aws_resources import fixtf_cur
from aws_resources import fixtf_customer_profiles
from aws_resources import fixtf_dataexchange
from aws_resources import fixtf_datapipeline
from aws_resources import fixtf_datasync
from aws_resources import fixtf_dax
from aws_resources import fixtf_detective
from aws_resources import fixtf_devicefarm
from aws_resources import fixtf_directconnect
from aws_resources import fixtf_dlm
from aws_resources import fixtf_dms
from aws_resources import fixtf_docdb
from aws_resources import fixtf_docdb_elastic
from aws_resources import fixtf_ds
from aws_resources import fixtf_dynamodb
from aws_resources import fixtf_ebs
from aws_resources import fixtf_ec2
from aws_resources import fixtf_ecr
from aws_resources import fixtf_ecs
from aws_resources import fixtf_efs
from aws_resources import fixtf_eks
from aws_resources import fixtf_elasticache
from aws_resources import fixtf_elasticbeanstalk
from aws_resources import fixtf_elastictranscoder
from aws_resources import fixtf_elb
from aws_resources import fixtf_elbv2
from aws_resources import fixtf_emr
from aws_resources import fixtf_emr_containers
from aws_resources import fixtf_emrserverless
from aws_resources import fixtf_es
from aws_resources import fixtf_events
from aws_resources import fixtf_evidently
from aws_resources import fixtf_finspace
from aws_resources import fixtf_firehose
from aws_resources import fixtf_fis
from aws_resources import fixtf_fms
from aws_resources import fixtf_fsx
from aws_resources import fixtf_gamelift
from aws_resources import fixtf_glacier
from aws_resources import fixtf_globalaccelerator
from aws_resources import fixtf_glue
from aws_resources import fixtf_grafana
from aws_resources import fixtf_guardduty
from aws_resources import fixtf_iam
from aws_resources import fixtf_identitystore
from aws_resources import fixtf_imagebuilder
from aws_resources import fixtf_inspector
from aws_resources import fixtf_inspector2
from aws_resources import fixtf_internetmonitor
from aws_resources import fixtf_iot
from aws_resources import fixtf_ivs
from aws_resources import fixtf_ivschat
from aws_resources import fixtf_kafka
from aws_resources import fixtf_kafkaconnect
from aws_resources import fixtf_kendra
from aws_resources import fixtf_keyspaces
from aws_resources import fixtf_kinesis
from aws_resources import fixtf_kinesisanalytics
from aws_resources import fixtf_kinesisanalyticsv2
from aws_resources import fixtf_kinesisvideo
from aws_resources import fixtf_kms
from aws_resources import fixtf_lakeformation
from aws_resources import fixtf_lambda
from aws_resources import fixtf_lex
from aws_resources import fixtf_lexv2_models
from aws_resources import fixtf_license_manager
from aws_resources import fixtf_lightsail
from aws_resources import fixtf_location
from aws_resources import fixtf_macie2
from aws_resources import fixtf_mediaconvert
from aws_resources import fixtf_medialive
from aws_resources import fixtf_mediapackage
from aws_resources import fixtf_mediastore
from aws_resources import fixtf_memorydb
from aws_resources import fixtf_mq
from aws_resources import fixtf_mwaa
from aws_resources import fixtf_neptune
from aws_resources import fixtf_network_firewall
from aws_resources import fixtf_networkmanager
from aws_resources import fixtf_opensearch
from aws_resources import fixtf_opsworks
from aws_resources import fixtf_organizations
from aws_resources import fixtf_outposts
from aws_resources import fixtf_pinpoint
from aws_resources import fixtf_pipes
from aws_resources import fixtf_polly
from aws_resources import fixtf_pricing
from aws_resources import fixtf_qldb
from aws_resources import fixtf_quicksight
from aws_resources import fixtf_ram
from aws_resources import fixtf_rds
from aws_resources import fixtf_redshift
from aws_resources import fixtf_redshift_data
from aws_resources import fixtf_redshift_serverless
from aws_resources import fixtf_resource_explorer_2
from aws_resources import fixtf_resource_groups
from aws_resources import fixtf_resourcegroupstaggingapi
from aws_resources import fixtf_rolesanywhere
from aws_resources import fixtf_route53
from aws_resources import fixtf_route53_recovery_control_config
from aws_resources import fixtf_route53_recovery_readiness
from aws_resources import fixtf_route53domains
from aws_resources import fixtf_route53resolver
from aws_resources import fixtf_rum
from aws_resources import fixtf_s3
from aws_resources import fixtf_s3control
from aws_resources import fixtf_s3outposts
from aws_resources import fixtf_sagemaker
from aws_resources import fixtf_scheduler
from aws_resources import fixtf_schemas
from aws_resources import fixtf_secretsmanager
from aws_resources import fixtf_securityhub
from aws_resources import fixtf_securitylake
from aws_resources import fixtf_serverlessrepo
from aws_resources import fixtf_servicecatalog
from aws_resources import fixtf_servicediscovery
from aws_resources import fixtf_servicequotas
from aws_resources import fixtf_ses
from aws_resources import fixtf_sesv2
from aws_resources import fixtf_shield
from aws_resources import fixtf_signer
from aws_resources import fixtf_simpledb
from aws_resources import fixtf_sns
from aws_resources import fixtf_sqs
from aws_resources import fixtf_ssm
from aws_resources import fixtf_ssm_contacts
from aws_resources import fixtf_ssm_incidents
from aws_resources import fixtf_sso_admin
from aws_resources import fixtf_stepfunctions
from aws_resources import fixtf_storagegateway
from aws_resources import fixtf_sts
from aws_resources import fixtf_swf
from aws_resources import fixtf_synthetics
from aws_resources import fixtf_timestreamwrite
from aws_resources import fixtf_transcribe
from aws_resources import fixtf_transfer
from aws_resources import fixtf_vpc_lattice
from aws_resources import fixtf_waf
from aws_resources import fixtf_waf_regional
from aws_resources import fixtf_wafv2
from aws_resources import fixtf_worklink
from aws_resources import fixtf_workspaces
from aws_resources import fixtf_xray


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
                tt2=t1.split("=")[1].strip()
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
            ends=ends+",data.aws_caller_identity.current.account_id"
         
            t1 = tt1+" = format("+tt2+ends+")\n"
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
    tt2=tt2.strip('\"')
    if ":role" in tt2:
        tt2=tt2.split('/')[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)
    return t1

def deref_kms_key(t1,tt1,tt2):
    print("deref_kms_key 1: " + tt2)
    if "arn:aws:kms:" in tt2:
        #tt2=tt2.split('/')[-1]
        #tt2=tt2.strip('\"')
        print("deref_kms_key 2: " + tt2)
        t1=globals_replace(t1,tt1,tt2)
        #t1=tt1 + " = aws_kms_key.k-" + tt2 + ".arn\n"
        #add_dependancy("aws_kms_key",tt2)
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



