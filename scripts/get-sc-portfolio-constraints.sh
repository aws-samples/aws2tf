#!/bin/bash

if [[ "$1" == "port-"* ]]; then
        cmd[0]="$AWS servicecatalog list-constraints-for-portfolio --portfolio-id $1"
else
    echo "must pass a portfolio id"
    exit
fi

c=0
cm=${cmd[$c]}

tft[0]="aws_servicecatalog_constraint"
pref[0]="ConstraintDetails"
idfilt[0]="ConstraintId"

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
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname $1"
            fn=`printf "%s__%s__%s.tf" $ttft $rname $1`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi

            printf "resource \"%s\" \"%s__%s\" {" $ttft $rname $1 > $fn
            printf "}" >> $fn
            terraform import $ttft.${rname}__${1} "${cname}" | grep Import
         
            terraform state show -no-color $ttft.${cname}__${1} > t1.txt
            #tfa=`printf "data/%s.%s__%s" $ttft $rname $1`
            #terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #cat $tfa.json | jq .

            rm -f $fn
    
            file="t1.txt"
            trole=""
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
                    if [[ ${tt1} == "created_time" ]];then skip=1;fi
                    if [[ ${tt1} == "owner" ]];then skip=1; fi         
                    if [[ ${tt1} == "status" ]];then skip=1; fi 

                    if [[ ${tt1} == "portfolio_id" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        t1=$(printf "%s = aws_servicecatalog_portfolio.%s.id" $tt1 $tt2)
                    fi 

                    if [[ ${tt1} == "product_id" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        t1=$(printf "%s = aws_servicecatalog_product.%s__%s.id" $tt1 $tt2 $1)
                    fi

                    if [[ ${tt1} == "RoleArn" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":iam:"* ]]; then
                            trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev)
                            t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                        fi                 
                    fi 

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [[ "$trole" != "" ]];then
                ../../scripts/050-get-iam-roles.sh $trole
            fi
            
        done # end for

    fi
done

rm -f t*.txt

