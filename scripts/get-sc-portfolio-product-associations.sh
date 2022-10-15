#!/bin/bash
if [[ "$1" == "prod-"* ]]; then
        cmd[0]="$AWS servicecatalog list-portfolios-for-product --product-id $1"
        

    else
        echo "must pass a product id"
        exit
    fi

c=0
cm=${cmd[$c]}

tft[0]="aws_servicecatalog_product_portfolio_association"

pref[0]="PortfolioDetails"
idfilt[0]="Id"

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
            terraform import $ttft.${rname}__${1} "en:${cname}:${1}" | grep Import
         
            terraform state show -no-color $ttft.${rname}__${1} > t1.txt

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
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "created_time" ]];then skip=1;fi
                                
                    if [[ ${tt1} == "portfolio_id" ]];then 
                        portid=$(echo $tt2 | tr -d '"')
                        t1=$(printf "%s = aws_servicecatalog_portfolio.%s.id" $tt1 $portid)
                    fi 

                    if [[ ${tt1} == "product_id" ]];then 
                        pid=$(echo $tt2 | tr -d '"')
                        
                        # .product__portfolio
                        t1=$(printf "%s = aws_servicecatalog_product.%s__%s.id" $tt1 $pid $rname)
                    fi 
             

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            if [[ "$portid" != "" ]];then
                ../../scripts/get-sc-portfolio-products.sh $portid
            fi
            
        done # end for

    fi
done

rm -f t*.txt

