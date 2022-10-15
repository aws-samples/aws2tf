#!/bin/bash
if [ "$1" != "" ]; then
    if [[ "$1" == "port-"* ]]; then
        cmd[0]="$AWS servicecatalog describe-portfolio --id $1"
        pref[0]="PortfolioDetail"

    else
        echo "must pass a portfolio id"
        exit
    fi
else
    cmd[0]="$AWS servicecatalog list-portfolios"
    pref[0]="PortfolioDetails"
fi
c=0
cm=${cmd[$c]}


tft[0]="aws_servicecatalog_portfolio"
idfilt[0]="Id"



for c in `seq 0 0`; do
 
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
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
            if [ "$1" != "" ]; then
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi

            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #cat $tfa.json | jq .

            rm -f $ttft.$cname.tf
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
                    if [[ ${tt1} == "created_time" ]];then skip=1;fi              

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            echo "$cname principals"
            ../../scripts/get-sc-portfolio-principal.sh $cname
            echo "$cname constraints"
            ../../scripts/get-sc-portfolio-constraints.sh $cname
            echo "$cname products"
            ../../scripts/get-sc-portfolio-products.sh $cname
        done # end for

    fi
done

rm -f t*.txt

