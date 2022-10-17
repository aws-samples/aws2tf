#!/bin/bash
if [[ "$1" != "" ]]; then
    cmd[0]="$AWS cognito-identity get-identity-pool-roles --identity-pool-id $1"
else
    echo "must pass an identity pool id exiting ..."
    exit
fi

pref[0]=""
tft[0]="aws_cognito_identity_pool_roles_attachment"
idfilt[0]="IdentityPoolId"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm You don't have access for this resource"
        exit
    fi
    count=1

    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq -r ".${idfilt[(${c})]}"`
                # get the user pool name

            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"

            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
    
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt
            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess > $fn
            tarn=""
      

            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
         
                    if [[ ${tt1} == "id" ]];then skip=1;fi
                    if [[ ${tt1} == "arn" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "last_modified_date" ]];then skip=1;fi
                    if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                    if [[ ${tt1} == "estimated_number_of_users" ]];then skip=1;fi  
                    if [[ ${tt1} == *"authenticated"* ]];then 
                        tarn=$(echo $tt2 | tr -d '"')
                        tid=$(echo $tarn | rev | cut -f1 -d'/' | rev)
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $tid`
                    fi
                                     

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [[ $tid != "" ]];then
                    ../../scripts/050-get-iam-roles.sh $tarn
            fi

        done
    fi 
done

#rm -f t*.txt

