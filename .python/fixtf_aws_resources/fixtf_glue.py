import globals 
import common

def aws_glue_crawler(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "database_name" and tt2 != "null":
		t1 = tt1 + " = aws_glue_catalog_database.d-"+globals.acc+"__"+tt2+".name\n"
		#common.add_dependancy("aws_glue_catalog_database",tt2)

	elif tt1 == "sample_size":
		if tt2 == "0": skip=1
	elif tt1 == "security_configuration" and tt2 != "null":
		t1 = tt1 + " = aws_glue_security_configuration."+tt2+".id\n"
		common.add_dependancy("aws_glue_security_configuration",tt2)
	return skip,t1,flag1,flag2

def aws_glue_catalog_database(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_catalog_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "database_name" and tt2 != "null":
		t1 = tt1 + " = aws_glue_catalog_database.d-"+globals.acc+"__"+tt2+".name\n"
		common.add_dependancy("aws_glue_catalog_database",tt2)
		pkey="aws_glue_catalog_database."+tt2
		globals.rproc[pkey]=True
	return skip,t1,flag1,flag2

def aws_glue_classifier(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_glue_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="connection_properties":
		t1=t1+"\n lifecycle {\n   ignore_changes = [connection_properties]\n}\n"
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
	#print("aws_glue_job t1=",t1)
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
		common.add_dependancy("aws_glue_security_configuration", tt2)
	if "--output_s3_bucket_name" in tt1:
		t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
		common.add_dependancy("aws_s3_bucket",tt2)
	
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

