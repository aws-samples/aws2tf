#!/bin/bash
# $AWS  organizations list-organizational-units-for-parent --parent-id $root
echo "*** sub org ou ***"
if [ "$1" != "" ]; then
    cmd[0]="$AWS  organizations list-organizational-units-for-parent --parent-id $1" 
    
else
    echo "must specify parent org"
    exit 
fi

pref[0]="OrganizationalUnits"
tft[0]="aws_organizations_organizational_unit"
idfilt[0]="Id"


c=0
#rm -f ${tft[0]}.tf

    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "This is either not an AWS organizations account or you don't have access"
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

            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`

            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
            printf "}"  >> $ttft.$rname.tf
            printf "terraform import %s.%s %s" $ttft $rname "$cname" > data/import_$ttft_$rname.sh
            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$rname.tf

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

                    if [[ ${tt1} == "status" ]];then skip=1;fi
                    if [[ ${tt1} == "joined_method" ]];then skip=1;fi
                    if [[ ${tt1} == "joined_timestamp" ]];then skip=1;fi
                    if [[ ${tt1} == "accounts" ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "$lbc $rbc $t1"

                            if [[ $rbc -eq $lbc ]]; then 
                                breq=1; 
                            else
                                read line
                                t1=`echo "$line"`
                            fi
                        done 
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn

                fi
                
            done <"$file"

            if [[ "${cname}" != "" ]]; then
                ../../scripts/get-suborg-ou.sh $cname
            fi
        done

    fi

rm -f t*.txt

