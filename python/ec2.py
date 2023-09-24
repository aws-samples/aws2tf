#!/usr/bin/env python3

import boto3
import json
import os
import common
import fixtf

# called by aws2tf.py
def ec2_resources(type,id):   # state file, aws_vpc , vpc-xxxxxxxxx called from main.py
   ec2client = boto3.client('ec2')   
   botokey,clfn,jsonid,filterid=resource_data(type,ec2client)
   print("calling get_resource with id="+str(id))
   # call with statefile, ec2client fn, type,
   ec2fn = getattr(ec2client, clfn)
## overrides here - eg use vpcid to filter subnets - rather than default subnet-id
   if type in "aws_subnet" and id in "vpc-":
      print(type+' '+id)
      get_resource(type,id,botokey,ec2fn,jsonid,"vpc-id")
   else: 
      # generic call
      get_resource(type,id,botokey,ec2fn,jsonid,filterid)
   #print("Done ec2_resources")


# aws_vpc, vpc-xxxx, 'Vpcs', ec2client.describe_vpcs, "VpcId", "vpc-id"
def get_resource(type,id,botokey,ec2fn,jsonid,filterid):
   """Get all VPCs in an account."""
   print("doing "+ type + ' with id ' + str(id))
   if id is None:
      response=ec2fn()   ##   ec2client.describe_vpcs()
   else:
      print("calling with filter id="+filterid + " and id=" + id)
      response=ec2fn(Filters=[{'Name': filterid, 'Values': [id]}]) ##   ec2client.describe_vpcs()
      #

   com="rm -f "+type+"*.tf "+type+"*.out"
   rout=common.rc(com)

   fn=type+"_import.tf"
   with open(fn, "w") as f:
         for item in response[botokey]:
               theid=item[jsonid]
               f.write('import {\n')
               f.write('  to = ' +type + '.' + theid + '\n')
               f.write('  id = "'+ theid + '"\n')
               f.write('}\n')
   f.close()

   print("tf plan")
   
   rf=type+"_resources.out"
   com="terraform plan -generate-config-out="+rf
   rout=common.rc(com)

   
  
   if "0 to destroy" not in str(rout.stdout.decode().rstrip()):
      print("--> plan warning destroy - existing state ?")
      print(str(rout.stdout.decode().rstrip()))
      print("--> plan warning destroy - existing state ?")

      #exit()
   print("gen complete")


   #gr=getfn(type)
   print("calling fixtf "+ type)
   getfn = getattr(fixtf, type)
   gr=getfn()
   #
   # Save output


def resource_data(type,ec2client):

   # tf_type   toplevel from cli describe - id field from awc cli, --filter field for cli, ec2 fn client call, fn call to filter tf

   #if type == "aws_availability_zone": return 'AvailabilityZones', ec2client.describe_availability_zones, "ZoneName"
   #if type == "aws_dhcp_options": return 'DhcpOptions', ec2client.describe_dhcp_options, "DhcpOptionsId"
   #if type == "aws_elastic_load_balancer": return 'ElasticLoadBalancers', ec2client.describe_load_balancers, "LoadBalancerName"

   #if type == "aws_internet_gateway": return 'InternetGateways', ec2client.describe_internet_gateways, "InternetGatewayId"
   #if type == "aws_instance": return 'Reservations', ec2client.describe_instances, "InstanceId"
   #if type == "aws_image": return 'Images', ec2client.describe_images, "ImageId"

   #if type == "aws_key_pair": return 'KeyPairs', ec2client.describe_key_pairs, "KeyName"

   #if type == "aws_load_balancer": return 'LoadBalancers', ec2client.describe_load_balancers, "LoadBalancerName"
   #if type == "aws_network_acl": return 'NetworkAcls', ec2client.describe_network_acls, "NetworkAclId"
   #if type == "aws_network_interface": return 'NetworkInterfaces', ec2client.describe_network_interfaces, "NetworkInterfaceId"

   #if type == "aws_route_table": return 'RouteTables', ec2client.describe_route_tables, "RouteTableId"
   #if type == "aws_route": return 'Routes', ec2client.describe_route_tables, "RouteTableId"

   if type == "aws_security_group": return 'SecurityGroups', "describe_security_groups", "GroupId","group-id"
   if type == "aws_subnet": return 'Subnets', "describe_subnets", "SubnetId","subnet-id"
   
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
   #if type == "aws_vpc": return 'Vpcs', ec2client.describe_vpcs, "VpcId", "vpc-id", aws_vpc.get_vpc
   if type == "aws_vpc": return 'Vpcs', "describe_vpcs", "VpcId", "vpc-id"
   #if type == "aws_vpn_gateway": return 'VpnGateways', ec2client.describe_vpn_gateways, "VpnGatewayId"
   #if type == "aws_vpn_connection": return 'VpnConnections', ec2client.describe_vpn_connections, "VpnConnectionId", "vpc-id"

   return None, None, None, None, None



