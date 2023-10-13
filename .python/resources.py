def resource_types(type):
    if type == "net":
        #net=["aws_vpc","aws_subnet","aws_security_group","aws_internet_gateway","aws_nat_gateway","aws_route_table","aws_vpc_endpoint"]
        net=["aws_vpc","aws_subnet"]
        return net
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
            filterid="vpc-id"

    elif type == "aws_vpc_endpoint": 
        clfn="ec2"
        descfn="describe_vpc_endpoints"
        topkey="VpcEndpoints"
        filterid="VpcEndpointIds"
        jsonid="vpc-endpoint-id"
        if id is not None and id in "vpc-": filterid="VpcId"

    
    elif type in "aws_subnet":
        if id is not None and id in "vpc-":
            return "ec2","describe_subnets",        'Subnets',"VpcId","subnet-id"
        else:
            return "ec2", "describe_subnets",       'Subnets', "SubnetId","subnet-id"

   # tf_type   toplevel from cli describe - id field from awc cli, --filter field for cli, ec2 fn client call, fn call to filter tf

   #if type == "aws_availability_zone": return 'AvailabilityZones', ec2client.describe_availability_zones, "ZoneName"
   #if type == "aws_dhcp_options": return 'DhcpOptions', ec2client.describe_dhcp_options, "DhcpOptionsId"
   #if type == "aws_elastic_load_balancer": return 'ElasticLoadBalancers', ec2client.describe_load_balancers, "LoadBalancerName"

    elif type == "aws_internet_gateway": 
            return "ec2","describe_internet_gateways", "InternetGatewayId","internet-gateway-id"
   #if type == "aws_instance": return 'Reservations', ec2client.describe_instances, "InstanceId"
   #if type == "aws_image": return 'Images', ec2client.describe_images, "ImageId"

   #if type == "aws_key_pair": return 'KeyPairs', ec2client.describe_key_pairs, "KeyName"

   #if type == "aws_load_balancer": return 'LoadBalancers', ec2client.describe_load_balancers, "LoadBalancerName"
    elif type == "aws_nat_gateway": 
            return "ec2","describe_nat_gateways",   'NatGateways', "NatGatewayId","nat-gateway-id"
    elif type == "aws_network_acl": 
            return "ec2","describe_network_acls",   'NetworkAcls',  "NetworkAclId","network-acl-id"
   #if type == "aws_network_interface": return 'NetworkInterfaces', ec2client.describe_network_interfaces, "NetworkInterfaceId"

    elif type == "aws_route_table": 
            return "ec2","describe_route_tables",'RouteTables',  "RouteTableId","route-table-id"
   #if type == "aws_route": return 'Routes', ec2client.describe_route_tables, "RouteTableId"

    elif type == "aws_security_group": 
          return "ec2","describe_security_groups",'SecurityGroups',  "GroupId","group-id"



   
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


