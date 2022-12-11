#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
ttft="aws_efs_file_system_policy"
pref="AccessKeyMetadata"
idfilt="FileSystemId"

cm="$AWS efs describe-file-system-policy --file-system-id $1"
if [[ "$1" != "" ]]; then  
    if [[ ${1} != "fs-"* ]]; then   
        echo "must provide a fs- id as a parameter"
        exit   
    fi
else
    echo "must provide a fs id as a parameter"
    exit   
fi


count=1
echo $cm
awsout=`eval $cm 2> /dev/null`
if [[ $? -ne 0 ]];then exit;fi


#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi   
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`
#echo $awsout | jq .
for i in `seq 0 $count`; do
    #echo $i

    cname=`echo $awsout | jq -r ".${idfilt}"`
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt
    tfa=`printf "%s.%s" $ttft $rname`
    terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
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

            if [[ ${tt1} == "Resource" ]];then 
                tt2=$(echo $tt2 | tr -d '"')
                if [[ "$tt2" == *"arn:aws:elasticfilesystem:${myreg}:${mysub}:file-system/"* ]];then
                        echo "--> here"
                        tarn=$(echo $tt2)
                        fsi=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'` 
                        #rn=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                        if [[ "$tarn" != "$cname" ]];then ## to stop - Error: Self-referential block
                                t1=`printf "%s = aws_efs_file_system.%s.arn" $tt1 $fsi`
                        fi
                fi
            fi


        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here
done

#rm -f t*.txt

