#!/usr/bin/python3
import json
import argparse
import common

def  aws_vpc():
    ttft="aws_vpc"
  ## VPC specific 
    rf=ttft+"_resources.out"
    tf2=ttft+".tf"
    skipipv6=False
    print("rw tf")
    f1 = open(rf, 'r')
    Lines = f1.readlines()
    with open(tf2, "w") as f2:
        for t1 in Lines:
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip()
            except:
                tt2=""
            if tt1 in "assign_generated_ipv6_cidr_block":
                if tt2 in "true": skipipv6=True
            if tt1 in "ipv6_cidr_block":
                if skipipv6: continue
            if tt1 in "ipv6_ipam_pool_id":
                if skipipv6: continue
            if tt1 in "ipv6_netmask_length":
                if skipipv6: continue
            f2.write(t1)
    f1.close()
    f2.close()
    
def aws_subnet():
    ttft="aws_aubnet"
    print(ttft+" fixtf")  







