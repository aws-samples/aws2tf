#!/bin/bash
ttft="aws_efs_file_system"
pref="FileSystems"

idfilt="FileSystemId"
cm="$AWS efs describe-file-systems"
if [[ "$1" != "" ]]; then  
    if [[ ${1} == "arn:aws:elasticfilesystem"* ]]; then
        idfilt="FileSystemArn"
    fi
    cm=`printf "$AWS efs describe-file-systems  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
fi
idfilt="FileSystemId"

fsid=()
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
    fsid+=$(echo "$cname ")
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
 
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
            if [[ ${tt1} == "dns_name" ]];then skip=1;fi 
            if [[ ${tt1} == "number_of_mount_targets" ]];then skip=1;fi 

            if [[ ${tt1} == "kms_key_id" ]]; then    
                        kmsarn=$(echo $tt2 | tr -d '"')            
                        if [[ $tt2 != *":alias/aws/"* ]]; then
                            kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`   
                            km=`$AWS kms describe-key --key-id $kid --query KeyMetadata.KeyManager | jq -r '.' 2>/dev/null`
                        else
                            kid=`echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"'`
                            kid=${kid//\//_}
                            km="ALIAS"
                        fi                         
      
                        if [[ $km == "AWS" ]];then
                            t1=`printf "%s = data.aws_kms_key.k_%s.arn" $tt1 $kid`
                        elif [[ $km == "ALIAS" ]];then               
                            t1=`printf "%s = data.aws_kms_alias.%s.arn" $tt1 $kid`
                        else
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`
                        fi 
            fi


            if [[ ${tt1} == "size_in_bytes" ]];then
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

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"



    if [[ "$kmsarn" != "" ]]; then 
                ../../scripts/080-get-kms-key.sh $kmsarn
    fi

    ../../scripts/get-efs-policy.sh $cname
#    ../../scripts/get-efs-ap-fsid.sh $cname
#    ../../scripts/get-efs-mt.sh $cname


    # dependancies here
done
#for fsi in ${fsid[@]}; do
#    echo $fsi
#    ../../scripts/get-efs-ap-fsid.sh $fsi
#done

#rm -f t*.txt

