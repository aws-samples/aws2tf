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
aws_kms_alias=[]
aws_vpc_resp=[]

plan2=False

specials=["aws_iam_role_policy","aws_route_table_association","aws_iam_policy","aws_iam_policy_attchment",
          "aws_eks_cluster","aws_eks_fagate_profile","aws_kms_key","aws_kms_alias",
          "aws_eks_identity_provider_config","aws_eks_addon","aws_vpc_ipv4_cidr_block_association"]

badlist=[]


## Dicts

rproc={}
rdep={}
trdep={}
