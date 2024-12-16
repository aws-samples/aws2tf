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
	if tt1=="domain_identifier" and tt2!="null":
		globals.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
	#elif tt1=="glossary_identifier" and tt2!="null":
	#	t1=tt1+" = aws_datazone_glossary."+globals.dzd+"_"+tt2+".id\n"
	#	common.add_dependancy("aws_datazone_glossary", tt2)
	return skip,t1,flag1,flag2

def aws_datazone_environment_blueprint_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_id" and tt2!="null":
		globals.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)

	return skip,t1,flag1,flag2

def aws_datazone_environment_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		globals.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)


	elif tt1=="project_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_project."+globals.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)
	elif tt1=="environment_blueprint_identifier":	
		t1=tt1+" = aws_datazone_environment_blueprint_configuration."+globals.dzd+"_"+tt2+".environment_blueprint_id\n"


	return skip,t1,flag1,flag2

def aws_datazone_environment(t1,tt1,tt2,flag1,flag2):
	skip=0
	
	if "resource" in t1 and "{" in t1 and "aws_datazone_environment" in t1:
		did="dzd_"+t1.split("dzd_")[1].split("_")[0]
		globals.dzd=did
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		globals.dzd=tt2
		common.add_dependancy("aws_datazone_domain",tt2)

	elif tt1=="profile_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_environment_profile."+globals.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)

	elif tt1=="project_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_project."+globals.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)
	elif tt1=="blueprint_identifier":
		t1=tt1+" = aws_datazone_environment_blueprint_configuration."+globals.dzd+"_"+tt2+".environment_blueprint_id\n"

	return skip,t1,flag1,flag2

def aws_datazone_form_type(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_datazone_user_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_datazone_asset_type(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2