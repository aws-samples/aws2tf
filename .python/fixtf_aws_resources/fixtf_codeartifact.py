import common
import globals

def aws_codeartifact_domain(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_codeartifact_domain_permissions_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_codeartifact_repository(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain" and tt2 != "null":
		t1=tt1+" = aws_codeartifact_domain."+tt2+".domain\n"
		common.add_dependancy("aws_codeartifact_domain",tt2)

	return skip,t1,flag1,flag2

def aws_codeartifact_repository_permissions_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

