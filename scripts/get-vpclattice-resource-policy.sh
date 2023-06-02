#!/bin/bash
ttft="aws_vpclattice_resource_policy"
pref="items"
idfilt="policy"

if [[ "$1" != "" ]]; then
    if [[ "$1" == "s"* ]]; then
        cm=$(printf "$AWS vpc-lattice get-resource-policy  --resource-identifier $1")
    fi
else
    echo "must pass identifier svc-* or sn-* as a parameter"
    exit
fi

count=1
#echo $cm
awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : Empty or You don't have access for this resource" && exit; fi
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)
for i in $(seq 0 $count); do
    #echo $i
    cname=$(echo $1)
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    fn=$(printf "%s__%s.tf" $ttft $rname)
    
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    pf=$(printf "%s__%s.json" $ttft $rname)
    aws vpc-lattice get-auth-policy  --resource-identifier $1 | jq -r .policy | jq . > $pf 

    printf "resource \"%s\" \"%s\" {}" $ttft $rname >$fn
    terraform import $ttft.${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.${rname} >t1.txt

    rm -f $fn

    file="t1.txt"
    echo $aws2tfmess >$fn
    while IFS= read t1; do
        skip=0
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$t1" | cut -f2- -d'=')
            if [[ ${tt1} == "id" ]]; then skip=1; fi
            if [[ ${tt1} == "create_date" ]]; then skip=1; fi
            if [[ ${tt1} == "arn" ]]; then skip=1; fi
  

            if [[ ${tt1} == "resource_arn" ]]; then
                ri=$(echo $tt2 | tr -d '"')
                if [[ "$ri" == "svc-"* ]];then
                    t1=$(printf "$tt1 = aws_vpclattice_service.%s.arn" $ri)
                fi
                if [[ "$ri" == "sn-"* ]];then
                    t1=$(printf "$tt1 = aws_vpclattice_service_network.%s.arn" $ri)
                fi
            fi


        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here

done

#rm -f t*.txt
