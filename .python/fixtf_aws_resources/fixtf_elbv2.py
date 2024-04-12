import globals
import common

def aws_lb_cookie_stickiness_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb_hosted_zone_id(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb_listener(t1,tt1,tt2,flag1,flag2):
	skip=0

	if "load_balancer_arn" == tt1:
		tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
		t1 = tt1 + " = aws_lb."+tt2+".arn\n"
		#t1=t1+"\n lifecycle {\n   ignore_changes = [default_action[0].forward[0]]\n}\n"

	if "order" == tt1:
		if tt2 == "0": skip=1
	elif "duration" == tt1:
		if tt2 == "0": t1=tt1+" = 1\n"	
	#elif "target_group_arn" == tt1: 
	#	tgarn=tt2
	#	tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
	#	t1 = tt1 + " = aws_lb_target_group."+tt2+".arn\n"
	#	common.add_dependancy("aws_lb_target_group",tgarn)

	return skip,t1,flag1,flag2


def aws_lb_listener_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb_listener_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	#if "listener_arn" == tt1:
	#	t1=t1+ "\nlifecycle {\n" + "   ignore_changes = [action[0].target_group_arn,action[0].forward[0].stickiness[0].duration]\n" +  "}\n"
	if "order" == tt1:
		if tt2 == "0": skip=1
	elif "duration" == tt1:
		if tt2 == "0": 
			t1=tt1+" = 1\n"
	#elif "target_group_arn" == tt1: 
#		tgarn=tt2
#		tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
#		t1 = tt1 + " = aws_lb_target_group."+tt2+".arn\n"
#		common.add_dependancy("aws_lb_target_group",tgarn)
	#elif "arn" == tt1: skip=1
			
	#elif "target_group_arn" == tt1: skip=1




	return skip,t1,flag1,flag2

def aws_lb_ssl_negotiation_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb_target_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "on_deregistration" in tt1:
		if tt2 == "null": t1=tt1+" = \"no_rebalance\"\n"
	if "on_unhealthy" in tt1:
		if tt2 == "null": 
			t1=tt1+" = \"no_rebalance\"\n" #+\n lifecycle {\n   ignore_changes = [on_deregistration,on_unhealthy,enable_unhealthy_connection_termination]\n}\n"

	if "enable_unhealthy_connection_termination" in tt1:
		if tt2 == "null": t1=tt1+" = true\n"

	if "name" == tt1:
		t1=t1+"\n lifecycle {\n   ignore_changes = [target_failover[0].on_deregistration,target_failover[0].on_unhealthy,target_health_state[0].enable_unhealthy_connection_termination]\n}\n"


	return skip,t1,flag1,flag2

def aws_lb_target_group_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb_trust_store(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb_trust_store_revocation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lb(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_load_balancer_backend_server_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_load_balancer_listener_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_load_balancer_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

