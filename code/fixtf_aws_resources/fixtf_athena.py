import common
import context
import logging
log = logging.getLogger('aws2tf')

def aws_athena_data_catalog(t1,tt1,tt2,flag1,flag2):
	skip=0
	
	return skip,t1,flag1,flag2

def aws_athena_database(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_athena_named_query(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "database" and tt2 != "null":
		if "-" not in tt2:
			t1 = tt1 + " = aws_athena_database." + tt2 + ".name\n"
			common.add_dependancy("aws_athena_database", tt2)
		else:
			log.warning("WARNING: aws_athena_named_query database name has a dash in it %s",  tt2)
	elif tt1 == "workgroup" and tt2 != "null":
		t1 = tt1 + " = aws_athena_workgroup." + tt2 + ".name\n"
		common.add_dependancy("aws_athena_workgroup", tt2)
		

	return skip,t1,flag1,flag2

def aws_athena_prepared_statement(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_athena_workgroup(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

