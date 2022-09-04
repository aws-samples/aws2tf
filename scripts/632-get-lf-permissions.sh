#!/bin/bash
pref[0]="PrincipalResourcePermissions"
tft[0]="aws_lakeformation_permissions"
idfilt[0]="DataLakePrincipalIdentifier"
c=0

# on input:
prin=`echo $1 | awk -F'LakeFormation-' '{print $2}' | awk -F'::arn:' '{print $1}'`
#

if [ "$1" != "" ]; then
    cmd[0]="$AWS lakeformation list-permissions | jq '.PrincipalResourcePermissions[] | select(.Principal.${idfilt[(${c})]}==\"${prin}\")'" 
else
    cmd[0]="$AWS lakeformation list-permissions" 
fi


cm=${cmd[$c]}
ppls=()
ppls+=`eval $cm`
echo $ppls

c=0
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
    cm=`echo "$cm $ia"`
	echo $cm
    awsout=`eval $cm`
    if [ "$awsout" == "" ];then
        echo "This is not an AWS organizations account"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi

    echo $count
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".Principal.${idfilt[(${c})]}" | tr -d '"'` 
                perms=`echo $awsout | jq ".Permissions[]"` 
                permg=`echo $awsout | jq ".PermissionsWithGrantOption[]"`
                dbn=`echo $awsout | jq ".Resource.Database.Name"`
                dbc=`echo $awsout | jq ".Resource.Database.CatalogId"`
                dla=`echo $awsout | jq ".Resource.DataLocation.ResourceArn"`
                dlc=`echo $awsout | jq ".Resource.DataLocation.CatalogId"`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Principal.${idfilt[(${c})]}" | tr -d '"'`
                prin=`echo $cname`
                perms=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Permissions[]"` 
                permg=`echo $awsout | jq ".${pref[(${c})]}[(${i})].PermissionsWithGrantOption[]"`
                dbn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Resource.Database.Name"`
                dbc=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Resource.Database.CatalogId"`
                dla=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Resource.DataLocation.ResourceArn"`
                dlc=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Resource.DataLocation.CatalogId"`
            fi
                    
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
       
            rname=$(printf "%s__%s"  $ttft $rname)
            fn=`printf "not-imported/%s__%s.tf" $ttft $rname`
            #echo $fn
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            
            printf "resource \"%s\" \"%s\" {\n" $ttft $rname > $fn
            printf "principal=\"%s\"\n" $prin >> $fn
            oldstr="\" \""
            newstr="\",\""

            perms=$(echo $perms | sed "s/$oldstr/$newstr/g")
            permg=$(echo $permg | sed "s/$oldstr/$newstr/g")


            #permissions = ["CREATE_TABLE", "ALTER", "DROP"]
            printf "permissions = [%s]\n" $perms >> $fn
            if [[ $permg != "" ]];then
                printf "permissions_with_grant_option = [%s]\n" $permg >> $fn
            fi
            
            if [[ $dbn != "null" ]];then
                printf "database {\n" >> $fn
                printf "name = %s\n" $dbn >> $fn
                printf "catalog_id = %s\n" $dbc >> $fn
                printf "}\n" >> $fn
            fi
            #database {
            #    name       = aws_glue_catalog_database.example.name
            #    catalog_id = "110376042874"
            #}

            # permissions_with_grant_option -
            if [[ $dla != "null" ]];then
                printf "data_location {\n" >> $fn
                printf "arn = %s\n" $dla >> $fn
                printf "catalog_id = %s\n" $dlc >> $fn
                printf "}\n" >> $fn
            fi

            #data_location {
            #arn = aws_lakeformation_resource.example.arn
            #catlog_id = "628794301331"
            #}

            #lf_tag_policy {
            #    resource_type = "DATABASE"

            #    expression {
            #    key    = "Team"
            #    values = ["Sales"]
            #    }

            #    expression {
            #    key    = "Environment"
            #    values = ["Dev", "Production"]
            #    }
            # }


            printf "}\n"  >> $fn

            echo "***** Can't import Lakeformation permission ******"

            # output
            cat $fn

        done

        # get the role_arn if $prin is one


    fi
# init and validate not-imported ?


