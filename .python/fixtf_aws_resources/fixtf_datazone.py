import common
import globals

def aws_datazone_domain(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_project(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		globals.dzd=tt2
		common.add_dependancy("aws_datazone_domain",tt2)
	return skip,t1,flag1,flag2

def aws_datazone_glossary(t1,tt1,tt2,flag1,flag2):
	skip=0
	## workaround
	## 
	if tt1=="description" and tt2!="null":
		t1=tt1+" = \"changeme\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [description]\n}\n"
	return skip,t1,flag1,flag2

def aws_datazone_glossary_term(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_environment_blueprint_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_id" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)
	return skip,t1,flag1,flag2

def aws_datazone_environment_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)

	return skip,t1,flag1,flag2

def aws_datazone_environment(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		globals.dzd=tt2
		common.add_dependancy("aws_datazone_domain",tt2)

	if tt1=="project_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_project."+globals.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)


	return skip,t1,flag1,flag2

def aws_datazone_form_type(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2