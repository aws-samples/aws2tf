import common
import fixtf
import base64
import boto3
import globals
import inspect
import json

def aws_ami(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ami_copy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ami_from_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ami_launch_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_customer_gateway(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_default_tags(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_default_subnet(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_default_vpc_dhcp_options(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ebs_encryption_by_default(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ebs_volume(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "throughput" in tt1:
		
		if tt2 == "0": skip=1
	return skip,t1,flag1,flag2

def aws_ec2_availability_zone_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_capacity_reservation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_carrier_gateway(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_client_vpn_authorization_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_client_vpn_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_client_vpn_network_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_client_vpn_route(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_coip_pool(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_default_security_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "name":
		if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    ##if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
	# fix via ingress /egress rules - ?
	elif tt1 == "egress" or globals.lbc > 0 :
            
		if tt2 == "[]": skip = 1
		if "[" in t1: globals.lbc=globals.lbc+1
		if "]" in t1: globals.lbc=globals.lbc-1
        #print("***t1="+t1+" lbc="+str(globals.lbc))
	
		if globals.lbc > 0: skip = 1
		if globals.lbc == 0:
           #print("***t1="+t1+" lbc="+str(globals.lbc))
			if "]" in t1.strip(): skip=1

	elif tt1 == "ingress" or globals.lbc > 0 :
    
		if tt2 == "[]": skip = 1
		if "[" in t1: globals.lbc=globals.lbc+1
		if "]" in t1: globals.lbc=globals.lbc-1
        #print("***t1="+t1+" lbc="+str(globals.lbc))
	
		if globals.lbc > 0: skip = 1
		if globals.lbc == 0:
           #print("***t1="+t1+" lbc="+str(globals.lbc))
			if "]" in t1.strip(): skip=1

	elif tt1 == "name_prefix" and flag1 is True: skip=1
	
	return skip,t1,flag1,flag2

def aws_ec2_fleet(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_host(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_image_block_public_access(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_instance_connect_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_instance_state(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_local_gateway_route(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_local_gateway_route_table_vpc_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_managed_prefix_list(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "max_entries":
			
			if tt2 == "0": skip=1
	return skip,t1,flag1,flag2

def aws_ec2_managed_prefix_list_entry(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_managed_prefix_lists(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_subnet_cidr_reservation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_tag(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_traffic_mirror_filter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_traffic_mirror_filter_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_traffic_mirror_session(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_traffic_mirror_target(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_attachments(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_connect(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_connect_peer(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_dx_gateway_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_multicast_domain(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_multicast_domain_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_multicast_group_member(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_multicast_group_source(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_peering_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "peer_account_id":
		if globals.acc in tt2: flag1=True
	if tt1=="peer_transit_gateway_id" and tt2 != "null":
		print(str(flag1))
		if flag1:
			t1=tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
			common.add_dependancy("aws_ec2_transit_gateway", tt2)
	if tt1=="transit_gateway_id" and tt2!="null":
		if flag1==True:
			t1=tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
			common.add_dependancy("aws_ec2_transit_gateway", tt2)
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_peering_attachment_accepter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_policy_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_policy_table_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_prefix_list_reference(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_route(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="transit_gateway_route_table_id" and tt2!="null":
			t1=tt1 + " = aws_ec2_transit_gateway_route_table." + tt2 + ".id\n"
			common.add_dependancy("aws_ec2_transit_gateway_route_table", tt2)
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_route_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="transit_gateway_id" and tt2!="null":
			t1=tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
			common.add_dependancy("aws_ec2_transit_gateway", tt2)
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_route_table_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_route_table_propropagation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_vpc_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="transit_gateway_id" and tt2!="null":
			t1=tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
			common.add_dependancy("aws_ec2_transit_gateway", tt2)
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_vpc_attachment_accepter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_vpc_attachments(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ec2_transit_gateway_vpn_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_egress_only_internet_gateway(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_eip(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "network_interface": skip = 1
	if tt1 == "instance" and tt2 != "null":
		t1 = tt1 + " = aws_instance."+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_eip_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "instance_id":
		if tt2 == "null": skip=1
		t1 = tt1 + " = aws_instance."+tt2+".id\n"
	elif tt1 == "public_ip": skip=1
	elif tt1 == "private_ip_address": skip=1
	elif tt1 == "network_interface_id": skip=1
	elif tt1 == "allocation_id": 
		t1=tt1 + " = aws_eip." + tt2 + ".id\n"
		common.add_dependancy("aws_eip",tt2)


	return skip,t1,flag1,flag2

def aws_flow_log(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


def aws_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	
	try:
		if tt1 == "ipv6_addresses":	
			if tt2 == "[]": skip=1

		elif tt1=="id":
			flag2=id
			if tt2.startswith("lt-"):
				t1 = tt1 +" = aws_launch_template."+tt2+".id\n"
				common.add_dependancy("aws_launch_template",tt2)
			flag1=True


		elif tt1=="name":
			if flag1:
				skip=1
				flag1=False

		elif tt1 == "user_data":
			inid=flag2.split("__")[1]
			session = boto3.Session(region_name=globals.region,profile_name=globals.profile)
			client = session.client("ec2")
			resp = client.describe_instance_attribute(Attribute="userData",InstanceId=inid)
			try:
				ud=resp['UserData']['Value']
				ud2=base64.b64decode(ud).decode('utf-8')
				with open(flag2+'.sh', 'w') as f:
					f.write(ud2)
				t1="user_data_base64 = filebase64sha256(\""+flag2+".sh\")\n lifecycle {\n   ignore_changes = [user_data_replace_on_change,user_data,user_data_base64,metadata_options[0].http_protocol_ipv6,launch_template[0].version]\n}\n"
				globals.ec2ignore=True
			except KeyError:
				pass

		elif tt1 == "user_data_base64": skip=1
	
		elif tt1 == "iam_instance_profile":
			if tt2 != "null":
				t1=tt1 + " = aws_iam_instance_profile." + tt2 + ".name\n"
				common.add_dependancy("aws_iam_instance_profile",tt2)


		elif tt1 == "security_groups": skip=1
		elif tt1 == "key_name": 
			if tt2 != "null":
				if not globals.dkey:
					tfil=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
					t1=tt1 + " = aws_key_pair." + tfil + ".id\n"
					common.add_dependancy("aws_key_pair",tt2)
				else:
					tfil=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
					t1=tt1 + " = data.aws_key_pair." + tfil + ".key_name\n"
					common.add_dependancy("aws_key_pair", tt2)

		elif tt1 == "user_data_replace_on_change" and tt2 == "null":
			t1=tt1 + " = false\n"
			if globals.ec2ignore==False:
				globals.ec2ignore=True
				t1=t1+"\n lifecycle {\n   ignore_changes = [user_data_replace_on_change,user_data,user_data_base64,metadata_options[0].http_protocol_ipv6,launch_template[0].version]\n}\n"		

		elif tt1 == "http_protocol_ipv6" and tt2 == "null":
			t1=tt1 + " = \"disabled\"\n"
		
			#t1=t1+"\n lifecycle {\n   ignore_changes = [user_data_replace_on_change]\n}\n"

		
		
	except Exception as e:
		common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)

		
	return skip,t1,flag1,flag2


def  aws_internet_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_internet_gateway_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ip_ranges(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_key_pair(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "key_name":	
		flag1=tt2
	if tt1 == "public_key":
		client = boto3.client("ec2")
		resp=client.describe_key_pairs(KeyNames=[flag1],IncludePublicKey=True)
		resp1=resp['KeyPairs']
		for j in resp1:
			pubk=j['PublicKey']
			pubk=pubk.strip()
			t1=tt1 + " = \""+pubk+"\"\n" +"\n lifecycle {\n   ignore_changes = [public_key]\n}\n"


	return skip,t1,flag1,flag2


def aws_launch_template(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "security_group_names":    
		if tt2 == "[]":     skip=1
	elif tt1 == "throughput":
		if tt2 == "0": skip=1

	elif tt1 == "name_prefix": skip=1
	elif tt1 == "http_put_response_hop_limit":
		if tt2 == "0": skip=1

	elif tt1=="excluded_instance_types" and tt2=="[]": skip=1
	elif tt1=="included_instance_types" and tt2=="[]": skip=1
	elif tt1=="volume_initialization_rate" and tt2=="0": skip=1

	elif tt1=="on_demand_max_price_percentage_over_lowest_price" and tt2=="0": skip=1
	elif tt1=="spot_max_price_percentage_over_lowest_price" and tt2=="0": skip=1
	elif tt1=="max_spot_price_as_percentage_of_optimal_on_demand_price" and tt2=="0": skip=1

	return skip,t1,flag1,flag2

def aws_main_route_table_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def  aws_nat_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "secondary_private_ip_address_count" in tt1:
        
        if tt2 == "0": skip=1

    elif tt1 == "private_ip": skip=1
    elif tt1 == "public_ip": skip=1
    elif tt1 == "allocation_id": 
        
        t1=tt1 + " = aws_eip." + tt2 + ".id\n"
        common.add_dependancy("aws_eip",tt2)
    return skip,t1,flag1,flag2 

def  aws_network_acl(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "ipv6_cidr_block":
       if tt2 == "":
         t1=tt1+ " = null\n"
    return skip,t1,flag1,flag2

def  aws_default_network_acl(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_network_acl_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_network_acl_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_network_acls(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_network_interface(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "private_ips_count" in tt1:
		if tt2 == "0": skip=1
	elif "private_ips_count" in tt1:
		if tt2 == "0": skip=1
	elif "ipv6_prefixes" in tt1:
		
		if tt2 == "[]": skip=1
	elif "ipv6_address_count" in tt1:
		
		if tt2 == "0": skip=1
	elif "ipv6_address_list" in tt1:
		
		if tt2 == "[]": skip=1
	elif "ipv4_prefix_count" in tt1:
		
		if tt2 == "0": skip=1
	elif "ipv4_prefixes" in tt1:
		
		if tt2 == "[]": skip=1
	
	

	return skip,t1,flag1,flag2

def aws_network_interface_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_network_interface_sg_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_network_interfaces(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_placement_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_prefix_list(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_region(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_regions(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_route(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def  aws_route_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "cidr_block" in tt1:   
		if tt2 == "": t1=tt1 + " = null\n"

	elif "nat_gateway_id" in tt1 and tt2.startswith("nat-"):
		t1=tt1 + " = aws_nat_gateway." + tt2 + ".id\n"
		common.add_dependancy("aws_nat_gateway",tt2)
	elif tt1 == "gateway_id" and tt2.startswith("igw-"):
		t1=tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
		common.add_dependancy("aws_internet_gateway",tt2)
	elif tt1 == "vpc_peering_connection_id" and tt2.startswith("pcx-"):
		t1=tt1 + " = aws_vpc_peering_connection." + tt2 + ".id\n"
		common.add_dependancy("aws_vpc_peering_connection",tt2)
	elif tt1 == "transit_gateway_id" and tt2.startswith("tgw-"):
		t1=tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
		common.add_dependancy("aws_ec2_transit_gateway", tt2)
# network_interface_id
	elif tt1 == "network_interface_id" and tt2.startswith("eni-"):
		t1=tt1 + " = aws_network_interface." + tt2 + ".id\n"
		common.add_dependancy("aws_network_interface", tt2)

	return skip,t1,flag1,flag2


def aws_route_table_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "route_table_id":
		t1=tt1 + " = aws_route_table." + tt2 + ".id\n"
		common.add_dependancy("aws_route_table",tt2)
	elif tt1 == "gateway_id":
		if tt2.startswith("igw-"):
			t1 = tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
		if tt2 == "null":
			skip=1
    #print("------Yo t1="+t1)
	return skip,t1,flag1,flag2

def aws_security_group_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "ipv6_cidr_blocks":	
		if tt2 == "[]": skip=1
	elif tt1 == "cidr_blocks":
		if tt2 == "[]": skip=1
	elif tt1 == "self":	
		if tt2 == "false": skip=1


	return skip,t1,flag1,flag2

def aws_security_group(t1,tt1,tt2,flag1,flag2):
    skip = 0
    #print("entry t1="+t1+" lbc="+str(globals.lbc))

    if tt1 == "name":  
        if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    ##if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
	# fix via ingress /egress rules - ?
    elif tt1 == "egress" or globals.lbc > 0 :
        
        
        if tt2 == "[]": skip = 1
        if "[" in t1: globals.lbc=globals.lbc+1
        if "]" in t1: globals.lbc=globals.lbc-1
        #print("***t1="+t1+" lbc="+str(globals.lbc))
	
        if globals.lbc > 0: skip = 1
        if globals.lbc == 0:
           #print("***t1="+t1+" lbc="+str(globals.lbc))
           if "]" in t1.strip(): skip=1

    elif tt1 == "ingress" or globals.lbc > 0 :
        
        
        if tt2 == "[]": skip = 1
        if "[" in t1: globals.lbc=globals.lbc+1
        if "]" in t1: globals.lbc=globals.lbc-1
        #print("***t1="+t1+" lbc="+str(globals.lbc))
	
        if globals.lbc > 0: skip = 1
        if globals.lbc == 0:
           #print("***t1="+t1+" lbc="+str(globals.lbc))
           if "]" in t1.strip(): skip=1

    elif tt1 == "name_prefix" and flag1 is True: skip=1
       
    #  
    #print("exit t1="+t1+" lbc="+str(globals.lbc))          
    return skip,t1,flag1,flag2

def aws_snapshot_create_volume_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_spot_datafeed_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_spot_fleet_request(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "load_balancers" and tt2=="null": skip=1
	elif tt1 == "target_group_arns" and tt2=="null": skip=1
	elif tt1 == "id" and tt2.startswith("lt-"):
		t1=tt1 + " = aws_launch_template." + tt2 + ".id\n"
		common.add_dependancy("aws_launch_template", tt2)
	elif tt1 == "allocation_strategy" and tt2!="null":
		t1=t1+"\n lifecycle {\n   ignore_changes = [target_group_arns,load_balancers,wait_for_fulfillment]\n}\n"
	elif tt1=="key_name" and tt2 != "null":
		if globals.dkey:
			tfil=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
			t1=tt1 + " = data.aws_key_pair." + tfil + ".key_name\n"
			common.add_dependancy("aws_key_pair",tt2)
		else:
			tfil=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
			t1=tt1 + " = aws_key_pair." + tfil + ".id\n"
			common.add_dependancy("aws_key_pair",tt2)
	return skip,t1,flag1,flag2

def aws_spot_instance_request(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_subnet(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "resource" in t1 and "{" in t1 and "aws_subnet" in t1:
		globals.subnetid=""
		inid=t1.split('aws_subnet"')[1].split("{")[0].strip().strip('"')
		globals.subnetid=inid
	elif tt1 == "enable_lni_at_device_index":
		if tt2 == "0": skip=1
	elif tt1 == "availability_zone_id": skip=1
	#
	elif tt1 == "map_customer_owned_ip_on_launch":
		if tt2 == "false": skip=1

	elif tt1=="ipv6_cidr_block" and tt2.endswith("/64"):
		try:
			nbs=tt2.split("::")[0].split(":")[-1]
			nb=int(nbs[-2:])
			for j in globals.subnets:
				if j['SubnetId'] == globals.subnetid:
					vpcid=j['VpcId']
					t1=tt1 + " = cidrsubnet(aws_vpc." + vpcid + ".ipv6_cidr_block, 8, "+str(nb)+")\n"
		except Exception as e:
			print("ERROR in ipv6_cidr_block, fix aws_subnet: "+str(e))

	return skip,t1,flag1,flag2

def aws_volume_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


def  aws_vpc(t1,tt1,tt2,skipipv6,flag2):
    skip = 0
    if tt1 == "assign_generated_ipv6_cidr_block":
        if tt2 in "true": skipipv6=True
    elif tt1 == "ipv6_cidr_block":
        if skipipv6: skip = 1
    elif tt1 == "ipv6_ipam_pool_id":
        if skipipv6: skip = 1
    elif tt1 == "ipv6_netmask_length":
        if tt2 == "0":  skip=1
    elif tt1 == "owner_id": skip=1
    #            
    return skip,t1,skipipv6,flag2


def aws_vpc_dhcp_options_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0

	if tt1 == "ip_address_type":
		if tt2 == "IPV4": 
			t1=tt1 + " = \"ipv4\"\n"
			t1=t1+"\n lifecycle {\n   ignore_changes = [ip_address_type]\n}\n"
		elif tt2 == "IPV6": 
			t1=tt1 + " = \"ipv6\"\n"
			t1=t1+"\n lifecycle {\n   ignore_changes = [ip_address_type]\n}\n"
		elif tt2 == "DUALSTACK": 
			t1=tt1 + " = \"dualstack\"\n"
			t1=t1+"\n lifecycle {\n   ignore_changes = [ip_address_type]\n}\n"
		
	return skip,t1,flag1,flag2

def aws_vpc_dhcp_options(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_vpc_endpoint_connection_accepter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_connection_notification(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_route_table_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_security_group_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_service(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="gateway_load_balancer_arns" and tt2=="[]": skip=1
	elif tt1=="network_load_balancer_arns" and tt2=="[]": skip=1
	elif tt1=="allowed_principal" and tt2=="[]": skip=1
	elif tt1 == "network_load_balancer_arns": 
		t1=fixtf.deref_elb_arn_array(t1,tt1,tt2)
	
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_service_allowed_principal(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_endpoint_subnet_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_organization_admin_account(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_pool(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_pool_cidr(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_pool_cidr_allocation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_preview_next_cidr(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_resource_discovery(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_resource_discovery_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipam_scope(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_ipv4_cidr_block_association(t1,tt1,tt2,skipipv6,flag2):
    skip = 0         

    return skip,t1,skipipv6,flag2

def aws_vpc_ipv6_cidr_block_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_network_performance_metric_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_peering_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_peering_connection_accepter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_peering_connection_options(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_security_group_egress_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpc_security_group_ingress_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpn_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1.startswith("tunnel") and tt2=="0": skip=1

	return skip,t1,flag1,flag2

def aws_vpn_connection_route(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpn_gateway(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpn_gateway_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpn_gateway_route_propagation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_verifiedaccess_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_verifiedaccess_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_verifiedaccess_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_verifiedaccess_instance_logging_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_verifiedaccess_instance_trust_provider_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_verifiedaccess_trust_provider(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2