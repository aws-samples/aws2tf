#!/usr/bin/env python3

import boto3
import json
import multiprocessing
import sys
import signal
import os
import subprocess


def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol=len(out.stdout.decode('utf-8').rstrip())    
    el=len(out.stderr.decode().rstrip())
    if el!=0:
         errm=out.stderr.decode().rstrip()
         print(errm)

    # could be > /dev/null
    #if ol==0:
    #    print("No return from command " + str(cmd) + " exit ...")
    
    #print(out.stdout.decode().rstrip())
    return out


def ctrl_c_handler(signum, frame):
  print("Ctrl-C pressed.")
  exit()

def start_state(sf):
   print("start state")
       #echo $tsf
   sf.write('{\n')
   sf.write('  "version": 4,\n')
   sf.write('  "resources\": [ \n')

def end_state(sf):
   print("end state")
   sf.write('  ]\n')
   sf.write('}\n')

def res_head(sf,ttft,rname):
   #print("res head")
   sf.write('    {\n')
   sf.write('      "mode": "managed",\n')
   sf.write('      "type": "'+ ttft + '",\n')
   sf.write('      "name": "' + rname + '",\n')
   sf.write('      "provider": "provider[\\"registry.terraform.io/hashicorp/aws\\"]",\n')
   sf.write('      "instances": [ \n')
   sf.write('        {\n')
   sf.write('          "attributes": {\n') 


def res_tail(sf):
   #print("res tail")
   sf.write('          }\n')
   sf.write('        }\n')
   sf.write('      ]\n')
   sf.write('    },\n')

def s3_state(sf,ttft,bucket_name):
   rname="b_"+bucket_name
   res_head(sf,ttft,rname)
   sf.write('            "bucket": "' + bucket_name +'",\n')
   sf.write('            "id": "' + bucket_name +'"\n')
   res_tail(sf)




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


def get_s3(sf,f,s3_fields,type,bucket_name):
   try:
      #print("in get_s3 type=" + type)
      response=s3_fields[type](Bucket=bucket_name)
      print("resp done" + type)
      s3_state(sf,type,bucket_name)
      print("state done" + type)
      f.write('"' + type + '": ' + json.dumps(response, indent=4, default=str) + "\n")
   except:
      print("err: " + type)
      pass


def get_all_s3_buckets(sf):
  """Gets all the AWS S3 buckets and saves them to a file."""
  s3a = boto3.resource("s3")
  s3 = boto3.client("s3")
  s3_fields = {
      'aws_s3_bucket_accelerate_configuration': s3.get_bucket_accelerate_configuration,
      'aws_s3_bucket_acl': s3.get_bucket_acl,
      'aws_s3_bucket_analytics': s3.get_bucket_analytics_configuration,
      'aws_s3_bucket_cors_configuration': s3.get_bucket_cors,
      'aws_s3_bucket_intelligent_tiering_configuration': s3.get_bucket_intelligent_tiering_configuration,
      'aws_s3_bucket_inventory': s3.get_bucket_inventory_configuration,
      'aws_s3_bucket_lifecycle_configuration': s3.get_bucket_lifecycle_configuration,  ##   ?
      'aws_s3_bucket_logging': s3.get_bucket_logging,
      'aws_s3_bucket_metric': s3.get_bucket_metrics_configuration,
      'aws_s3_bucket_notification': s3.get_bucket_notification,
      #  no terraform resource ': s3.get_bucket_notification_configuration,
      'aws_s3_bucket_object_lock_configuration': s3.get_object_lock_configuration,
      'aws_s3_bucket_ownership_controls': s3.get_bucket_ownership_controls,
      'aws_s3_bucket_policy': s3.get_bucket_policy,
      #  no terraform resource ': s3.get_bucket_policy_status,
      'aws_s3_bucket_replication_configuration': s3.get_bucket_replication,
      'aws_s3_bucket_request_payment_configuration': s3.get_bucket_request_payment,
      'aws_s3_bucket_server_side_encryption_configuration': s3.get_bucket_encryption,
      #: no terraform resource s3.get_bucket_tagging,
      'aws_s3_bucket_versioning': s3.get_bucket_versioning,
      'aws_s3_bucket_website_configuration': s3.get_bucket_website
   }

  buckets = s3a.buckets.all()



  for buck in buckets: 
   
     bucket_name=buck.name
     if bucket_name not in 'at-dwp':
        continue

     fn="data/s3-"+str(bucket_name)+".json"

     #print(fn)
     with open(fn, "w") as f:
   
   
      print("Bucket: "+bucket_name + '  ----------------------------------------------------------------')

      try:
         #print('location')
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
            pass
            #print(bl)
            
      except:
         print('continuing on exception to location .......')
         continue

      f.write("{\n")
      f.write('"name": "' + bucket_name + '",\n')
      #f.write("{\n")

      s3_state(sf,"aws_s3_bucket",bucket_name)

      #print(bucket)
      for key in s3_fields:
         print("key="+key)
         print("outside get_s3 type=" + key)
         get_s3(sf,f,s3_fields,key,bucket_name)
      
      continue
     









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
         #print('replic')
         replication = s3.get_bucket_replication(Bucket=bucket_name)
         #print(json.dumps(replication, indent=4, default=str))
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
         #print('vers')
         #versioning = s3.get_bucket_versioning(Bucket=bucket_name)
         s3_state(sf,"aws_s3_bucket_versioning",bucket_name)
         #print(json.dumps(versioning, indent=4, default=str))
         
      except:
         versioning = None
      
      try:   
         #print('website')
         website = s3.get_bucket_website(Bucket=bucket_name)
         #print(json.dumps(website, indent=4, default=str))  
      except:
         website = None

      #f.write("}\n")
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

####################################################


if __name__ == '__main__':
   statefile='data/terraform.tfstate'
   check_python_version()
   signal.signal(signal.SIGINT, ctrl_c_handler)

# get the current region
   my_session = boto3.session.Session()
   my_region = my_session.region_name

   print(my_region)
   
   ec2client = boto3.client('ec2')
   cpus=multiprocessing.cpu_count()
   print("cpus="+str(cpus))
   stf="data/terraform.tfstate"
   print(stf)
   with open(stf, "w") as sf:
      start_state(sf)
      get_all_s3_buckets(sf)
      end_state(sf)
   

   sf.close()
   with open(r"data/terraform.tfstate", 'r') as fp:
     for count, line in enumerate(fp):
         pass
   print('Total Lines', count + 1)
   el=count-2
   print('toedit=' + str(el))
   fp.close()


      # with is like your try .. finally block in this case
   with open(statefile, 'r') as file:
      # read a list of lines into data
      data = file.readlines()


   # now change the 2nd line, note that you have to add a newline
   data[el] = '    }\n'

   # and write everything back
   with open(statefile, 'w') as file:
      file.writelines( data )
   file.close()



   f = open(statefile, 'r')
   data = json.load(f)
   f.close()
   
   com="cd data && terraform refresh -no-color -lock=false"
   rout=rc(com)
   print(rout)


   for i in data['resources']:
      #print(json.dumps(i, indent=4, default=str)) 
      ttft=i['type']
      rname=i['name']
      com="terraform state show -no-color -state " + statefile + " " + ttft + "." + rname + " > data/" + ttft + "-" + rname + ".txt"
      print(com)
      rout=rc(com)
      #print(rout)

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
   exit()



