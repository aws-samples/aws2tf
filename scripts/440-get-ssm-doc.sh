#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]=$(printf "$AWS ssm list-documents --filters \"Key=Owner,Values=Self\" | jq '.DocumentIdentifiers[] | select(.Name==\"%s\")'" $1)
    pref[0]="DocumentIdentifiers"
else
    cmd[0]="$AWS ssm list-documents --filters \"Key=Owner,Values=Self\""
    pref[0]="DocumentIdentifiers"
fi

tft[0]="aws_ssm_document"
idfilt[0]="Name"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    #echo $awsout | jq .
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=$(echo $awsout | jq -r ".${idfilt[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            echo "$ttft $cname"
            rnamec=`printf "%s" $cname`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            $AWS ssm get-document --name $rnamec > $rname.json
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn
            printf "terraform import %s.%s %s" $ttft $rname $cname > data/import_$ttft_$rname.sh
            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess > $fn
            sgs=()
            subnets=()
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
                    if [[ ${tt1} == "latest_version" ]];then skip=1;fi
                    if [[ ${tt1} == "owner" ]];then skip=1;fi
                    #if [[ ${tt1} == "last_modified" ]];then skip=1;fi
                    if [[ ${tt1} == "status" ]];then skip=1;fi
                    if [[ ${tt1} == "instance_type" ]];then skip=1;fi
                    if [[ ${tt1} == "version" ]];then skip=1;fi
                    if [[ ${tt1} == "schema_version" ]];then skip=1;fi
                    if [[ ${tt1} == "hash" ]];then skip=1;fi
                    if [[ ${tt1} == "hash_type" ]];then skip=1;fi
                    if [[ ${tt1} == "created_date" ]];then skip=1;fi
                    if [[ ${tt1} == "document_version" ]];then skip=1;fi
                    if [[ ${tt1} == "default_version" ]];then skip=1;fi
                    if [[ ${tt1} == "description" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                        skip=1
                    fi
                    if [[ ${tt1} == "role" ]];then 
                        rarn=`echo $tt2 | tr -d '"'` 
                        skip=0;
                        #trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                        trole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`
                                                    
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi

                   if [[ ${tt1} == "content" ]];then 
                        tt2=`echo $tt2 | tr -d '"'`
                        #echo "tt2=$tt2"
                        if [[ "$tt2" == *"EOT"* ]];then
                            bs="EOT"
                            es="EOT"
                        else
                            bs="("
                            es=")"                           
                        fi
                        echo "bs=$bs  es=$es"
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"${bs}"* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"${es}"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "$lbc $rbc $t1"
                            read line
                            t1=`echo "$line"`
                            if [[ ${bs} != "EOT" ]]; then
                                if [[ $rbc -eq $lbc ]]; then breq=1; fi
                            else
                                if [[ $lbc -eq 2 ]]; then breq=1; fi
                            fi

                        done 
                        #echo "**** out of content"
                        skip=0
                        t1=`printf "content = file(\"%s.json\")" $rname`
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [content]\n" >> $fn
                        printf "}\n" >> $fn

                    fi

                                                            
                    if [[ ${tt1} == "platform_types" ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "$lbc $rbc $t1"
                            read line
                            t1=`echo "$line"`
                            if [[ $rbc -eq $lbc ]]; then breq=1; fi
                        done 
                    fi
                    if [[ ${tt1} == "parameter" ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "$lbc $rbc $t1"
                            read line
                            t1=`echo "$line"`
                            if [[ $rbc -eq $lbc ]]; then breq=1; fi
                        done 
                    fi

                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        subnets+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        sgs+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [ "$trole" != "" ]; then
                ../../scripts/050-get-iam-roles.sh $trole
            fi
            if [ "$vpcid" != "" ]; then
                ../../scripts/100-get-vpc.sh $vpcid
            fi


            for sub in ${subnets[@]}; do
                #echo "therole=$therole"
                sub1=`echo $sub | tr -d '"'`
                echo "calling for $sub1"
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                fi
            done

            for sg in ${sgs[@]}; do
                #echo "therole=$therole"
                sg1=`echo $sg | tr -d '"'`
                echo "calling for $sg1"
                if [ "$sg1" != "" ]; then
                    ../../scripts/110-get-security-group.sh $sg1
                fi
            done 

        
        done

    fi
done


#rm -f t*.txt

