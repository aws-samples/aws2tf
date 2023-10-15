def resource_types(type):
    if type == "net":
        #net=["aws_vpc","aws_subnet","aws_security_group","aws_internet_gateway","aws_nat_gateway","aws_route_table","aws_vpc_endpoint"]
        net=["aws_vpc","aws_vpc_dhcp_options","aws_subnet","aws_internet_gateway","aws_nat_gateway","aws_route_table","aws_vpc_endpoint","aws_security_group"]
        # call aws_route_table_association from subnet and igw
        return net
    #elif type == "iam": return ["aws_iam_role","aws_iam_policy","aws_iam_user"]
    elif type == "iam": return ["aws_iam_role"]

    else:
        same=[type]
        return same


# problematic: "aws_network_acl"
# Error: use the `aws_default_network_acl` resource instead

# 5x returns:
# boto3.client('ec2') - so for example ec2
# the describe function - like describe-vpcs
# from the response -the top level key - like Vpcs
# the primary filter for the API call - either direct to describe call - or as part of filter Name=""
# finally - in the response what the primary id field is vpc-id 



def resource_data(type,id):

    clfn=None
    descfn=None
    topkey=None
    key=None
    filterid=None

    if type == "aws_vpc": 
            clfn="ec2"
            descfn="describe_vpcs"
            topkey='Vpcs' 
            key="VpcId" 
            filterid=key

    elif type == "aws_vpc_endpoint": 
        clfn="ec2"
        descfn="describe_vpc_endpoints"
        topkey="VpcEndpoints"
        key="VpcEndpointId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"
    
    elif type in "aws_subnet":
        clfn="ec2"
        descfn="describe_subnets"
        topkey="Subnets"
        key="SubnetId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_security_group": 
        clfn="ec2"
        descfn="describe_security_groups"
        topkey="SecurityGroups"
        key="GroupId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"         

    elif type == "aws_internet_gateway": 
        clfn="ec2"
        descfn="describe_internet_gateways"
        topkey="InternetGateways"
        key="InternetGatewayId"
        filterid=key
        if id is not None and "vpc-" in id: filterid=".Attachments.0.VpcId"    

    elif type == "aws_nat_gateway": 
        clfn="ec2"
        descfn="describe_nat_gateways"
        topkey="NatGateways"
        key="NatGatewayId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"           

    elif type == "aws_network_acl": 
        clfn="ec2"
        descfn="describe_network_acls"
        topkey="NetworkAcls"
        key="NetworkAclId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId" 

    elif type == "aws_route_table": 
        clfn="ec2"
        descfn="describe_route_tables"
        topkey="RouteTables"
        key="RouteTableId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"    


    elif type == "aws_route_table_association":
        clfn="ec2"
        descfn="describe_route_tables"
        topkey="RouteTables"
        key=".Associations.0.SubnetId"
        filterid=key
        if id is not None and "vpc-" in id: filterid=".Associations.0.SubnetId" 
        if id is not None and "subnet-" in id: filterid=".Associations.0.SubnetId" 

    elif type == "aws_default_network_acl": 
        clfn="ec2"
        descfn="describe_network_acls"
        topkey="NetworkAcls"
        key="NetworkAclId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_route_table":
        clfn="ec2"
        descfn="describe_route_tables"
        topkey="RouteTables"
        key="RouteTableId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_security_group":
        clfn="ec2"
        descfn="describe_security_groups"
        topkey="SecurityGroups"
        key="GroupId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_subnet":
        clfn="ec2"
        descfn="describe_subnets"
        topkey="Subnets"
        key="SubnetId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_vpc":
        clfn="ec2"
        descfn="describe_vpcs"
        topkey="Vpcs"
        key="VpcId"
        filterid=KeyError

    elif type == "aws_default_internet_gateway":
        clfn="ec2"
        descfn="describe_internet_gateways"
        topkey="InternetGateways"
        key="InternetGatewayId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="attachment.vpc-id"

    elif type == "aws_vpc_dhcp_options":
        clfn="ec2"
        descfn="describe_dhcp_options"
        topkey="DhcpOptions"
        key="DhcpOptionsId"
        filterid=""


    elif type == "aws_image":
        clfn="ec2"
        descfn="describe_images"
        topkey="Images"
        key="ImageId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_key_pair":
        clfn="ec2"
        descfn="describe_key_pairs"
        topkey="KeyPairs"
        key="KeyName"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_launch_configuration":
        clfn="autoscaling"
        descfn="describe_launch_configurations"
        topkey="LaunchConfigurations"
        key="LaunchConfigurationName"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_launch_template":
        clfn="ec2"
        descfn="describe_launch_templates"
        topkey="LaunchTemplates"
        key="LaunchTemplateId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_load_balancer":
        clfn="elb"
        descfn="describe_load_balancers"
        topkey="LoadBalancerDescriptions"
        key="LoadBalancerName"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_transit_gateway_vpc_attachment":
        clfn="ec2"
        descfn="describe_transit_gateway_vpc_attachments"
        topkey="TransitGatewayVpcAttachments"
        key="TransitGatewayAttachmentId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_transit_gateway_route_table_vpc_association":
        clfn="ec2"
        descfn="describe_transit_gateway_route_table_vpc_associations"
        topkey="TransitGatewayRouteTableVpcAssociations"
        key="TransitGatewayAttachmentId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"
    
    elif type == "aws_transit_gateway_route_table_propagation":
        clfn="ec2"
        descfn="describe_transit_gateway_route_table_propagations"
        topkey="TransitGatewayRouteTablePropagations"
        key="TransitGatewayAttachmentId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_vpc_ipv4_cidr_block_association":
        clfn="ec2"
        descfn="describe_vpc_cidr_block_association_sets"
        topkey="VpcId"
        key="AssociationId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_iam_role":
        clfn="iam"
        descfn="list_roles"
        topkey="Roles"
        key="RoleName"
        filterid=key
        if id is not None and "arn:aws:iam::" in id: filterid="Arn"



    elif type == "aws_iam_policy":
        clfn="iam"
        descfn="list_policies"
        topkey="Policies"
        key="PolicyName"
        filterid=key  # no filter on list-policies so use jq like filter
        if id is not None and "arn:aws:iam::" in id: filterid="Arn"


    elif type == "aws_iam_user":
        clfn="iam"
        descfn="list_users"
        topkey="Users"
        key="UserName"
        filterid=key  # no filter on list-users so use jq like filter
        if id is not None and "arn:aws:iam::" in id: filterid="Arn"

    elif type == "aws_flow_log":
        clfn="ec2"
        descfn="describe_flow_logs"
        topkey="FlowLogs"
        key="FlowLogId"
        filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"


   #if type == "aws_availability_zone": return 'AvailabilityZones', ec2client.describe_availability_zones, "ZoneName"

   #if type == "aws_elastic_load_balancer": return 'ElasticLoadBalancers', ec2client.describe_load_balancers, "LoadBalancerName"
   #if type == "aws_instance": return 'Reservations', ec2client.describe_instances, "InstanceId"

   #if type == "aws_load_balancer": return 'LoadBalancers', ec2client.describe_load_balancers, "LoadBalancerName"
   
   #if type == "aws_snapshot": return 'Snapshots', ec2client.describe_snapshots, "SnapshotId"
   #if type == "aws_target_group": return 'TargetGroups', ec2client.describe_target_groups, "TargetGroupName"

      # 'TransitGatewayAttachments':ec2client.describe_transit_gateway_attachments,
   #if type == "aws_transit_gateway": return 'TransitGateways', ec2client.describe_transit_gateways, "TransitGatewayId"
   #if type == "aws_transit_gateway_connect_peer": return 'TransitGatewayConnectPeers', ec2client.describe_transit_gateway_connect_peers, "TransitGatewayConnectPeerId"
   #if type == "aws_transit_gateway_connect": return 'TransitGatewayConnects', ec2client.describe_transit_gateway_connects, "TransitGatewayConnectId"
   #if type == "aws_transit_gateway_multicast_domain": return 'TransitGatewayMulticastDomains', ec2client.describe_transit_gateway_multicast_domains, "TransitGatewayMulticastDomainId"
   #if type == "aws_transit_gateway_vpc_attachment": return 'TransitGatewayVpcAttachments', ec2client.describe_transit_gateway_vpc_attachments, "TransitGatewayAttachmentId"
   #if type == "aws_transit_gateway_vpn": return 'TransitGatewayVpns', ec2client.describe_transit_gateway_vpns, "TransitGatewayVpnId"
   #if type == "aws_transit_gateway_route_table": return 'TransitGatewayRouteTables', ec2client.describe_transit_gateway_route_tables, "TransitGatewayRouteTableId"
   #if type == "aws_transit_gateway_route_table_vpc_association": return 'TransitGatewayRouteTableVpcAssociations', ec2client.describe_transit_gateway_route_table_vpc_associations, "TransitGatewayAttachmentId"
   #if type == "aws_transit_gateway_route_table_propagation": return 'TransitGatewayRouteTablePropagations', ec2client.describe_transit_gateway_route_table_propagations, "TransitGatewayAttachmentId"
   #if type == "aws_transit_gateway_peering_attachment": return 'TransitGatewayPeeringAttachments', ec2client.describe_transit_gateway_peering_attachments, "TransitGatewayAttachmentId"
   #if type == "aws_transit_gateway_multicast_group": return 'TransitGatewayMulticastGroups', ec2client.describe_transit_gateway_multicast_groups, "TransitGatewayMulticastDomainId"
   #if type == "aws_transit_gateway_multicast_group_source": return 'TransitGatewayMulticastGroupSources', ec2client.describe_transit_gateway_multicast_group_sources, "TransitGatewayMulticastDomainId"
   #if type == "aws_transit_gateway_multicast_group_member": return 'TransitGatewayMulticastGroupMembers', ec2client.describe_transit_gateway_multicast_group_members, "TransitGatewayMulticastDomainId"
   #if type == "aws_transit_gateway_attachment": return 'TransitGatewayAttachments', ec2client.describe_transit_gateway_attachments, "TransitGatewayAttachmentId"
   #if type == "aws_transit_gateway_route_table": return 'TransitGatewayRouteTables', ec2client.describe_transit_gateway_route_tables, "TransitGatewayRouteTableId"
      
   #if type == "aws_volume": return 'VolumeAttachments', ec2client.describe_volumes, "VolumeId"

   #if type == "aws_vpn_gateway": return 'VpnGateways', ec2client.describe_vpn_gateways, "VpnGatewayId"
   #if type == "aws_vpn_connection": return 'VpnConnections', ec2client.describe_vpn_connections, "VpnConnectionId", "vpc-id"

    
    return clfn,descfn,topkey,key,filterid
