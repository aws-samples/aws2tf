#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS codepipeline list-pipelines | jq '.pipelines[] | select(.name==\"${1}\")'" 
else
    cmd[0]="$AWS codepipeline list-pipelines"
fi

pref[0]="pipelines"
tft[0]="aws_codepipeline"
idfilt[0]="name"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=1
    if [ "$1" == "" ]; then
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" == "" ]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
            else
                cname=`echo $awsout | jq -r ".${idfilt[(${c})]}"`
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$cname.tf

            file="t1.txt"
            echo $aws2tfmess > $fn
            trole=""
            rarns=()
            allowid=0
            doned=0
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    #echo $tt2
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then 
                        if [ "$allowid" == "0" ]; then
                            skip=1
                        else
                            earn=`echo "$tt2" | rev | cut -d'/' -f 1 | rev | tr -d '"'`
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $earn`
                        fi       
                    fi          

                    if [[ ${tt1} == "role_arn" ]];then 
                                skip=0;
                                trole=`echo "$tt2" | rev | cut -d'/' -f 1 | rev | tr -d '"'`
                                #echo "***trole=$trole"
                                rarns+=`printf "\"%s\" " $trole`
                                if [ "$doned" == "0" ]; then
                                    echo "depends_on = [aws_iam_role.$trole]" >> $fn  
                                    doned=1 
                                fi           
                                t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi

                    if [[ ${tt1} == "location" ]];then 
                                skip=0;
                                s3buck=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                                t1=`printf "%s = aws_s3_bucket.b_%s.id" $tt1 $s3buck`
                    fi
                    
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "rule_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                else
                    if [[ "$t1" == *"encryption_key"* ]]; then
                        allowid=1
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            #echo "rarns=$rarns"
            ## role arn

            #if [[ "$trole" != "" ]]; then
            #    echo "call1 for $trole"
            #    ../../scripts/050-get-iam-roles.sh $trole
            #fi


            for therole in ${rarns[@]}; do
                #echo "therole=$therole"
                trole1=`echo $therole | tr -d '"'`
                echo "for $trole1"
                if [[ "$trole1" != "" ]]; then
                    #echo "calling for $trole1"
                    ../../scripts/050-get-iam-roles.sh $trole1
                fi
            done           
            if [[ "$s3buck" != "" ]]; then
                ../../scripts/060-get-s3.sh $s3buck
            fi
            
        done
        
    fi
done

rm -f t*.txt

