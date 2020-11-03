#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ecr describe-repositories --repository-names \"$1\"" 
else
    cmd[0]="$AWS ecr describe-repositories"
fi

pref[0]="repositories"
tft[0]="aws_ecr_repository"
idfilt[0]="repositoryName"

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
            rname=${cname//:/_}
            rname=${rname//\//_}
            echo "cname=$cname"
            
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" $cname >> $fn
            printf "terraform import %s.%s %s" $ttft $rname $cname > import_$ttft_$rname.sh
            terraform import $ttft.$rname $cname
            terraform state show $ttft.$rname > t2.txt
            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $ttft.$rname.tf
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
                    if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "registry_id" ]];then skip=1;fi
                    if [[ ${tt1} == "repository_url" ]];then skip=1;fi                   
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
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

            ofn=`printf "output__%s__%s.tf" $ttft $rname`
            printf "output \"%s__%s__id\" {\n" $ttft $rname > $ofn
            printf "value = %s.%s.name\n" $ttft $rname >> $ofn
            printf "}\n" >> $ofn

            dfn=`printf "data/data_%s__%s.tf" $ttft $rname`
            printf "data \"%s\" \"%s\" {\n" $ttft $rname > $dfn
            printf "name = \"%s\"\n" $cname >> $dfn
            printf "}\n" >> $dfn
            
        done
        terraform fmt
        terraform validate
    fi
done

rm -f t*.txt

