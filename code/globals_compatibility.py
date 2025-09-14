#!/usr/bin/env python3
"""
Compatibility layer for globals.py during migration.

This module provides a compatibility interface that allows existing code
to continue working while the migration to ConfigurationManager is completed.
It acts as a bridge between the old global variable system and the new
configuration management system.
"""

import sys
import os
from typing import Dict, List, Any, Optional

# Import the new configuration system
from .config import ConfigurationManager

# Global configuration instance for compatibility
_global_config: Optional[ConfigurationManager] = None


def initialize_global_config(config: ConfigurationManager = None) -> ConfigurationManager:
    """
    Initialize the global configuration instance.
    
    Args:
        config: Optional ConfigurationManager instance to use.
        
    Returns:
        The global ConfigurationManager instance.
    """
    global _global_config
    if config is not None:
        _global_config = config
    elif _global_config is None:
        _global_config = ConfigurationManager()
    return _global_config


def get_global_config() -> ConfigurationManager:
    """
    Get the global configuration instance.
    
    Returns:
        The global ConfigurationManager instance.
    """
    global _global_config
    if _global_config is None:
        _global_config = ConfigurationManager()
    return _global_config


# Compatibility properties that map to ConfigurationManager
class GlobalsCompatibility:
    """
    Compatibility class that provides the same interface as the old globals module
    but uses ConfigurationManager internally.
    """
    
    @property
    def aws2tfver(self) -> str:
        return "v1010"
    
    @property
    def tfver(self) -> str:
        config = get_global_config()
        return config.aws.tf_version
    
    @tfver.setter
    def tfver(self, value: str):
        config = get_global_config()
        config.aws.tf_version = value
    
    @property
    def esttime(self) -> float:
        config = get_global_config()
        try:
            return config.processing.get_estimated_time()
        except AttributeError:
            return 120.0
    
    @esttime.setter
    def esttime(self, value: float):
        config = get_global_config()
        try:
            config.processing.set_estimated_time(value)
        except AttributeError:
            pass
    
    @property
    def profile(self) -> str:
        config = get_global_config()
        return config.aws.profile
    
    @profile.setter
    def profile(self, value: str):
        config = get_global_config()
        config.aws.profile = value
    
    @property
    def sso(self) -> bool:
        config = get_global_config()
        return config.aws.is_sso
    
    @sso.setter
    def sso(self, value: bool):
        config = get_global_config()
        config.aws.is_sso = value
    
    @property
    def merge(self) -> bool:
        config = get_global_config()
        return config.runtime.merge
    
    @merge.setter
    def merge(self, value: bool):
        config = get_global_config()
        config.runtime.merge = value
    
    @property
    def fast(self) -> bool:
        config = get_global_config()
        return config.runtime.fast
    
    @fast.setter
    def fast(self, value: bool):
        config = get_global_config()
        config.runtime.fast = value
    
    @property
    def apionly(self) -> bool:
        config = get_global_config()
        return config.runtime.apionly
    
    @apionly.setter
    def apionly(self, value: bool):
        config = get_global_config()
        config.runtime.apionly = value
    
    @property
    def tracking_message(self) -> str:
        config = get_global_config()
        return config.get_tracking_message()
    
    @tracking_message.setter
    def tracking_message(self, value: str):
        config = get_global_config()
        config.set_tracking_message(value)
    
    @property
    def cores(self) -> int:
        config = get_global_config()
        return config.get_cores()
    
    @cores.setter
    def cores(self, value: int):
        config = get_global_config()
        config.set_cores(value)
    
    @property
    def cwd(self) -> str:
        config = get_global_config()
        return config.runtime.cwd
    
    @cwd.setter
    def cwd(self, value: str):
        config = get_global_config()
        config.runtime.cwd = value
    
    @property
    def path1(self) -> str:
        config = get_global_config()
        return config.runtime.path1
    
    @path1.setter
    def path1(self, value: str):
        config = get_global_config()
        config.runtime.path1 = value
    
    @property
    def path2(self) -> str:
        config = get_global_config()
        return config.runtime.path2
    
    @path2.setter
    def path2(self, value: str):
        config = get_global_config()
        config.runtime.path2 = value
    
    @property
    def path3(self) -> str:
        config = get_global_config()
        return config.runtime.path3
    
    @path3.setter
    def path3(self, value: str):
        config = get_global_config()
        config.runtime.path3 = value
    
    @property
    def debug(self) -> bool:
        config = get_global_config()
        return config.is_debug_enabled()
    
    @debug.setter
    def debug(self, value: bool):
        config = get_global_config()
        config.debug.enabled = value
    
    @property
    def debug5(self) -> bool:
        config = get_global_config()
        return config.debug.enabled5
    
    @debug5.setter
    def debug5(self, value: bool):
        config = get_global_config()
        config.debug.enabled5 = value
    
    @property
    def validate(self) -> bool:
        config = get_global_config()
        return config.runtime.validate
    
    @validate.setter
    def validate(self, value: bool):
        config = get_global_config()
        config.runtime.validate = value
    
    @property
    def dnet(self) -> bool:
        config = get_global_config()
        return config.runtime.dnet
    
    @dnet.setter
    def dnet(self, value: bool):
        config = get_global_config()
        config.runtime.dnet = value
    
    @property
    def dkms(self) -> bool:
        config = get_global_config()
        return config.runtime.dkms
    
    @dkms.setter
    def dkms(self, value: bool):
        config = get_global_config()
        config.runtime.dkms = value
    
    @property
    def dkey(self) -> bool:
        config = get_global_config()
        return config.runtime.dkey
    
    @dkey.setter
    def dkey(self, value: bool):
        config = get_global_config()
        config.runtime.dkey = value
    
    @property
    def dsgs(self) -> bool:
        config = get_global_config()
        return config.runtime.dsgs
    
    @dsgs.setter
    def dsgs(self, value: bool):
        config = get_global_config()
        config.runtime.dsgs = value
    
    @property
    def acc(self) -> str:
        config = get_global_config()
        return config.aws.account_id
    
    @acc.setter
    def acc(self, value: str):
        config = get_global_config()
        config.aws.account_id = value
    
    @property
    def region(self) -> str:
        config = get_global_config()
        return config.aws.region
    
    @region.setter
    def region(self, value: str):
        config = get_global_config()
        config.aws.region = value
    
    @property
    def serverless(self) -> bool:
        config = get_global_config()
        return config.runtime.serverless
    
    @serverless.setter
    def serverless(self, value: bool):
        config = get_global_config()
        config.runtime.serverless = value
    
    @property
    def all_extypes(self) -> List[str]:
        config = get_global_config()
        return config.runtime.all_extypes
    
    @all_extypes.setter
    def all_extypes(self, value: List[str]):
        config = get_global_config()
        config.runtime.all_extypes = value
    
    # Dictionary properties
    @property
    def rproc(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_processed_resources()
        except AttributeError:
            # Fallback to empty dict if method doesn't exist
            return {}
    
    @rproc.setter
    def rproc(self, value: Dict[str, bool]):
        config = get_global_config()
        for key, val in value.items():
            if val:
                config.mark_resource_processed(key)
    
    @property
    def vpclist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_vpc_list()
        except AttributeError:
            return {}
    
    @property
    def subnetlist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_subnet_list()
        except AttributeError:
            return {}
    
    @property
    def sglist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_sg_list()
        except AttributeError:
            return {}
    
    @property
    def lambdalist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_lambda_list()
        except AttributeError:
            return {}
    
    @property
    def s3list(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_s3_list()
        except AttributeError:
            return {}
    
    @property
    def rolelist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_role_list()
        except AttributeError:
            return {}
    
    @property
    def policylist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_policy_list()
        except AttributeError:
            return {}
    
    @property
    def tgwlist(self) -> Dict[str, bool]:
        config = get_global_config()
        try:
            return config.resources.get_tgw_list()
        except AttributeError:
            return {}
    
    # Processing flags
    @property
    def elastirep(self) -> bool:
        config = get_global_config()
        try:
            return config.processing.get_processing_flag('elastirep')
        except AttributeError:
            return False
    
    @elastirep.setter
    def elastirep(self, value: bool):
        config = get_global_config()
        try:
            config.processing.set_processing_flag('elastirep', value)
        except AttributeError:
            pass
    
    @property
    def elastigrep(self) -> bool:
        config = get_global_config()
        try:
            return config.processing.get_processing_flag('elastigrep')
        except AttributeError:
            return False
    
    @elastigrep.setter
    def elastigrep(self, value: bool):
        config = get_global_config()
        try:
            config.processing.set_processing_flag('elastigrep', value)
        except AttributeError:
            pass
    
    @property
    def elasticc(self) -> bool:
        config = get_global_config()
        try:
            return config.processing.get_processing_flag('elasticc')
        except AttributeError:
            return False
    
    @elasticc.setter
    def elasticc(self, value: bool):
        config = get_global_config()
        try:
            config.processing.set_processing_flag('elasticc', value)
        except AttributeError:
            pass
    
    # Exit function
    def exit_aws2tf(self, mess: str = None):
        """
        Exit aws2tf with optional message.
        
        Args:
            mess: Optional exit message.
        """
        if mess is not None and mess != "":
            print(mess)
        
        config = get_global_config()
        if config.runtime.fast:
            os._exit(1)
        else:
            sys.exit(1)


# Create the compatibility instance
_compat = GlobalsCompatibility()

# Export all the properties as module-level variables for backward compatibility
aws2tfver = _compat.aws2tfver
tfver = _compat.tfver
esttime = _compat.esttime
profile = _compat.profile
sso = _compat.sso
merge = _compat.merge
fast = _compat.fast
apionly = _compat.apionly
tracking_message = _compat.tracking_message
cores = _compat.cores
cwd = _compat.cwd
path1 = _compat.path1
path2 = _compat.path2
path3 = _compat.path3
debug = _compat.debug
debug5 = _compat.debug5
validate = _compat.validate
dnet = _compat.dnet
dkms = _compat.dkms
dkey = _compat.dkey
dsgs = _compat.dsgs
acc = _compat.acc
region = _compat.region
serverless = _compat.serverless
all_extypes = _compat.all_extypes
rproc = _compat.rproc
vpclist = _compat.vpclist
subnetlist = _compat.subnetlist
sglist = _compat.sglist
lambdalist = _compat.lambdalist
s3list = _compat.s3list
rolelist = _compat.rolelist
policylist = _compat.policylist
tgwlist = _compat.tgwlist
elastirep = _compat.elastirep
elastigrep = _compat.elastigrep
elasticc = _compat.elasticc
exit_aws2tf = _compat.exit_aws2tf

# Additional compatibility variables
processed = []
dependancies = []
types = []
regionl = 0
policies = []
policyarns = []
roles = []
aws_subnet_resp = []
aws_route_table_resp = []
aws_kms_alias_resp = []
aws_vpc_resp = []
aws_iam_role_resp = []
aws_instance_resp = []
lbc = 0
rbc = 0
asg_azs = False
plan2 = False
lbskipaacl = False
lbskipcnxl = False
mskcfg = False
ssmparamn = ""
repdbin = False
gulejobmaxcap = False
levsmap = False
ec2ignore = False
api_id = ""
stripblock = ""
stripstart = ""
stripend = ""
apigwrestapiid = ""
ssoinstance = None
emrsubnetid = False
secid = ""
secvid = ""
pathadd = ""
meshname = ""
workaround = ""
expected = False
dzd = ""
dzgid = ""
dzpid = ""
connectinid = ""
waf2id = ""
waf2nm = ""
waf2sc = ""
ec2tag = None
ec2tagv = None
ec2tagk = None
subnetid = ""
credtype = "invalid"
kinesismsk = False
destbuck = False
badlist = []
rdep = {}
trdep = {}
mopup = {
    "aws_service_discovery_http_namespace": "ns-"
}
noimport = {
    "aws_iam_user_group_membership": True,
    "aws_iam_security_token_service_preferences": True,
    "aws_ebs_snapshot_copy": True,
    "aws_ebs_snapshot_import": True,
    "aws_vpclattice_target_group_attachment": True
}
tested = {}
subnets = {}
vpcs = {}
bucketlist = {}
gluedbs = {}
attached_role_policies_list = {}
role_policies_list = {}