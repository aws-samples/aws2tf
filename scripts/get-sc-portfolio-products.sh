#!/bin/bash

if [[ "$1" == "port-"* ]]; then
    cmd[0]="$AWS servicecatalog search-products-as-admin --portfolio-id $1"
#elif [[ "$1" == "prod-"* ]];then
#    cmd[0]="$AWS servicecatalog search-products-as-admin | jq -r '. | select(.ProductViewDetails[].ProductViewSummary.ProductId==\"${1}\")'"
else
    echo "must pass a portfolio id or product id"
    exit
fi

c=0
cm=${cmd[$c]}

tft[0]="aws_servicecatalog_product"
pref[0]="ProductViewDetails"
idfilt[0]="ProductViewSummary.ProductId"

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
    echo "product count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
        #for i in `seq 0 0`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}") # product id
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname $1"
     
            awsout2=$($AWS servicecatalog  describe-product-as-admin --id ${cname} --source-portfolio-id $1)     

            paname=$(echo $awsout2 | jq -r .ProductViewDetail.ProductViewSummary.Name)
            paids=$(echo $awsout2 | jq .ProvisioningArtifactSummaries)
            jcount=$(echo $awsout2 | jq ".ProvisioningArtifactSummaries | length")


            if [ "$jcount" -gt "0" ]; then
                jcount=`expr $jcount - 1`
                    for j in `seq 0 $jcount`; do
                        #echo "paids $j"
                        #echo $paids | jq ".[(${j})].Id"
                        cname2=$(echo $paids | jq -r ".[(${j})].Id") # provisioning id
                        rname2=${cname2//:/_} && rname2=${rname2//./_} && rname2=${rname2//\//_}
                        #echo "cname2=$cname2"
                        awsout3=$($AWS servicecatalog describe-provisioning-artifact --provisioning-artifact-id $cname2 --product-name "${paname}")
                        #echo "awsout3"
                        #echo $awsout3 | jq .

                        status=$(echo $awsout3 | jq .Status)
                        url=$(echo $awsout3 | jq .Info.TemplateUrl)
                        type=$(echo $awsout3 | jq .ProvisioningArtifactDetail.Type)

                        #echo "** status =$status,type=$type,url=$url"

                        fn=`printf "%s__%s__%s.tf" $ttft $rname $1`
                        if [ -f "$fn" ] ; then
                            echo "$fn exists already skipping"
                            continue
                        fi

                        printf "resource \"%s\" \"%s__%s\" {" $ttft $rname $1 > $fn
                        printf "}" >> $fn

                        #echo "# import product=$cname portfolio=$1 prodName=$paname"

                        terraform import $ttft.${rname}__${1} "${cname}" | grep Import
                    
                        terraform state show -no-color $ttft.${rname}__${1} > t1.txt
                        #tfa=`printf "data/%s.%s__%s" $ttft $rname $1`
                        #terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
                        #cat $tfa.json | jq .

                        rm -f $fn
                
                        #	for k in `cat t1.txt`; do
                        #		echo $k
                        #	done
                        file="t1.txt"

                        echo $aws2tfmess > $fn
                        #echo "# import product=$cname portfolio=$1 prodName=$paname"  >> $fn
                        while IFS= read line
                        do
                            skip=0
                            # display $line or do something with $line
                            t1=`echo "$line"` 
                          
                            if [[ ${t1} == *"="* ]];then
                                tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                tt2=`echo "$line" | cut -f2- -d'='`
                                if [[ ${tt1} == "arn" ]];then skip=1; fi                
                                if [[ ${tt1} == "id" ]];then 
                                    skip=1; 
                                    printf "provisioning_artifact_parameters {\n" >> $fn 
                                    printf "template_url = %s\n" "$url" >> $fn
                                    printf "}\n"       >> $fn 
                                    printf "lifecycle {\n" >> $fn
                                    printf "   ignore_changes = [provisioning_artifact_parameters,accept_language]\n" >> $fn
                                    printf "}\n" >> $fn
                                    printf "accept_language=\"en\"\n" >> $fn
                                fi
                                if [[ ${tt1} == "created_time" ]];then skip=1;fi         
                                if [[ ${tt1} == "status" ]];then skip=1; fi 
                                if [[ ${tt1} == "has_default_path" ]];then skip=1; fi
                                if [[ ${tt1} == "template_url" ]];then 
                                    echo "type = \"CLOUD_FORMATION_TEMPLATE\"" >> $fn
                                fi
                            fi
                            if [ "$skip" == "0" ]; then
                                #echo $skip $t1
                                echo "$t1" >> $fn
                            fi
                            
                        done <"$file"
                done # for j
            fi # if jcount
        # get product assiciations
        echo "Product $cname portfolio associations"
        ../../scripts/get-sc-portfolio-product-associations.sh ${cname}
        done # end for i

    fi
done

rm -f t*.txt

