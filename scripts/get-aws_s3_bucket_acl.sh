#!/bin/bash
if [ "$1" == "" ]; then echo "must specify bucket name" && exit; fi
c=0
tft[0]="aws_s3_bucket_acl"
ttft=${tft[(${c})]}

#echo $i
cname=`echo $1`
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
rname=`printf "b_%s" $rname`
echo "$ttft $rname"

fn=`printf "%s__%s.tf" $ttft $rname`
st=`printf "%s__%s.tfstate" $ttft $rname`
if [ -f "$fn" ] ; then echo "$fn exists already skipping" && exit; fi
if [ -f "$st" ] ; then echo "$st exists already skipping" && exit; fi
            
printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn
sync
        #printf "terraform import %s.%s %s" $ttft $rname $cname > data/import_$ttft_$rname.sh
#echo "s3 $cname acl import"    
cmdi=`printf "terraform import -state %s %s.%s %s > /dev/null" $st $ttft $rname $cname`      
#echo $cmdi
eval $cmdi
#terraform import -allow-missing-config -lock=false -state $st $ttft.$rname $cname &> /dev/null       
if [[ $? -ne 0 ]];then
    echo "retry import .."
    terraform import -state $st $ttft.$rname $cname   
    if [[ $? -ne 0 ]];then
                echo "** No bucket acl found for $cname exiting ..."
                mv $fn data/$fn.notfound
                exit
    fi
fi
sleep 2
rm -f $fn
        #echo "s3 policy show"   
s3acl=$(terraform state show -state $st $ttft.$rname  2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
if [[ $? -ne 0 ]];then
            echo "No bucket acl found for $rname exiting ..."
            mv $fn data/$fn.failed
            exit
fi
#echo "ACL Len=${#s3acl}"
vl=${#s3acl}
if [[ $vl -eq 0 ]];then
    echo "sleep 5 & retry for $ttft $rname"
    sleep 5
    s3acl=$(terraform state show -state $st $ttft.$rname  2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
    #echo "ACL Len=${#s3acl}"
    vl=${#s3acl}
    if [[ $vl -eq 0 ]];then
        echo "Second sleep 5 & retry for $ttft $rname"
        sleep 5
        s3acl=$(terraform state show -state $st $ttft.$rname  2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
        #echo "ACL Len=${#s3acl}"
        vl=${#s3acl}
        if [[ $vl -eq 0 ]];then
            echo "** Error Zero state $ttft $rname exiting...."
            rm -f $fn
            exit
        fi
    fi
fi
rm -f $fn
      
#echo $aws2tfmess > $fn
skipid=1
echo "$s3acl" | while IFS= read -r line
do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
  

                    if [[ ${tt1} == "id" ]];then 
                        if [[ "$skipid" == "1" ]];then
                            skip=1; 
                            skipid=0
                        fi
                    fi
 

                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "resource_owner" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "rotation_enabled" ]];then skip=1;fi
                    if [[ ${tt1} == "display_name" ]];then skip=1;fi
                    if [[ ${tt1} == "acl" ]];then skip=1;fi

                    if [[ ${tt1} == *":"* ]];then
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "bucket" ]];then
                        tt1=`echo $tt1 | tr -d '"'`
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s=aws_s3_bucket.b_%s.id" $tt1 $tt2`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi               
done





