cwd=""
path1=""
path2=""
processed=[]
dependancies=[]
types=[]
debug=False
validate=False
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
ssmparamn=""
repdbin=False
gulejobmaxcap=False
levsmap=False
api_id=""
stripblock=""
stripstart=""
stripend=""

meshname=""


#specials=["aws_iam_role_policy","aws_route_table_association","aws_iam_policy","aws_iam_policy_attchment",
#          "aws_eks_cluster","aws_eks_fagate_profile","aws_kms_key","aws_kms_alias",
#          "aws_eks_identity_provider_config","aws_eks_addon","aws_vpc_ipv4_cidr_block_association",
#          "aws_vpclattice_service_network_vpc_association","aws_vpclattice_service_network_service_association",
#          "aws_vpclattice_service","aws_vpclattice_listener","aws_vpclattice_listener_rule","aws_vpclattice_auth_policy"]

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
