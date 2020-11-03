#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS appmesh list-meshes --filters \"Name=vpc-id,Values=$1\"" 
else
    cmd[0]="$AWS appmesh list-meshes"
fi

pref[0]="meshes"
tft[0]="aws_appmesh_mesh"
idfilt[0]="meshName"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > import_$ttft_$cname.sh
            terraform import $ttft.$cname $cname
            terraform state show $ttft.$cname > t2.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $ttft.$cname.tf
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
                    if [[ ${tt1} == "mesh_owner" ]];then skip=1;fi
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

            # app mesh vs
            ../../scripts/361-get-appmesh-vs.sh $cname
            ../../scripts/362-get-appmesh-vr.sh $cname
            ../../scripts/363-get-appmesh-no.sh $cname
            
        done
        terraform fmt
        terraform validate
    fi
done

rm -f t*.txt

