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
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
            printf "terraform import %s.%s %s" $ttft $rname $cname > data/import_$ttft_$rname.sh
              
            cmdi=`printf "terraform import %s.%s %s" $ttft $rname $cname`
            echo $cmdi
            eval $cmdi
            
            cmds=`printf "terraform state show %s.%s > t2.txt" $ttft $rname`
            eval $cmds
            
            #tfa=`printf "data/%s.%s" $ttft $rname`
            #terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $fn
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
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

        

    


rm -f t*.txt

