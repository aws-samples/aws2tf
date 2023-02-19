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


if sys.version_info<(3,7,0):
  sys.stderr.write("You need python 3.7 or later to run this script\n")
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
        #print(rname)
        fn=ttft+"__"+rname+".tf"
        #print(fn)
        if os.path.isfile(fn):
            print(fn+" exists continuing..")
            continue
        print(ttft+" "+cname+" import")


# exists ?
       

        fr=open(fn, 'w')
        fr.write('resource ' + ttft + ' "' + rname  + '" {}\n')
        fr.close()
        
        cmd ='terraform import '+ttft+'.'+rname+' "' + cname+ '"'
        rc(cmd)

        fnt=ttft+'__'+rname+'.txt'
        cmd ='terraform state show -no-color '+ttft+'.'+rname+' > '+fnt
        rc(cmd)

        print(fn)
        fr=open(fn, 'w')

        with open(fnt) as file:
            while (line := file.readline().rstrip()):
                print(line)


        fr.close()

        

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
                    echo "$t1" >> $fn
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