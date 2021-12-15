#!/bin/bash
if [ "$1" == "" ]; then echo "must specify bucket name" && exit; fi
ttft="aws_s3_bucket_policy"

#echo $i
cname=`echo $1`
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
echo "$ttft $rname"
            
fn=`printf "%s__%s.tf" $ttft $rname`
        if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                exit
        fi
        printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
        printf "}" >> $fn
        printf "terraform import %s.%s %s" $ttft $rname $cname > data/import_$ttft_$rname.sh
              
        cmdi=`printf "terraform import %s.%s %s" $ttft $rname $cname | grep Import`
        eval $cmdi
            
        cmds=`printf "terraform state show %s.%s > t2.txt" $ttft $rname`
        eval $cmds

        rm $fn
        cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt

        file="t1.txt"
        terraform state show aws_s3_bucket_policy.ds-data-lake-029e33c5a105 | grep = | grep policy > /dev/null
        if [[ $? -eq 0 ]];then


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
 

                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "resource_owner" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "rotation_enabled" ]];then skip=1;fi


                    if [[ ${tt1} == *":"* ]];then
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
        else
            echo "No bucket policy found for $1 skipping ..."
        fi # grep


rm -f t*.txt

