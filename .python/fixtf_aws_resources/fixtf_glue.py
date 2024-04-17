import globals 

def aws_glue_crawler(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "database_name" and tt2 != "null":
		t1 = tt1 + " = aws_glue_catalog_database."+tt2+".id\n"
	elif tt1 == "sample_size":
		if tt2 == "0": skip=1
	elif tt1 == "security_configuration" and tt2 != "null":
		t1 = tt1 + " = aws_glue_security_configuration."+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_glue_catalog_database(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2


def aws_glue_catalog_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "database_name" and tt2 != "null":
		t1 = tt1 + " = aws_glue_catalog_database."+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_glue_classifier(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_data_catalog_encryption_settings(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_data_quality_ruleset(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_dev_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_job(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "max_capacity" and tt2 != "null":
		globals.gulejobmaxcap=True
	if tt1 == "number_of_workers":
		if globals.gulejobmaxcap: skip=1
	if tt1 == "worker_type":
		if globals.gulejobmaxcap: skip=1
	if tt1 == "description":
		t1=t1+"\n lifecycle {\n   ignore_changes = [glue_version,number_of_workers,worker_type]\n}\n"
	if tt1 == "security_configuration" and tt2 != "null":
		t1 = tt1 + " = aws_glue_security_configuration."+tt2+".id\n"
	
	return skip,t1,flag1,flag2

def aws_glue_ml_transform(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_partition(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_partition_index(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_registry(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_schema(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_script(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_security_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_trigger(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "timeout": 
		if tt2 == "0": skip=1
	
	return skip,t1,flag1,flag2

def aws_glue_user_defined_function(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_workflow(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

