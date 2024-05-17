def aws_servicecatalog_budget_resource_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_constraint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_launch_paths(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_organizations_access(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_portfolio(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_portfolio_constraints(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_portfolio_share(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_principal_portfolio_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_product(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="accept_language" and tt2=="null": 
		t1 = tt1 + " = \"en\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [accept_language]\n}\n"
	return skip,t1,flag1,flag2

def aws_servicecatalog_product_portfolio_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_provisioned_product(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_provisioning_artifact(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_provisioning_artifacts(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_service_action(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_tag_option(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_servicecatalog_tag_option_resource_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

