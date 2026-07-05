import sys,os
import logging

log = logging.getLogger('aws2tf')


class _State:
    """
    Encapsulates mutable application state that needs to be reset between runs/tests.
    
    Attributes managed here can be reset cleanly via reset(). Over time, more module-level
    variables will migrate into this class.
    """
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all managed state to initial values."""
        self.vpclist = {}


# Singleton instance — all access goes through this
_state = _State()


def reset():
    """Reset all managed state. Call between test runs or before a new import."""
    _state.reset()


# --- Module-level variables (not yet migrated to _State) ---

aws2tfver="v6273"
tfver="6.27.0"
esttime=120.0
profile="default"
sso=False
merge=False
fast=False
apionly=False
tracking_message="aws2tf: Starting, update messages every 20 seconds"
cores=2
cwd=""
path1=""
path2=""
path3=""
processed=[]
dependancies=[]
types=[]
debug=False
debug5=False
validate=False
warnings=False
show_status=False  # Show STATUS messages (controlled by --status flag)
dnet=False
dkms=False
dkey=False
dsgs=False
acc="xxxxxxxxxxxx"
region="xx-xxxx-x"
regionl=0

# Adaptive progress tracking
terraform_plan_rate = 25.0  # Initial estimate: resources per second
terraform_plan_samples = 0  # Number of samples collected
terraform_apply_rate = 50.0  # Initial estimate: resources per second for apply
terraform_apply_samples = 0  # Number of apply samples collected
last_plan_time = 0.0  # Time taken for last terraform plan (for post-import estimate)
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
pathadd=""

meshname=""
workaround=""
expected=False
all_extypes=[]
skipname=None
current_tf=""
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
subnetid=""
credtype="invalid"
elastirep=False
elastigrep=False
elasticc=False
kinesismsk=False
destbuck=False
iskmskey=False

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

# List Dicts (migrating to _State over time)
subnets={}
vpcs={}
subnetlist={}
loggrouplist={}
athenadatabaselist={}
eventrulelist={}
sglist={}
# vpclist is now managed by _State — accessed via module __getattr__/__setattr__
igwlist={}
natgwlist={}
vpcpeerlist={}
enilist={}
ltlist={}
lambdalist={}
s3list={}
rolelist={}
policylist={}
inplist={}
bucketlist={}
tgwlist={}
gluedbs={}
attached_role_policies_list={}
role_policies_list={}

def exit_aws2tf(mess):
    if mess is not None or mess!="":
        log.error(mess)

    if fast:
        sys.exit(1) 
    else:
        sys.exit(1)


# --- Module-level attribute routing for migrated state ---
# This makes `context.vpclist` transparently delegate to `_state.vpclist`

def __getattr__(name):
    if name == 'vpclist':
        return _state.vpclist
    raise AttributeError(f"module 'context' has no attribute {name!r}")


# To intercept `context.vpclist = {...}` we need the module to be its own class.
# Python 3.7+ supports module __getattr__ but NOT module __setattr__.
# So we use the sys.modules trick to make the module instance support setattr.

class _ModuleProxy(sys.modules[__name__].__class__):
    """Allow attribute assignment to route to _state for managed attributes."""
    def __setattr__(self, name, value):
        if name == 'vpclist':
            _state.vpclist = value
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == 'vpclist':
            return _state.vpclist
        raise AttributeError(f"module 'context' has no attribute {name!r}")


sys.modules[__name__].__class__ = _ModuleProxy
    



