#!/usr/bin/python3
import sys
import subprocess
import os
import json
import argparse
import sys


def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol=len(out.stdout.decode().rstrip())
    el=len(out.stderr.decode().rstrip())
    if el!=0:
        errm=out.stderr.decode().rstrip()
        if "Resource already managed by Terraform" not in errm:
            print("Error from command " + str(cmd))
            print(errm)  
            exit() 
        else:
            print(errm)

    # could be > /dev/null
    #if ol==0:
    #    print("No return from command " + str(cmd) + " exit ...")
    
    #print(out.stdout.decode().rstrip())
    return out


pref="Vpcs"
ttft="aws_vpc"
idfilt="VpcId"


if sys.version_info<(3,8,0):
  sys.stderr.write("You need python 3.8 or later to run this script\n")
  exit(1)


nargs=len(sys.argv)
#print('Argument List:', str(sys.argv))
#print('Argument 1:', sys.argv[0])
if nargs==1:
    cmd="$AWS ec2 describe-vpcs"
elif nargs==2:
    id=str(sys.argv[1])
    cmd="$AWS ec2 describe-vpcs --vpc-ids "+ id
else:
    print("error: too many args")
    exit()
print(cmd)
out=rc(cmd)

js=json.loads(out.stdout.decode().rstrip())
#print(json.dumps(js, indent=4, separators=(',', ': ')))
awsout=js[pref]

#print(json.dumps(awsout, indent=4, separators=(',', ': ')))
count=len(awsout)
#print(count)
if count > 0:
    for i in range(0,count):
        cname=awsout[i][idfilt]
        print(cname)
        rname=cname.replace(":","_")
        rname=rname.replace(".","_")
        rname=rname.replace("\\","_")
        rname=rname.replace(" ","_")
        #print(rname)
        fn=ttft+"__"+rname+".tf"
        #print(fn)
# exists ?
        if os.path.isfile(fn):
            print(fn+" exists continuing..")
            continue
        print(ttft+" "+cname+" import")



       

        fr=open(fn, 'w', closefd=True)
        fr.write('resource ' + ttft + ' "' + rname  + '" {}\n')
        fr.close()
        
        cmd ='terraform import '+ttft+'.'+rname+' "' + cname+ '"'
        rc(cmd)

        fnt=ttft+'__'+rname+'.txt'
        cmd ='terraform state show -no-color '+ttft+'.'+rname+' > '+fnt
        state=rc(cmd)
        print(state)
        print(fnt)
        fr=open(fn, 'w')

        with open(fnt) as file:
            while (line := file.readline().rstrip()):
                skip=0
                #print(line)
                if "=" in line:
                    tt1=line.split("=")[0].replace('"','').strip()
         
                    tt2=line.split("=")[1].strip()
                    #print(tt1+"/"+tt2)
                    if tt1=="arn": skip=1
                    if tt1=="id": skip=1
                    if tt1=="role_arn": skip=1
                    if tt1=="allocated_capacity": skip=1
                    if tt1=="dhcp_options_id": skip=1
                    if tt1=="main_route_table_id": skip=1
                    if tt1=="default_security_group_id": skip=1
                    if tt1=="default_route_table_id": skip=1
                    if tt1=="owner_id": skip=1
                    if tt1=="default_network_acl_id": skip=1
                    if tt1=="ipv6_association_id": skip=1
                    if tt1=="ipv6_cidr_block": skip=1
                    if tt1 == "enable_classiclink": skip=1
                    if tt1 == "enable_classiclink_dns_support":skip=1

                    if tt1 == "ipv6_netmask_length":
                        tt2=tt2.replace('"','')
                        if tt2 == "0": skip=1

                #print("skip="+str(skip))
                if skip==0:
                    fr.write(line+'\n')
            # end while
        # end with
        fr.close()
        file.close()

        

exit()
