import common

def aws_service_discovery_http_namespace(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_service_discovery_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_service_discovery_private_dns_namespace(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_service_discovery_public_dns_namespace(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_service_discovery_service(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="type" and tt2=="DNS_HTTP": skip=1
	elif tt1=="namespace_id":
		if tt2.startswith("ns-"):
			t1=tt1+" = aws_service_discovery_private_dns_namespace."+tt2+".id\n"
			common.add_dependancy("aws_service_discovery_private_dns_namespace",tt2)
		
	return skip,t1,flag1,flag2

