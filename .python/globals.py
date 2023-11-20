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
plan2=False

specials=["aws_iam_role_policy","aws_route_table_association","aws_iam_policy","aws_iam_policy_attchment","aws_eks_cluster","aws_eks_fagate_profile"]

## Dicts

rproc={}
rdep={}
trdep={}
