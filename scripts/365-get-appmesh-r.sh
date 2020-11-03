#!/bin/bash
if [ "$2" != "" ]; then
    cmd[0]="$AWS appmesh list-routes --mesh-name $1 --virtual-router-name $2" 
else
    echo "Mesh and Virtual Router name must be set"
    exit
fi

pref[0]="routes"
tft[0]="aws_appmesh_route"
idfilt[0]="routeName"
echo "*************************"
echo $1 $2
#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo $cname
            rname=${cname//:/_}
            rname=${rname//./_}
            rname=${rname//\//_}
            echo "365 rname=$rname"

            fn=`printf "%s__%s__%s__%s.tf" $ttft $1 $2 $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s__%s__%s\" {" $ttft $1 $2 $rname > $ttft.$1__$2__$rname.tf
            printf "}" >> $ttft.$1__$2__$rname.tf
            printf "terraform import %s.%s__%s__%s %s/%s/%s" $ttft $1 $2 $rname $1 $2 $cname > import_$ttft_$1_$2_$rname.sh
            terraform import $ttft.$1__$2__$rname $1/$2/$cname
            terraform state show $ttft.$1__$2__$rname > t2.txt
            tfa=`printf "%s.%s__%s__%s" $ttft $1 $2 $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $ttft.$1__$2__$rname.tf
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
                    if [[ ${tt1} == "created_date" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "last_updated_date" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"

            
        done

    fi
done

rm -f t*.txt

