#!/bin/bash
# $AWS  organizations list-organizational-units-for-parent --parent-id $root
roots=()
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
	echo $cm
       
    awsout=`eval $cm`
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
            #rname=$(printf "a-%s" $rname)


            echo "$ttft $cname:$1 import"
            fn=`printf "%s__%s.tf" $ttft $rname`

            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
            printf "}"  >> $ttft.$rname.tf
            printf "terraform import %s.%s %s" $ttft $rname "$cname" > data/import_$ttft_$rname.sh
            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show $ttft.$rname > t2.txt
            tfa=`printf "data/%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $ttft.$rname.tf
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
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
                    if [[ ${tt1} == *":"* ]];then 
                        t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                    fi
                    if [[ ${tt1} == *"@@"* ]];then
                        #echo "$tt2" 
                        printf "\"%s\" = %s" $tt1  "$tt2" > t1.tmp
                        t1=`cat t1.tmp`
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

