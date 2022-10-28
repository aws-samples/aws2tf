#!/bin/bash
ttft="aws_launch_configuration"
pref="LaunchConfigurations"
idfilt="LaunchConfigurationName"

cm="$AWS autoscaling describe-launch-configurations"
if [[ "$1" != "" ]]; then
    cm=`printf "$cm  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
fi

count=1
echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=`echo $awsout | jq ".${pref} | length"`; fi   
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`
for i in `seq 0 $count`; do
    #echo $i
    if [[ "$1" != "" ]]; then
        cname=`echo $awsout | jq -r ".${idfilt}"`
    else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
    $AWS autoscaling describe-launch-configurations --launch-configuration-names $cname | jq .LaunchConfigurations[0].UserData | tr -d '"' | base64 --decode > $cname.sh
 
    file="t1.txt"
    echo $aws2tfmess > $fn
    while IFS= read t1
    do
		skip=0
        if [[ ${t1} == *"="* ]];then
            tt1=`echo "$t1" | cut -f1 -d'=' | tr -d ' '` 
            tt2=`echo "$t1" | cut -f2- -d'='`             
            if [[ ${tt1} == "id" ]];then 
                skip=1;
                printf "lifecycle {\n" >> $fn
                printf "   create_before_destroy = true\n" >> $fn
                printf "   ignore_changes = [user_data]\n" >> $fn
                printf "}\n" >> $fn
            
            fi  
            if [[ ${tt1} == "arn" ]];then skip=1;fi
            if [[ ${tt1} == "vpc_classic_link_security_groups" ]];then skip=1;fi
            if [[ ${tt1} == "name" ]];then 
                namp=`echo $tt2 | tr -d '"|,'`
                #t1=`printf "name_prefix = \"%s\"" $namp`
            fi  

            if [[ ${tt1} == "iam_instance_profile" ]];then 
                iip=`echo $tt2 | tr -d '"|,'`
                t1=`printf "$tt1 = aws_iam_instance_profile.%s.id" $iip`
            fi 



            if [[ ${tt1} == "user_data" ]];then 
                skip=0
                        
                if [[ -f ${cname}.sh ]];then 
                    #echo "user data via file ${cname}.sh"
                    t1=`printf "user_data = file(\"%s.sh\")" $cname`
                fi
            fi                  
        
        else
            if [[ "$t1" == *"sg-"* ]]; then
                sgid=`echo $t1 | tr -d '"|,'`
                t1=`printf "aws_security_group.%s.id," $sgid`
            fi
               
        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here
    if [[ $sgid != "" ]];then
        ../../scripts/110-get-security-group.sh $sgid
    fi
     if [[ $iip != "" ]];then
        ../../scripts/056-get-instance-profile.sh $iip
    fi   

done

#rm -f t*.txt

