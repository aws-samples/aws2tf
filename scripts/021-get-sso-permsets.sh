#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS sso-admin list-permission-sets --instance-arn" 
else
    cmd[0]="$AWS sso-admin list-permission-sets --instance-arn" 
fi

pref[0]="PermissionSets"
tft[0]="aws_ssoadmin_permission_set"
idfilt[0]=""

c=0
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
    cm=`echo "$cm $ia"`
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "This is either not an AWS organizations account or you don't have access"
        exit
    fi




#rm -f ${tft[0]}.tf


# write the data files and refresh
echo 'data "aws_ssoadmin_instances" "sso" {}' > data__aws_ssoadmin_instances__sso.tf
#
#echo 'data "aws_identitystore_group" "sso" {' >> data__aws_ssoadmin_idstore__sso.tf
#echo '  identity_store_id = tolist(data.aws_ssoadmin_instances.sso.identity_store_ids)[0]' >> data__aws_ssoadmin_idstore__sso.tf

#echo '  filter {' >> data__aws_ssoadmin_idstore__sso.tf
#echo '    attribute_path  = "DisplayName"' >> data__aws_ssoadmin_idstore__sso.tf
#echo '    attribute_value = "ExampleGroup"' >> data__aws_ssoadmin_idstore__sso.tf
#echo '  }' >> data__aws_ssoadmin_idstore__sso.tf
#echo '}' >> data__aws_ssoadmin_idstore__sso.tf


echo "Refresh .."
terraform refresh -target=data.aws_ssoadmin_instances.sso> /dev/null
#terraform refresh -target=data.aws_identitystore_group.sso> /dev/null
ia=`terraform state show data.aws_ssoadmin_instances.sso | grep ':instance' | tr -d ',' | tr -d ' ' | jq -r `
#echo $ia
ria=${ia//:/_} && ria=${ria//./_} && ria=${ria//\//_}
#echo $ria
#terraform state show data.aws_identitystore_group.sso


    

    count=1    
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})]" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            #rname=$(printf "%s" $rname)
            rname=$(printf "%s__%s"  $rname $ria)

            echo "$ttft ${cname},${ia} import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            #echo $fn
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
            printf "}"  >> $ttft.$rname.tf
            printf "terraform import %s.%s %s" $ttft $rname "${cname},${ia}" > data/import_$ttft_$rname.sh
            terraform import $ttft.$rname "${cname},${ia}" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm $ttft.$rname.tf

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

                    if [[ ${tt1} == "status" ]];then skip=1;fi
                    if [[ ${tt1} == "created_date" ]];then skip=1;fi
                
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn

                fi
                
            done <"$file"

            echo "../../scripts/get-sso-man-pol-attach.sh $ia $cname"
            ../../scripts/get-sso-man-pol-attach.sh $ia $cname
            echo "../../scripts/get-sso-inline-pol-attach.sh $ia $cname"



# ------------------------------------------------------

            #echo "../../scripts/get-sso-acc-assignment.sh $ia $cname"
            # aws sso-admin list-accounts-for-provisioned-permission-set --instance-arn $ia --permission-set-arn $cname 
            # {
            #    "AccountIds": [
            #        "628794301331",
            #        "433146468867",
            #        "817339700138",
            #        "915259118275"
            #    ]
            #}





            # resource "aws_ssoadmin_account_assignment" "example" {
            # instance_arn       = data.aws_ssoadmin_permission_set.example.instance_arn
            # permission_set_arn = data.aws_ssoadmin_permission_set.example.arn

            # principal_id   = data.aws_identitystore_group.example.group_id
            # principal_type = "GROUP"

             #target_id   = "012347678910"
            # target_type = "AWS_ACCOUNT"
             # }

        done

    fi


rm -f t*.txt

