#!/bin/bash
if [[ "$1" != "" ]]; then
        cmd[0]="$AWS cloudformation describe-stack-resources --stack-name $1"
        pref[0]="StackResources"       
    else
        cmd[0]="$AWS cloudformation list-stacks"
        pref[0]="StackSummaries"
fi

c=0
cm=${cmd[$c]}

tft[0]="aws_cloudformation_stack"
idfilt[0]="StackName"


for c in `seq 0 0`; do
 
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$1" != "" ]]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`        
    fi
    #echo $awsout | jq .
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            $AWS cloudformation get-template --stack-name $cname > cft__$rname.json
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $rname`
            tfs=`printf "%s__%s.txt" $ttft $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi

            if [[ "$1" != "" ]]; then
                sstatus=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].ResourceStatus")
            else
                sstatus=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].StackStatus")
            fi
            if [[ "$sstatus" != "CREATE_COMPLETE" ]]; then
                echo "Stack $cname status=$sstatus skipping ..."
                continue
            fi

            printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn
 
            terraform import $ttft.${rname} "${cname}" | grep Import
         
            terraform state show -no-color $ttft.${rname} > $tfs 

            rm -f $fn

            file=$(echo $tfs)

            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"$"* ]];then
                    t1=${t1//$/&}       
                fi
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then 
                        t1=`printf "template_url = file(\"cft__%s.json\")" $rname`
                    fi          
                    if [[ ${tt1} == "created_time" ]];then skip=1;fi
                    if [[ ${tt1} == "Description" ]];then 
                        tt2=$(echo $tt2 | sed 's/^"//')
                        tt2=$(echo $tt2 | sed 's/"$//')
                        #tt2=${tt2//\\/\\\\}
                        #tt2=${tt2//%\{/%%\{}
                        tt2=$(echo $tt2 | sed 's/"/\\"/g')
                        t1=`printf "%s = \"%s\"" $tt1 "$tt2"`
                    tt2=$(echo $tt2 | sed 's/"/\\"/g')
                    skip=1;
                    fi
                    # skip block
                    if [[ ${tt1} == "outputs" ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "op=$lbc $rbc $t1"
                            if [[ $rbc -eq $lbc ]]; then 
                                breq=1; 
                            else
                                read line
                                t1=`echo "$line"`
                            fi
                        done 
                    fi

                    if [[ ${tt1} == "template_body" ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"("* ]] || [[ "${t1}" == *"<<-EOT"* ]]; then lbc=`expr $lbc + 1`; fi
                            t1=`echo $t1 | tr -d ' '`
                            if [[ "${t1}" == *")"* ]] || [[ "${t1}" == "EOT" ]];then rbc=`expr $rbc + 1`; fi
                            #echo "tb=$lbc $rbc $t1"
                            if [[ $rbc -eq $lbc ]]; then 
                                breq=1; 
                                #echo "breaking tb"
                            else
                                read line
                                t1=`echo "$line"`
                            fi
                        done 
                    fi



                    #if [[ ${tt1} == *":"* ]];then
                    #    tt2=${tt2//$/&} 
                    #    tt1=`echo $tt1 | tr -d '"'`
                    #    echo "$tt1 --- $tt2"
                    #    t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                    #fi
                    if [[ ${tt1} == *"/"* ]];then
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\" = %s" $tt1 "$tt2"`
                    fi
                    #template_body = file("example.yml")


                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            
        done # end for

    fi
done

#rm -f t*.txt

