import common
import context

def aws_networkmanager_attachment_accepter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_connect_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_connect_peer(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_connections(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_core_network(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_core_network_policy_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_core_network_policy_documument(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_customer_gateway_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_device(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="global_network_id" and tt2 !="null":
		t1=tt1+" = aws_networkmanager_global_network."+tt2+".id\n"
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [location]\n" +  "}\n"
	return skip,t1,flag1,flag2

def aws_networkmanager_devices(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_global_network(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_global_networks(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_link(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_link_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_links(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_site(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="global_network_id" and tt2 !="null":
		t1=tt1+" = aws_networkmanager_global_network."+tt2+".id\n"
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [location]\n" +  "}\n"


	return skip,t1,flag1,flag2

def aws_networkmanager_site_to_site_vpn_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_sites(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_transit_gateway_connect_peer_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_transit_gateway_peering(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_transit_gateway_registration(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="global_network_id" and tt2 !="null":
		t1=tt1+" = aws_networkmanager_global_network."+tt2+".id\n"
	elif tt1=="transit_gateway_arn" and tt2 !="null":
		if tt2.startswith("arn:"):
			tgid=tt2.split("/")[-1]
			if tgid in str(context.tgwlist.keys()):
				t1=tt1+" = aws_ec2_transit_gateway."+tgid+".arn\n"
				common.add_dependancy("aws_ec2_transit_gateway",tgid)
	return skip,t1,flag1,flag2

def aws_networkmanager_transit_gateway_route_table_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_networkmanager_vpc_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_oam_link(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_oam_sink(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_oam_sink_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

