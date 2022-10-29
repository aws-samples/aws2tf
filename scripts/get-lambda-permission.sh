#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
#echo "globe vars $myreg $mysub"
if [ "$1" != "" ]; then
    pat=$($AWS lambda get-policy --function-name $1 | jq .Policy | tr -d '\\' | tr -d '"')
else
    echo "must supply a finction name"
    exit
fi

echo $pat | grep 'Sid:' > /dev/null
if [[ $? -ne 0 ]];then
    echo "Found no statement id for $1 exiting ..."
    exit
fi


tft[0]="aws_lambda_permission"
perms=()
# got to count how many - yukk
count=0
echo $pat | grep 'Sid:' > /dev/null
while [ $? -eq 0 ];do
    pat=${pat#*Sid:}
    tp=$(echo $pat | cut -f1 -d',')

    perms+=$(printf "\"%s\" " $tp)
    count=`expr $count + 1`
    echo $pat | grep 'Sid:' > /dev/null
done
c=0
ttft=${tft[(${c})]}
#echo $count

for perm in ${perms[@]}; do
            cname=$(echo $perm | tr -d '"')          
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

                    if [[ ${tt1} == "function_name" ]];then 
                        tfn=$(echo "$tt2" | rev | cut -d':' -f1 | rev | tr -d '"')
                                                    
                        t1=`printf "%s = aws_lambda_function.%s.arn" $tt1 $1`
                    fi

                    if [[ ${tt1} == "source_account" ]];then 
                        tacc=`echo $tt2 | tr -d '"'` 
                        tsub="%s"
                        if [[ "$mysub" == "$tacc" ]];then
                            t1=$(printf "%s = data.aws_caller_identity.current.account_id" $tt1)
                        fi
                    fi

                    if [[ ${tt1} == "source_arn" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ ${tt2} == "arn:aws:events:"* ]];then
                                tstart=$(echo $tt2 | cut -f1-3 -d ':')
                                treg=$(echo $tt2 | cut -f4 -d ':')
                                tacc=$(echo $tt2 | cut -f5 -d ':')
                                tend=$(echo $tt2 | cut -f6- -d ':')
                                tsub="%s"
                                if [[ "$mysub" == "$tacc" ]] && [[ "$mysub" == "$tacc" ]];then
                                    t1=$(printf "%s = format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tsub $tend)
                                fi
                            fi
                        fi

                # else
                    #
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
           
done # for cname


rm -f t*.txt

