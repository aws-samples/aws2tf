#!/bin/bash
# $AWS  organizations list-organizational-units-for-parent --parent-id $root

if [ "$1" != "" ]; then
    cmd[0]="$AWS  organizations list-targets-for-policy --policy-id $1" 
    
else
    echo "must specify a policy id"
    exit
fi

pref[0]="Targets"
tft[0]="aws_organizations_policy_attachment"
idfilt[0]="TargetId"

c=0

    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
       
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "This is not an AWS organizations account"
        exit
    fi
    count=1    
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            rname=$(printf "att-%s" $rname)

            echo "$ttft $cname:$1 import"
            fn=`printf "%s__%s__%s.tf" $ttft $rname $1`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s__%s\" {\n" $ttft $rname $1 > $fn
            printf "}\n"  >> $fn
            printf "terraform import %s.%s__%s %s" $ttft $rname $1 "$cname":$1 > data/import_$ttft_$rname_$1.sh
            comm=`printf "terraform import %s.%s__%s \"%s:%s\"" $ttft $rname $1 $cname $1`
            eval $comm | grep Import
            #terraform import $ttft.$rname__$1 "$cname:$1" #| grep Import

            terraform state show -no-color ${ttft}.${rname}__${1} > t1.txt
            
            tfa=`printf "data/%s.%s__%s" $ttft $rname $1`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $fn
    
            file="t1.txt"
            iddo=0
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                #echo $t1

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi
                    if [[ ${tt1} == "policy_id" ]];then 
                        pid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_organizations_policy.%s.id" $tt1 $pid` 
                    fi

                    if [[ ${tt1} == "target_id" ]];then 
                        tid=`echo $tt2 | tr -d '"'`
                        if [[ ${tid} == "ou-"* ]];then
                            t1=`printf "%s = aws_organizations_organizational_unit.%s.id" $tt1 $tid` 
                        fi
                        if [[ ${tid} =~ ^[0-9]+$ ]];then
                            echo "tid=${tid}"
                            t1=`printf "%s = aws_organizations_account.a-%s.id" $tt1 $tid`
                        fi

                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn

                fi
                
            done <"$file"

        done

    fi


rm -f t*.txt

