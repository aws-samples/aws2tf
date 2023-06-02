#!/usr/bin/python3
import sys
import subprocess
import os
import json
import argparse
import sys
import boto3

# implement a  function that gets all vpcs using boto3 and saves the results to a local file called vpcs.json , also have a function parameter that passed the vpc id - if this is included then just get the specific vpc if not then get all vpcs
# then loop through the vpcs and get the subnets for each vpc   - # save the results to a local file called subnets.json
# use the vpc informaation to write a protoype terraform state file

def  get_vpc(vpc_id=None):
  
  
    ec2 = boto3.client('ec2')
    if vpc_id:
        vpcs = ec2.describe_vpcs(VpcIds=[vpc_id])
    else:
        vpcs = ec2.describe_vpcs()

    # save the results to a local file called vpcs.json
    with open('vpcs.json', 'w') as f:
        json.dump(vpcs, f)
    # loop around the vpcs and retirn the vpd_id for each vpc
    for vpc in vpcs['Vpcs']:
        print(vpc['VpcId'])
        # call get_subnets with the vpcID
        get_subnets(vpc['VpcId'])
        #print(vpc['CidrBlock'])
        #print(vpc['IsDefault'])
        #print(vpc['InstanceTenancy'])
        #print(vpc['State'])
        #print(vpc['Tags'])
        #print(vpc['DhcpOptionsId'])
        #print(vpc['VpcEndpointIds'])


    # create a file called vpc.tf




    return vpcs

def  get_subnets(vpc_id):
    ec2 = boto3.client('ec2')
    subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    # save the results to a local file called subnets.json
    with open('subnets.json', 'w') as f:
        json.dump(subnets, f)
    return subnets

def  get_all_vpcs():
    vpcs = get_vpc()
    return vpcs



# add a __main__ function that calls get_all_vpcs # get the command line argments and pass the vpc id if it exists
# call get_all_vpcs and print the results to the screen

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--vpc_id', help='vpc id')
    args = parser.parse_args()
    if args.vpc_id:
        get_vpc(args.vpc_id)
    else:
        get_all_vpcs()

