#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
if [ "$1" != "" ]; then
    cmd[0]="$AWS apigateway get-rest-api --rest-api-id $1"
else
    cmd[0]="$AWS apigateway get-rest-apis"
    pref[0]="items"
fi

tft[0]="aws_api_gateway_rest_api"
getp=0
for c in `seq 0 0`; do
 
    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1      
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
       
    fi

    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            echo $i
            # is it AWS Managed ?

            if [ "$1" != "" ]; then
                #cname=`echo $awsout | jq -r ".${pref[(${c})]}.id"`
                cname=`echo $awsout | jq -r ".id"`
                
            else
                #cname=`echo $awsout | jq -r ".id"`
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].id"`
            fi

            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
            fi

                echo "$ttft $cname"
                printf "resource \"%s\" \"%s\" {}" $ttft $cname > $fn

                terraform import $ttft.$cname $cname | grep Import
                terraform state show -no-color $ttft.$cname > t1.txt
                rm -f $fn
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

                        if [[ ${tt1} == "aws:"* ]]; then
                                tt2=`echo $tt2 | tr -d '"'`
                                t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                        fi

                        if [[ ${tt1} == "arn" ]];then skip=1; fi
                        if [[ ${tt1} == "id" ]];then skip=1; fi
                        if [[ ${tt1} == "created_date" ]];then skip=1; fi
                        if [[ ${tt1} == "execution_arn" ]];then skip=1; fi
                        if [[ ${tt1} == "root_resource_id" ]];then skip=1; fi
                        if [[ ${tt1} == "vpc_endpoint_ids" ]];then 
                            tt2=`echo $tt2 | tr -d '"'`
                            if [[ ${tt2} == "[]" ]];then
                                skip=1; 
                            fi
                        fi
                    fi
                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                        echo "$t1" >> $fn
                    fi
                    
                done <"$file"   # done while
                # depoyments - no import support
                #../../scripts/751-get-apigw-resource.sh $cname
        done # done for i
    fi
done


rm -f t*.txt

