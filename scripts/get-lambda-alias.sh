#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS lambda list-aliases --function-name $1"
    pref[0]="Aliases"
else
    echo "must supply a finction name"
    exit
fi

tft[0]="aws_lambda_alias"
idfilt[0]="Name"

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

    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i

            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$1/$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$cname.tf

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
                    if [[ ${tt1} == "last_modified" ]];then skip=1;fi
                    if [[ ${tt1} == "invoke_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "qualified_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "version" ]];then skip=1;fi
                    if [[ ${tt1} == "source_code_size" ]];then skip=1;fi

                    if [[ ${tt1} == "role" ]];then 
                        rarn=`echo $tt2 | tr -d '"'` 
                        skip=0;
                        #trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                        trole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`
                                                    
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi



                # else
                    #
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"



           
        done

    fi
done


rm -f t*.txt

