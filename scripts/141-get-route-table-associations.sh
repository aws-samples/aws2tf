#!/bin/bash
if [ "$1" != "" ]; then
    if [[ "$1" == "rtb"* ]]; then
        cmd[0]="$AWS ec2 describe-route-tables --filters \"Name=association.route-table-association-id,Values=$1\""
    else  
        cmd[0]="$AWS ec2 describe-route-tables --filters \"Name=vpc-id,Values=$1\""
    fi 
else
    cmd[0]="$AWS ec2 describe-route-tables"
fi
c=0
cm=${cmd[$c]}

pref[0]="RouteTables"
tft[0]="aws_route_table_association"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    #echo $awsout | jq .
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].RouteTableId" | tr -d '"'`
            #echo "inner cname=$cname"
            # get the subnet id
            # Inner loop associations
            awsout2=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Associations"`
            #echo $awsout2 | jq .
            jcount=`echo $awsout2 | jq ". | length"`
            #echo "jcount=$jcount"
            if [ "$jcount" -gt "0" ]; then
                jcount=`expr $jcount - 1`
                for j in `seq 0 $jcount`; do
                    ismain=`echo $awsout2 | jq ".[(${j})].Main" | tr -d '"'`
                    if [ $ismain == false ]; then
                            sname=`echo $awsout2 | jq ".[(${j})].SubnetId" | tr -d '"'`
                            cname=`echo $awsout2 | jq ".[(${j})].RouteTableAssociationId" | tr -d '"'`
                            rtbid=`echo $awsout2 | jq ".[(${j})].RouteTableId" | tr -d '"'`
                            
                            echo "$ttft $sname/$cname Import"
                            fn=`printf "%s__%s__%s.tf" $ttft $sname $cname`
                            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

                            printf "resource \"%s\" \"%s__%s\" {\n" $ttft $sname $cname > $fn
                            printf "}\n" >> $fn
                            #cat $fn
                            comm=$(printf "terraform import %s.%s__%s %s/%s | grep Import" $ttft $sname $cname $sname $rtbid) 
                            #echo $comm
                            eval $comm
                            #echo "state show"
                            comm=$(printf "terraform state show -no-color %s.%s__%s" $ttft $sname $cname) 
                            #echo $comm
                            eval $comm > t1.txt
                            rm $fn

                            file="t1.txt"
                            
                            echo $aws2tfmess > $fn
                            #cat $fn
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
                       
                                fi
                                if [ "$skip" == "0" ]; then
                                    #echo $skip $t1
                                    echo "$t1" >> $fn
                                
                                fi
                                
                            done <"$file"
                    fi
                    #else    
                    #    echo "association null subnetID"
                    #fi
                done
            fi
        done
    fi
done

rm -f t*.txt

