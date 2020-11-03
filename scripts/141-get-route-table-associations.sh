#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-route-tables --filters \"Name=vpc-id,Values=$1\""
else
    cmd[0]="$AWS ec2 describe-route-tables"
fi
c=0
cm=${cmd[$c]}
echo $cm

pref[0]="RouteTables"
tft[0]="aws_route_table_association"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].RouteTableId" | tr -d '"'`
            echo $cname
            # get the subnet id
            # Inner loop associations
            awsout2=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Associations"`
            jcount=`echo $awsout2 | jq ". | length"`
            if [ "$jcount" -gt "0" ]; then
                jcount=`expr $jcount - 1`
                for j in `seq 0 $jcount`; do
                    ismain=`echo $awsout2 | jq ".[(${j})].Main" | tr -d '"'`
                    if [ $ismain == false ]; then
                        sname=`echo $awsout2 | jq ".[(${j})].SubnetId" | tr -d '"'`
                        #echo "sname= $sname"
                        #if [ "$sname" != "null" ]; then
                            cname=`echo $awsout2 | jq ".[(${j})].RouteTableAssociationId" | tr -d '"'`
                            rtbid=`echo $awsout2 | jq ".[(${j})].RouteTableId" | tr -d '"'`
                            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
                            printf "}" $cname >> $ttft.$cname.tf
                            terraform import $ttft.$cname $sname/$rtbid
                            terraform state show $ttft.$cname > t2.txt
                            rm $ttft.$cname.tf
                            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                            #	for k in `cat t1.txt`; do
                            #		echo $k
                            #	done
                            file="t1.txt"
                            fn=`printf "%s__%s.tf" $ttft $cname`
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
                                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                                    if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                                    #if [[ ${tt1} == "default_route_table_id" ]];then skip=1;fi
                                    #if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                                    if [[ ${tt1} == "route_table_id" ]]; then
                                        tt2=`echo $tt2 | tr -d '"'`
                                        t1=`printf "%s = aws_route_table.%s.id" $tt1 $tt2`
                                    fi
                                    if [[ ${tt1} == "subnet_id" ]]; then
                                        tt2=`echo $tt2 | tr -d '"'`
                                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                                    fi
                                else
                                    if [[ "$t1" == *"subnet-"* ]]; then
                                        t1=`echo $t1 | tr -d '"|,'`
                                        t1=`printf "aws_subnet.%s.id," $t1`
                                    fi                         
                                fi
                                if [ "$skip" == "0" ]; then
                                    #echo $skip $t1
                                    echo $t1 >> $fn
                                fi
                                
                            done <"$file"
                    fi
                    #else    
                    #    echo "association null subnetID"
                    #fi
                done
            fi
        done
        terraform fmt
        terraform validate
    fi
done

rm -f t*.txt

