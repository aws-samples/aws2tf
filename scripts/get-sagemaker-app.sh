#!/bin/bash
if [ "$1" == "" ]; then
    echo "domain must be set" 
    exit
fi
if [ "$2" == "" ]; then
    echo "user profile name must be set" 
    exit
fi

cmd[0]="$AWS sagemaker list-apps --domain-id-equals $1 --user-profile-name-equals $2"

pref[0]="Apps"
tft[0]="aws_sagemaker_app"
idfilt[0]="AppName"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        echo $awsout
        exit
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            appn=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")  
            appt=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].AppType")             
            domid=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].DomainId")
            upn=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].UserProfileName")
            cname=$($AWS sagemaker describe-app --domain-id $domid --user-profile-name $upn --app-type $appt --app-name $appn --query AppArn | jq -r .)
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

         
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            echo "$ttft $cname import"

            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            rm -f $fn

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
                    if [[ ${tt1} == "url" ]];then skip=1;fi
                    if [[ ${tt1} == "home_efs_file_system_uid" ]];then skip=1;fi

                    if [[ ${t1} == *"resource_spec"* ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "$lbc $rbc $t1"
                            read line
                            t1=`echo "$line"`
                            if [[ $rbc -eq $lbc ]]; then breq=1; fi
                        done 
                    fi

                    if [[ ${tt1} == "domain_id" ]];then 
                                skip=0;
                                did=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`          
                                t1=`printf "domain_id = aws_sagemaker_domain.%s.id" $did`
                    fi
                    if [[ ${tt1} == "single_sign_on_managed_application_instance_id" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"            
        done
    fi
done

rm -f *.backup 



#