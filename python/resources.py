#!/usr/bin/env python3

import boto3
import json
import multiprocessing
import sys
import signal
import os
import subprocess


def ctrl_c_handler(signum, frame):
  print("Ctrl-C pressed.")
  exit()


def check_python_version():
  version = sys.version_info
  major = version.major
  minor = version.minor
  if major < 3 or (major == 3 and minor < 7):
    print("This program requires Python 3.7 or later.")
    sys.exit(1)

def is_pool_running(pool):
    """Check if a multiprocessing pool is running."""

    if pool is None:
        return False
    return True


def get_all_s3_buckets():
  """Gets all the AWS S3 buckets and saves them to a file."""
  s3a = boto3.resource("s3")
  s3 = boto3.client("s3")

  buckets = s3a.buckets.all()

  

  for buck in buckets: 
   
     bucket_name=buck.name
     fn="data/s3-"+str(bucket_name)+".json"
     print(fn)
     with open(fn, "w") as f:
   
   
      print("Bucket: "+bucket_name + '  ----------------------------------------------------------------')

      try:
         print('location')
         location = s3.get_bucket_location(Bucket=bucket_name)
         
         bl=location['LocationConstraint']
         if bl != my_region:
            print('continuing on non default location '+ bl)
            continue
         if bl is None:  
               print('continuing on None location .......')
               continue
         elif bl == 'null':  
               print('continuing on null location .......')
               continue
         else:
            print(bl)
            
      except:
         print('continuing on exception to location .......')
         continue

      f.write("{\n")
      f.write("name: '" + "bucket_name" + "'\n")
      f.write("{\n")

      #print(bucket)
      try:
         print('analytics')
         analytics = s3.get_bucket_analytics(Bucket=bucket_name)
         json.dump(analytics, f,indent=4, default=str)
      except:
         analytics = None 

      try:
         print('accelerate')
         accelerate = s3.get_accelerate_configuration(Bucket=bucket_name)
         print(json.dumps(accelerate, indent=4, default=str))
      except:
         accelerate = None

      try:  
         #print('acl')
         acl=s3.get_bucket_acl(Bucket=bucket_name)
         #print(json.dumps(acl, indent=4, default=str))
         f.write("acl: '" + json.dumps(acl, indent=4, default=str) + "'\n")
      except:
         acl=None

      try:
         print('cors')
         cors=s3.get_bucket_cors(Bucket=bucket_name)
         print(json.dumps(cors, indent=4, default=str))
      except:
         cors=None   

      try:
         print('tiering')
         intelligent_tiering_configuration = s3.get_bucket_intelligent_tiering_configuration(Bucket=bucket_name)
         print(json.dumps(intelligent_tiering_configuration, indent=4, default=str))
      except:
         intelligent_tiering_configuration = None

      try:   
         #print('crypto')
         encryption = s3.get_bucket_encryption(Bucket=bucket_name)
         #print(json.dumps(encryption, indent=4, default=str))
      except:
         encryption = None

      try:
         print('inventory')  
         inventory = s3.get_inventory_configuration(Bucket=bucket_name)
         print(json.dumps(inventory, indent=4, default=str))
      except:
         inventory = None

      try:   
         print('lifecycle')
         lifecycle = s3.get_bucket_lifecycle(Bucket=bucket_name)
         print(json.dumps(lifecycle, indent=4, default=str))
      except:
         lifecycle = None

      try:
         #print('location')
         location = s3.get_bucket_location(Bucket=bucket_name)
         #print(json.dumps(location, indent=4, default=str))
      except:
         location = None
      try:   
         print('logging')
         logging = s3.get_bucket_logging(Bucket=bucket_name)
         print(json.dumps(logging, indent=4, default=str))
         
      except:
         logging = None

      try:   
         print('metrics')
         metrics = s3.get_bucket_metrics(Bucket=bucket_name)
         print(json.dumps(metrics, indent=4, default=str))
      except:
         metrics = None

      try:
         notification = s3.Notification()
      except:
         notification = None

      try: 
         object_lock_configuration = s3.get_bucket_object_lock_configuration(Bucket=bucket_name)
      except:
         object_lock_configuration = None

      try:
         object_ownership = s3.get_bucket_object_ownership(Bucket=bucket_name)
      except:
         object_ownership = None

      try:
         #print('policy')
         policy = s3.get_bucket_policy(Bucket=bucket_name)
         #print(json.dumps(policy, indent=4))
      except:
         policy = None

      try:
         print('replic')
         replication = s3.get_bucket_replication(Bucket=bucket_name)
         print(json.dumps(replication, indent=4, default=str))
      except:
         replication = None

      try:
         #print('request')
         request_payer = s3.get_bucket_request_payment(Bucket=bucket_name)
         #print(json.dumps(request_payer, indent=4, default=str))

      except:
         request_payment = None

      try:
         #print('tagging')
         tagging = s3.get_bucket_tagging(Bucket=bucket_name)
         #print(json.dumps(tagging, indent=4, default=str))
      except:
         tagging = None

      try:
         print('vers')
         versioning = s3.get_bucket_versioning(Bucket=bucket_name)
         print(json.dumps(versioning, indent=4, default=str))
         
      except:
         versioning = None
      
      try:   
         #print('website')
         website = s3.get_bucket_website(Bucket=bucket_name)
         #print(json.dumps(website, indent=4, default=str))  
      except:
         website = None

      f.write("}\n")
      f.write("}\n")
      f.close()

  #with open("s3.json", "w") as f:
  #  json.dump(buckets, f)


def get_resource(fields,type):
    """Get all VPCs in an account."""
    print("doing "+type)
    response=fields[type]()
    awsout = response[type]
    filename='data/'+type+'.json'
    """Save to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(awsout, f, indent=4, default=str)

if __name__ == '__main__':
    check_python_version()
    signal.signal(signal.SIGINT, ctrl_c_handler)

# get the current region
    my_session = boto3.session.Session()
    my_region = my_session.region_name

    print(my_region)
   
    ec2client = boto3.client('ec2')
    cpus=multiprocessing.cpu_count()
    print("cpus="+str(cpus))
    
    get_all_s3_buckets()
    exit()


    # comma lists are required to create a dictionary
    fields = {
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
    

    #response=ec2client.describe_instances()
    #awsout = response['Reservations']
    #print(json.dumps(awsout, indent=4, default=str))
    #exit()
    #get_resource('Reservations','ec2client.describe_instances')
    #exit()


    for key in fields:
        print(key)
        #
        get_resource(fields,key)

        #print(res.get())
        #get_resource(fields,key)
        # Wait for all tasks to complete

    print("closing ....")
    #pool.close()
    print("Waiting for all tasks to complete...")
    #pool.join()  

    

    print("Done")



