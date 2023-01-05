#!/bin/bash
if [ "$1" == "" ]; then echo "must specify bucket name" && exit; fi
c=0
tft[0]="aws_s3_bucket_versioning"
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
  
cmdi=`printf "terraform import -state %s %s.%s %s > /dev/null" $st $ttft $rname $cname`      
#echo $cmdi
    #terraform import -allow-missing-config -lock=false -state $st $ttft.$rname $cname &> /dev/null     
eval $cmdi 
if [[ $? -ne 0 ]];then
    echo "retry import"
    sleep 1;sync
    terraform import -state $st $ttft.$rname $cname
    if [[ $? -ne 0 ]];then
        echo "** No bucket versioning found for $cname exiting ..."
        mv $fn data/$fn.notfound
        exit
    fi
fi

rm -f $fn
sleep 2
o1=$(terraform state show -state $st $ttft.$rname 2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
if [[ $? -ne 0 ]];then
        echo "Show: No bucket versioning found for $rname exiting ..."
        mv $fn data/$fn.failed
        exit
fi
#echo "Vers Len=${#o1}"
vl=${#o1}
if [[ $vl -eq 0 ]];then
    echo "sleep 5 & retry for $ttft $rname"
    sleep 5
    o1=$(terraform state show -state $st $ttft.$rname 2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
        #echo "Vers Len=${#o1}"
    vl=${#o1}
    if [[ $vl -eq 0 ]];then
        echo "** Error: Zero state $ttft $rname exiting...."
        exit
    fi
fi

rm -f $fn


#echo $aws2tfmess > $fn
echo "$o1" | while IFS= read -r line
    do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                #echo $t1
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

                    if [[ ${tt1} == "bucket" ]];then
                        tt1=`echo $tt1 | tr -d '"'`
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s=aws_s3_bucket.b_%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == *":"* ]];then
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi                
done
 


