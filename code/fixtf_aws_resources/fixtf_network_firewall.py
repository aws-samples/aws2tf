import common
def aws_networkfirewall_firewall(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="firewall_policy_arn":
		if tt2!="null" and tt2.startswith("arn:"):
			tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
			t1=tt1 + " = aws_networkfirewall_firewall_policy." + tarn + ".arn\n"
			common.add_dependancy("aws_networkfirewall_firewall_policy", tt2)
	return skip,t1,flag1,flag2

def aws_networkfirewall_firewall_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="priority" and tt2=="0": skip=1
	elif tt1=="resource_arn" and tt2!="null" and tt2.startswith("arn:"):
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1 + " = aws_networkfirewall_rule_group." + tarn + ".arn\n"
		common.add_dependancy("aws_networkfirewall_rule_group", tt2)
	return skip,t1,flag1,flag2

def aws_networkfirewall_logging_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="firewall_arn" and tt2!="null" and tt2.startswith("arn:"):
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1 + " = aws_networkfirewall_firewall." + tarn + ".arn\n"
		common.add_dependancy("aws_networkfirewall_firewall", tt2)

	elif tt1==" tls_inspection_configuration_arn" and tt2!="null" and tt2.startswith("arn:"):
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1 + " = aws_networkfirewall_tls_inspection_configuration." + tarn + ".arn\n"
		common.add_dependancy("aws_networkfirewall_tls_inspection_configuration", tt2)
	return skip,t1,flag1,flag2

def aws_networkfirewall_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkfirewall_rule_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

