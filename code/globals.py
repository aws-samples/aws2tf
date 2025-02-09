import sys,os

tfver="5.86.0"
esttime=120.0
profile="default"
merge=False
fast=False
apionly=False
tracking_message="aws2tf: Starting, update messages every 20 seconds"
cores=2
cwd=""
path1=""
path2=""
processed=[]
dependancies=[]
types=[]
debug=False
validate=False
dnet=False
dkms=False
dkey=False
acc="xxxxxxxxxxxx"
region="xx-xxxx-x"
regionl=0
policies=[]
policyarns=[]
roles=[]
aws_subnet_resp=[]
aws_route_table_resp=[]
aws_kms_alias_resp=[]
aws_vpc_resp=[]
aws_iam_role_resp=[]
aws_instance_resp=[]
lbc=0; rbc=0
asg_azs=False
plan2=False
lbskipaacl=False
lbskipcnxl=False
mskcfg=False
ssmparamn=""
repdbin=False
gulejobmaxcap=False
levsmap=False
ec2ignore=False
api_id=""
stripblock=""
stripstart=""
stripend=""
apigwrestapiid=""
ssoinstance=None
emrsubnetid=False
# secretsmanager secret version
secid=""
secvid=""

meshname=""
workaround=""
expected=False
all_extypes=[]
serverless=False
dzd=""
dzgid=""
dzpid=""
connectinid=""
waf2id=""
waf2nm=""
waf2sc=""
ec2tag=None
ec2tagv=None
ec2tagk=None

badlist=[]

## Dicts

rproc={}
rdep={}
trdep={}

# for common boto3
mopup={
    "aws_service_discovery_http_namespace":"ns-"
}

# these skip import - as they can't be imported - or no way to find with boto3
noimport={
    "aws_iam_user_group_membership": True,
    "aws_iam_security_token_service_preferences": True,
    "aws_ebs_snapshot_copy": True,
    "aws_ebs_snapshot_import": True,
    "aws_vpclattice_target_group_attachment": True
}

tested={
    
}

# List Dicts
subnets={}
subnetlist={}
sglist={}
vpclist={}
s3list={}
rolelist={}
policylist={}
bucketlist={}
tgwlist={}
gluedbs={}
attached_role_policies_list={}
role_policies_list={}

def exit_aws2tf(mess):
    if mess is not None or mess!="":
        print(mess)
    
    if globals.fast:
        os._exit(1) 
    else:
        sys.exit(1)
    



