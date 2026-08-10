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
        # Resource list dicts (populated by build_lists)
        self.vpclist = {}
        self.subnetlist = {}
        self.sglist = {}
        self.ltlist = {}
        self.lambdalist = {}
        self.s3list = {}
        self.rolelist = {}
        self.policylist = {}
        self.inplist = {}
        self.bucketlist = {}
        self.tgwlist = {}
        self.gluedbs = {}
        self.attached_role_policies_list = {}
        self.role_policies_list = {}
        self.igwlist = {}
        self.natgwlist = {}
        self.vpcpeerlist = {}
        self.enilist = {}
        self.loggrouplist = {}
        self.athenadatabaselist = {}
        self.eventrulelist = {}
        self.subnets = {}
        self.vpcs = {}
        # Processing state dicts
        self.rproc = {}
        self.rdep = {}
        self.trdep = {}
        # Accumulator lists (grow during a run, must be empty at start)
        self.processed = []
        self.dependancies = []
        self.types = []
        self.all_extypes = []
        self.badlist = []
        self.policies = []
        self.policyarns = []
        self.roles = []
        # Cached API responses (cleared between runs)
        self.aws_subnet_resp = []
        self.aws_route_table_resp = []
        self.aws_kms_alias_resp = []
        self.aws_vpc_resp = []
        self.aws_iam_role_resp = []
        self.aws_instance_resp = []
        # Transient processing flags (reset between runs)
        self.lbc = 0
        self.rbc = 0
        self.asg_azs = False
        self.plan2 = False
        self.lbskipaacl = False
        self.lbskipcnxl = False
        self.mskcfg = False
        self.repdbin = False
        self.gulejobmaxcap = False
        self.levsmap = False
        self.ec2ignore = False
        self.emrsubnetid = False
        self.expected = False
        self.serverless = False
        self.elastirep = False
        self.elastigrep = False
        self.elasticc = False
        self.kinesismsk = False
        self.destbuck = False
        self.iskmskey = False
        # Transient string state (reset between runs)
        self.ssmparamn = ""
        self.api_id = ""
        self.stripblock = ""
        self.stripstart = ""
        self.stripend = ""
        self.apigwrestapiid = ""
        self.secid = ""
        self.secvid = ""
        self.pathadd = ""
        self.meshname = ""
        self.workaround = ""
        self.current_tf = ""
        self.dzd = ""
        self.dzgid = ""
        self.dzpid = ""
        self.connectinid = ""
        self.waf2id = ""
        self.waf2nm = ""
        self.waf2sc = ""
        self.subnetid = ""


# Singleton instance — all access goes through this
_state = _State()


def reset():
    """Reset all managed state. Call between test runs or before a new import."""
    _state.reset()


# --- Module-level variables (not yet migrated to _State) ---

aws2tfver="v6532"
tfver="6.53.0"
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
## Lists below are managed by _State — accessed via module proxy
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
# policies, policyarns, roles, aws_*_resp, transient flags/strings — all migrated to _State

# Configuration set from CLI (not reset between runs)
ssoinstance=None
skipname=None
ec2tag=None
ec2tagv=None
ec2tagk=None
credtype="invalid"

## Dicts (now managed by _State)
# rproc, rdep, trdep — migrated to _State

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

# List Dicts — all migrated to _State, accessed via module proxy

def exit_aws2tf(mess):
    if mess is not None or mess!="":
        log.error(mess)

    if fast:
        sys.exit(1) 
    else:
        sys.exit(1)


# --- Module-level attribute routing for migrated state ---
# All attributes in _MANAGED_ATTRS are delegated to _state

_MANAGED_ATTRS = frozenset([
    # Resource list dicts
    'vpclist', 'subnetlist', 'sglist', 'ltlist', 'lambdalist', 's3list',
    'rolelist', 'policylist', 'inplist', 'bucketlist', 'tgwlist', 'gluedbs',
    'attached_role_policies_list', 'role_policies_list', 'igwlist', 'natgwlist',
    'vpcpeerlist', 'enilist', 'loggrouplist', 'athenadatabaselist', 'eventrulelist',
    'subnets', 'vpcs',
    # Processing state dicts
    'rproc', 'rdep', 'trdep',
    # Accumulator lists
    'processed', 'dependancies', 'types', 'all_extypes', 'badlist',
    'policies', 'policyarns', 'roles',
    # Cached API responses
    'aws_subnet_resp', 'aws_route_table_resp', 'aws_kms_alias_resp',
    'aws_vpc_resp', 'aws_iam_role_resp', 'aws_instance_resp',
    # Transient processing flags
    'lbc', 'rbc', 'asg_azs', 'plan2', 'lbskipaacl', 'lbskipcnxl', 'mskcfg',
    'repdbin', 'gulejobmaxcap', 'levsmap', 'ec2ignore', 'emrsubnetid',
    'expected', 'serverless', 'elastirep', 'elastigrep', 'elasticc',
    'kinesismsk', 'destbuck', 'iskmskey',
    # Transient strings
    'ssmparamn', 'api_id', 'stripblock', 'stripstart', 'stripend',
    'apigwrestapiid', 'secid', 'secvid', 'pathadd', 'meshname',
    'workaround', 'current_tf', 'dzd', 'dzgid', 'dzpid', 'connectinid',
    'waf2id', 'waf2nm', 'waf2sc', 'subnetid',
])


def __getattr__(name):
    if name in _MANAGED_ATTRS:
        return getattr(_state, name)
    raise AttributeError(f"module 'context' has no attribute {name!r}")


# To intercept `context.vpclist = {...}` we need the module to be its own class.
# Python 3.7+ supports module __getattr__ but NOT module __setattr__.
# So we use the sys.modules trick to make the module instance support setattr.

class _ModuleProxy(sys.modules[__name__].__class__):
    """Allow attribute assignment to route to _state for managed attributes."""
    def __setattr__(self, name, value):
        if name in _MANAGED_ATTRS:
            setattr(_state, name, value)
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in _MANAGED_ATTRS:
            return getattr(_state, name)
        raise AttributeError(f"module 'context' has no attribute {name!r}")


sys.modules[__name__].__class__ = _ModuleProxy
    



