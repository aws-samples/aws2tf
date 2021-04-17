#!/usr/bin/python3
import sys
import subprocess
import os
import json
import argparse
import sys

pref="Vpcs"
ttft="aws_vpc"
idfilt="VpcId"


if sys.version_info<(3,6,0):
  sys.stderr.write("You need python 3.6 or later to run this script\n")
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



#out = subprocess.run('aws configure get region', shell=True, capture_output=True)
#region=out.stdout.decode().rstrip()
#print(region)

out = subprocess.run(cmd, shell=True, capture_output=True)
ol=len(out.stdout.decode().rstrip())
if ol==0:
    print("No return from command exit ...")
    exit()
print("ol="+str(ol))
print(out.stdout.decode().rstrip())


js=json.loads(out.stdout.decode().rstrip())
print(json.dumps(js, indent=4, separators=(',', ': ')))
awsout=js[pref]

print(json.dumps(awsout, indent=4, separators=(',', ': ')))
count=len(awsout)
print(count)
if count > 0:
    for i in range(0,count):
        cname=awsout[i][idfilt]
        print(cname)
        rname=cname.replace(":","_")
        rname=rname.replace(".","_")
        rname=rname.replace("\\","_")
        #print(rname)
        fn=ttft+"__"+rname+".tf"
        #print(fn)
        if os.path.isfile(fn):
            print(fn+" exists continuing..")
            continue
        print(ttft+" "+cname+" import")

        
        cmd ='terraform import '+ttft+'.'+rname+' "' + cname+ '" > /dev/null'
        print(cmd)
        out = subprocess.run(cmd, shell=True, capture_output=True)
        ol=len(out.stdout.decode().rstrip())
        if ol==0:
            print("No return from command exit ...")
            exit()
        print("ol="+str(ol))
        print(out.stdout.decode().rstrip())

        cmd ='terraform state show '+ttft+'.'+rname+' > '+ttft+'-'+rname+'-2.txt'
        print(cmd)
        out = subprocess.run(cmd, shell=True, capture_output=True)
        ol=len(out.stdout.decode().rstrip())
        if ol==0:
            print("No return from command exit ...")
            exit()
        print("ol="+str(ol))
        print(out.stdout.decode().rstrip())

        cmd ="cat "+ttft+"-"+rname+"-2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > "+ttft+"-"+rname+"-1.txt"
        print(cmd)
        out = subprocess.run(cmd, shell=True, capture_output=True)
        ol=len(out.stdout.decode().rstrip())
        if ol==0:
            print("No return from command exit ...")
            exit()
        print("ol="+str(ol))
        print(out.stdout.decode().rstrip())

        file=ttft+'-'+rname+'-1.txt'
        print(file)
        

exit()
"""
            
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"`
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "allocated_capacity" ]];then skip=1;fi
                    if [[ ${tt1} == "dhcp_options_id" ]];then skip=1;fi
                    if [[ ${tt1} == "main_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_security_group_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"
   

            dfn=`printf "data/data_%s__%s.tf" $ttft $cname`
            printf "data \"%s\" \"%s\" {\n" $ttft $cname > $dfn
            printf "id = \"%s\"\n" $cname >> $dfn
            printf "}\n" $ttft $cname >> $dfn
            
        done
    fi
done

rm -f *.backup
"""