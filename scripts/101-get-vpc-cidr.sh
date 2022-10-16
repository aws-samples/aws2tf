#!/bin/bash
if [ "$1" ]; then
    cmd[0]="$AWS ec2 describe-vpcs --filters \"Name=vpc-id,Values=$1\"" 
else
    cmd[0]="$AWS ec2 describe-vpcs"
fi
#echo $cmd[0]
pref[0]="Vpcs[].CidrBlockAssociationSet"
tft[0]="aws_vpc_ipv4_cidr_block_association"
idfilt[0]="AssociationId"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=0
    #echo $awsout
    for i in `echo $awsout | jq ".${pref[(${c})]} | length"`
    do
      count=$((count+1))
    done
    #echo $awsout | jq .
    #
    #echo "vpc cidr count=$count"
    if (test $count -gt 0); then
    #echo "count:${count}"
        count=`expr ${count} - 1`
        for i in `seq 0 $count`; do
            basecidr=`echo $awsout | jq ".Vpcs[0].CidrBlock"`
            thiscidr=`echo $awsout | jq ".${pref[(${c})]}[(${i})].CidrBlock| select( . != null )"`
            #echo "basecidr:$basecidr thiscidr:$thiscidr"
            for x in $thiscidr
            do
                #echo "basecidr:$basecidr cname:$x"
                if [ $basecidr != $x ]; then
                    #echo "test jq: $c $count"
                    #echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"
                    cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
                    #echo "cname:$cname"
                    for y in $cname; do
                        #echo "ttft: $ttft cname:$y"
                        if [[ $y == "null" ]];then
                            echo "null value if vpc cidr block skipping"
                            continue
                        fi
                        fn=`printf "%s__%s.tf" $ttft $y`
                        if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

                        printf "resource \"%s\" \"%s\" {" $ttft $y > $ttft.$y.tf
                        printf "}" $y >> $ttft.$y.tf
                        terraform import $ttft.$y "$y" | grep Import
                        terraform state show -no-color $ttft.$y > t1.txt
                        tfa=`printf "data/%s.%s" $ttft $y`
                        terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
                        #echo $awsj | jq . 
                        rm $ttft.$y.tf

                        file="t1.txt"
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
                                if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                                #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                                if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                                if [[ ${tt1} == "vpc_id" ]]; then
                                    tt2=`echo $tt2 | tr -d '"'`
                                    t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                                fi
                        
                            fi
                            if [ "$skip" == "0" ]; then
                                #echo $skip $t1
                                echo "$t1" >> $fn
                            fi
                       
                        done <"$file"
                    done
                fi
            done
        done
    fi
done

rm -f t*.txt

