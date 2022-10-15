#!/bin/bash
# $AWS  organizations list-organizational-units-for-parent --parent-id $root
roots=()
if [ "$1" != "" ]; then
    cmd[0]="$AWS  organizations list-policies --filter" 
    
else
    cmd[0]="$AWS  organizations list-policies --filter"
fi

pref[0]="Policies"
tft[0]="aws_organizations_policy"
idfilt[0]="Id"


roots+="SERVICE_CONTROL_POLICY "
roots+="TAG_POLICY "
roots+="BACKUP_POLICY "
roots+="AISERVICES_OPT_OUT_POLICY "
#echo $roots

c=0
#rm -f ${tft[0]}.tf
for root in ${roots[@]}; do
    #echo $root
    
    cm=${cmd[$c]}
    cm=`echo "$cm $root"`
	ttft=${tft[(${c})]}
	#echo $cm
    
    
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "This is either not an AWS organizations account or you don't have access"
        exit
    fi
    count=1    
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            #rname=$(printf "a-%s" $rname)

            if [[ "$cname" ==  "p-FullAWSAccess" ]] ; then
                echo "skipping p-FullAWSAccess"
                continue
            fi

            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`

            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
            printf "}"  >> $ttft.$rname.tf
            printf "terraform import %s.%s %s" $ttft $rname "$cname" > data/import_$ttft_$rname.sh
            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$rname.tf

            file="t1.txt"
            iddo=0
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                #echo $t1

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi
                    if [[ ${tt1} == *":"* ]];then 
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                    fi
                    if [[ ${tt1} == *"@@"* ]];then
                        #echo "$tt2" 
                        printf "\"%s\" = %s" $tt1  "$tt2" > t1.tmp
                        t1=`cat t1.tmp`
                    fi

               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn

                fi
                
            done <"$file"

            ../../scripts/get-org-policy_attachment.sh $cname

        done

    fi
done

rm -f t*.txt

