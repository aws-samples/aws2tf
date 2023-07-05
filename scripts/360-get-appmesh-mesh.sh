#!/bin/bash
pref[0]="meshes"
tft[0]="aws_appmesh_mesh"
idfilt[0]="meshName"

if [ "$1" != "" ]; then
    cmd[0]=$(printf "$AWS appmesh list-meshes  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
else
    cmd[0]="$AWS appmesh list-meshes"
fi

#rm -f ${tft[0]}.tf

for c in $(seq 0 0); do

    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=$(eval $cm 2>/dev/null)
    #echo $awsout | jq .
    if [ "$awsout" == "" ]; then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=1
    if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
    if [[ "$1" == "" ]]; then count=$(echo $awsout | jq ".${pref} | length"); fi
    if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
    echo $count
    if [ "$count" -gt "0" ]; then
        count=$(expr $count - 1)
        for i in $(seq 0 $count); do
            #echo $i
            if [[ "$1" != "" ]]; then
                cname=$(echo $awsout | jq -r ".${idfilt}")
            else
                cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
            fi

            echo "$ttft $cname"
            fn=$(printf "%s__%s.tf" $ttft $cname)
            if [ -f "$fn" ]; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname >$fn
           
            #printf "terraform import %s.%s %s" $ttft $cname $cname >data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$cname" | grep Importing
            terraform state show -no-color $ttft.$cname >t1.txt

            #echo $awsj | jq .
            rm -f $fn

            file="t1.txt"
            #echo $aws2tfmess >$fn
            while IFS= read line; do
                skip=0
                # display $line or do something with $line
                t1=$(echo "$line")
                if [[ ${t1} == *"="* ]]; then
                    tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                    tt2=$(echo "$line" | cut -f2- -d'=')
                    if [[ ${tt1} == "arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "id" ]]; then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "resource_owner" ]]; then skip=1; fi
                    if [[ ${tt1} == "mesh_owner" ]]; then skip=1; fi
                    if [[ ${tt1} == "created_date" ]]; then skip=1; fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "last_updated_date" ]]; then skip=1; fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        t1=$(printf "%s = aws_vpc.%s.id" $tt1 $tt2)
                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >>$fn
                fi

            done <"$file"

            # app mesh vs
            ../../scripts/get-appmesh-vs.sh $cname
            ../../scripts/get-appmesh-vr.sh $cname
            ../../scripts/get-appmesh-no.sh $cname
            ../../scripts/get-appmesh-vgw.sh $cname
        done

    fi
done

rm -f t*.txt
