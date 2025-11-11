#aws_bedrockagent_agent
def aws_bedrockagent_agent(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="skip_resource_in_use_check" and tt2=="null":
		t1 = tt1+" = false\n"
	elif tt1=="agent_name":
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [skip_resource_in_use_check]\n}\n"
	
	return skip,t1,flag1,flag2

def aws_bedrockagent_knowledge_base(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_bedrockagent_agent_knowledge_base_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="agent_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_agent.r-"+tt2+".id\n"
	elif tt1=="knowledge_base_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_knowledge_base.r-"+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_bedrockagent_data_source(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="knowledge_base_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_knowledge_base.r-"+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_bedrockagent_agent_action_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="skip_resource_in_use_check" and tt2=="null":
		skip=1
	#	t1 = tt1+" = false\n"
	if tt1=="agent_id":
		if tt2 != "null":
			t1 = tt1+" = aws_bedrockagent_agent.r-"+tt2+".id\n"
		#t1=t1+"skip_resource_in_use_check = false\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [skip_resource_in_use_check]\n}\n"
	return skip,t1,flag1,flag2

def aws_bedrockagent_agent_alias(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="agent_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_agent.r-"+tt2+".id\n"
	return skip,t1,flag1,flag2