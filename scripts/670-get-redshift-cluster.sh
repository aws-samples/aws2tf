#!/bin/bash
ttft="aws_redshift_cluster"
pref="Clusters"
idfilt="ClusterIdentifier"

cm="$AWS redshift describe-clusters"
if [[ "$1" != "" ]]; then
    cm=`printf "$AWS redshift describe-clusters  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
fi

count=1
#echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=`echo $awsout | jq ".${pref} | length"`; fi   
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`
for i in `seq 0 $count`; do
    #echo $i
    if [[ "$1" != "" ]]; then
        cname=`echo $awsout | jq -r ".${idfilt}"`
    else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
    lroles=()
    file="t1.txt"
    echo $aws2tfmess > $fn
    while IFS= read t1
    do
		skip=0
        if [[ ${t1} == *"="* ]];then
            tt1=`echo "$t1" | cut -f1 -d'=' | tr -d ' '` 
            tt2=`echo "$t1" | cut -f2- -d'='`             
            if [[ ${tt1} == "id" ]];then skip=1; fi  
            if [[ ${tt1} == "create_date" ]];then skip=1; fi  
            if [[ ${tt1} == "arn" ]];then skip=1;fi
            if [[ ${tt1} == "owner_id" ]];then skip=1;fi 
            if [[ ${tt1} == "cluster_security_groups" ]];then skip=1;fi 
            if [[ ${tt1} == "dns_name" ]];then skip=1;fi 

            if [[ ${tt1} == "cluster_subnet_group_name" ]];then 
                csbn=`echo $tt2 | tr -d '"'`
                t1=`printf "%s = aws_redshift_subnet_group.%s.id" $tt1 $csbn`
            fi 


            if [[ ${tt1} == "cluster_nodes" ]];then
                        #echo "dns block" 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                        #while [[ "$t1" != "]" ]] ;do

                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
            fi  
            if [[ ${tt1} == "default_iam_role_arn" ]];then 
                rarn=`echo $tt2 | tr -d '"'` 
                skip=0;
                trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                                                    
                t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
            fi 

            if [[ ${tt1} == "kms_key_id" ]];then 
                kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                            
                kmsarn=$(echo $tt2 | tr -d '"')
                km=`$AWS kms describe-key --key-id $kid --query KeyMetadata.KeyManager | jq -r '.' 2>/dev/null`
                #echo "---> $km"
                if [[ $km == "AWS" ]];then
                    t1=`printf "%s = data.aws_kms_key.k_%s.arn" $tt1 $kid`
                else
                    t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`
                fi
                     
            fi

        else
            if [[ "$t1" == *"sg-"* ]]; then
                sgid=`echo $t1 | tr -d '"|,'`
                t1=`printf "aws_security_group.%s.id," $sgid`
            fi
            if [[ "$t1" == *"arn:aws:iam:"*":role/"* ]]; then
                        lrl=`echo $t1 | tr -d '"|,'`
                        lrl=`echo $lrl | rev | cut -f1 -d'/' | rev`
                        lroles+=`printf "\"%s\" " $lrl`
                        t1=`printf "aws_iam_role.%s.arn," $lrl`
            fi


        fi       

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"

    if [ "$trole" != "" ]; then
        ../../scripts/050-get-iam-roles.sh $trole
    fi

    if [ "$kmsarn" != "" ]; then
        #echo "getting key $kmsarn"
        ../../scripts/080-get-kms-key.sh $kmsarn
    fi

    if [[ $sgid != "" ]];then
        ../../scripts/110-get-security-group.sh $sgid
    fi

    if [ "$csbn" != "" ]; then
        ../../scripts/671-get-redshift-cluster-subnet.sh $csbn
    fi

    for therole in ${lroles[@]}; do
        #echo "therole=$therole"
        trole1=`echo $therole | tr -d '"'`
        echo "for $trole1"
        if [[ "$trole1" != "" ]]; then
            #echo "calling for $trole1"
            ../../scripts/050-get-iam-roles.sh $trole1
        fi
    done 
    # dependancies here
done

#rm -f t*.txt

