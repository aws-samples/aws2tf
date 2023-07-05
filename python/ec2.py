#!/usr/bin/env python3

import boto3
import json
import multiprocessing
import sys
import signal
import os
import subprocess
import aws2tf


def do_state(sf,awsout,ttft,idf):
   
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
         rname=awsout[ic][idf]
         #print("rname="+rname)
         aws2tf.res_head(sf,ttft,rname)
         sf.write('            "id": "' + rname +'"\n')
         aws2tf.res_tail(sf)


def get_resource(sf,fields,type):
   """Get all VPCs in an account."""
   print("doing "+type)
   response=fields[type]()
   awsout = response[type]
   filename='data/'+type+'.json'

   #print(json.dumps(awsout, indent=4, default=str))
   """Save to a JSON file."""
   with open(filename, 'w') as f:
      json.dump(awsout, f, indent=4, default=str)

   # state
   if type == "Vpcs":            
      do_state(sf,awsout,"aws_vpc","VpcId")
   if type == "Subnets":         
      do_state(sf,awsout,"aws_subnet","SubnetId")
   if type == "SecurityGroups":   
      do_state(sf,awsout,"aws_security_group","GroupId")
   if type == "Reservations":   
      #print(json.dumps(awsout, indent=4, default=str))
      do_state(sf,awsout,"aws_instance","GroupId")



####################################################


def ec2_resources(sf):
   ec2client = boto3.client('ec2')  

    # comma lists are required to create a dictionary
   fields2 = {
              'Vpcs':ec2client.describe_vpcs,
              'Subnets':ec2client.describe_subnets,
              'SecurityGroups':ec2client.describe_security_groups,
              'Reservations':ec2client.describe_instances,
              'NetworkInterfaces':ec2client.describe_network_interfaces,
              'RouteTables':ec2client.describe_route_tables,
              #'Routes':ec2client.describe_route_tables,
              'AvailabilityZones':ec2client.describe_availability_zones,
              #'Images':ec2client.describe_images,
              #'KeyPairs':ec2client.describe_key_pairs,
              #'Snapshots':ec2client.describe_snapshots,
              #'VolumeAttachments':ec2client.describe_volumes,
              #'Instances':ec2client.describe_instances,
              #'ElasticLoadBalancers':ec2client.describe_load_balancers,
              #'TargetGroups':ec2client.describe_target_groups,
              #'LoadBalancers':ec2client.describe_load_balancers,
              'VpnGateways':ec2client.describe_vpn_gateways,
              'VpnConnections':ec2client.describe_vpn_connections,
              'TransitGateways':ec2client.describe_transit_gateways,
              'TransitGatewayConnectPeers':ec2client.describe_transit_gateway_connect_peers,
              'TransitGatewayConnects':ec2client.describe_transit_gateway_connects,
              'TransitGatewayMulticastDomains':ec2client.describe_transit_gateway_multicast_domains,
              'TransitGatewayVpcAttachments':ec2client.describe_transit_gateway_vpc_attachments,
              #'TransitGatewayVpns':ec2client.describe_transit_gateway_vpns,
              'TransitGatewayRouteTables':ec2client.describe_transit_gateway_route_tables,
              #'TransitGatewayRouteTableVpcAssociations':ec2client.describe_transit_gateway_route_table_vpc_associations,
              #'TransitGatewayRouteTablePropagations':ec2client.describe_transit_gateway_route_table_propagations,
              'TransitGatewayPeeringAttachments':ec2client.describe_transit_gateway_peering_attachments,
              #'TransitGatewayMulticastGroups':ec2client.describe_transit_gateway_multicast_groups,
              #'TransitGatewayMulticastGroupSources':ec2client.describe_transit_gateway_multicast_group_sources,
              #'TransitGatewayMulticastGroupMembers':ec2client.describe_transit_gateway_multicast_group_members,

              'TransitGatewayAttachments':ec2client.describe_transit_gateway_attachments,
              'TransitGatewayRouteTables':ec2client.describe_transit_gateway_route_tables,
              'InternetGateways':ec2client.describe_internet_gateways,
              'DhcpOptions':ec2client.describe_dhcp_options,
              'NetworkAcls':ec2client.describe_network_acls,
              }  
       
   fields = {
               #'Vpcs':ec2client.describe_vpcs,
               #'Subnets':ec2client.describe_subnets, 
               #'SecurityGroups':ec2client.describe_security_groups, 
               'Reservations':ec2client.describe_instances, 
              }
    #response=ec2client.describe_instances()
    #awsout = response['Reservations']
    #print(json.dumps(awsout, indent=4, default=str))
    #exit()
    #get_resource('Reservations','ec2client.describe_instances')
    #exit()


   for key in fields:
        print(key)
        #
        get_resource(sf,fields,key)

        #print(res.get())
        #get_resource(fields,key)
        # Wait for all tasks to complete
 

    

   print("Done ec2_resources")




