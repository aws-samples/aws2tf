#!/usr/bin/env python3

import boto3
import json
import multiprocessing
import sys
import signal
import os
import subprocess
import aws2tf


def resource_data(type,ec2client):

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

   if type == "aws_security_group": return 'SecurityGroups', ec2client.describe_security_groups, "GroupId","group-id"
   #if type == "aws_subnet": return 'Subnets', ec2client.describe_subnets, "SubnetId"
   
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
   if type == "aws_vpc": return 'Vpcs', ec2client.describe_vpcs, "VpcId", "vpc-id"
   #if type == "aws_vpn_gateway": return 'VpnGateways', ec2client.describe_vpn_gateways, "VpnGatewayId"
   #if type == "aws_vpn_connection": return 'VpnConnections', ec2client.describe_vpn_connections, "VpnConnectionId", "vpc-id"

   return None, None, None



def do_state(sf,response,botokey,ttft,jsonid):
   awsout = response[botokey]
   #print("In state with "+ ttft + ' with id ' + jsonid)
   if ttft == "aws_instance":
      al=len(awsout)
      for ic in range(0, al): 
         a2=awsout[ic]['Instances']
         al2=len(a2)
         print(al2)
         #print(json.dumps(a2, indent=4, default=str))
         for ic2 in range(0, al2):
            a3=a2[ic2]
            print("----------------")
            print(json.dumps(a3['InstanceId'], indent=4, default=str))  
            rname=a3['InstanceId']
            aws2tf.res_head(sf,ttft,rname)
            sf.write('            "id": "' + rname +'"\n')
            aws2tf.res_tail(sf)

   else:   
   
      al=len(awsout)
      for ic in range(0, al):
         rname=awsout[ic][jsonid]

         #print("rname="+rname)
         aws2tf.res_head(sf,ttft,rname)
         sf.write('            "id": "' + rname +'"\n')
         aws2tf.res_tail(sf)


#def get_resource(sf,fields,type):
#get_resource(sf,type,id,botokey,ec2fn,jsonid)
def get_resource(sf,type,id,botokey,ec2fn,jsonid,filterid):
   """Get all VPCs in an account."""
   #print("doing "+ type + ' with id ' + str(id))
   if id is None:
      response=ec2fn()
   else:
      #print("calling with filter id="+id)
      response=ec2fn(Filters=[{'Name': filterid, 'Values': [id]}])

   # get ousout
   awsout=response[botokey]
   # test for filename

   al=len(awsout)
   for ic in range(0, al):
         rname=awsout[ic][jsonid]
         # tf file exists ?
         fn=type+"__"+rname+".tf"
         if os.path.isfile(fn):
            print("file found "+fn + " skipping json and state")
            return


   filename='data/'+type+'.json'

   #print(json.dumps(awsout, indent=4, default=str))
   """Save to a JSON file."""
   with open(filename, 'w') as f:
      json.dump(response, f, indent=4, default=str)

   do_state(sf,response,botokey,type,jsonid)
   


####################################################

# ec2 client resources
def ec2_resources(sf,type,id):   # state file, aws_vpc , vpc-xxxxxxxxx called from main.py
   ec2client = boto3.client('ec2')  

   # returns key = boto3 type, ec2client function name, Identifiier in returnded json  
   botokey,ec2fn,jsonid,filterid=resource_data(type,ec2client)
   print("calling get_resource with id="+str(id))
   # call with statefile, ec2client fn, type,
   get_resource(sf,type,id,botokey,ec2fn,jsonid,filterid)

   #print("Done ec2_resources")







