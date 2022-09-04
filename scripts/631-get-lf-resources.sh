#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS lakeformation list-resources | jq '.ResourceInfoList[] | select(.ResourceArn==\"${1}\")'" 
else
    cmd[0]="$AWS lakeformation list-resources" 
fi

pref[0]="ResourceInfoList"
tft[0]="aws_lakeformation_resource"
idfilt[0]="ResourceArn"

c=0
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
    cm=`echo "$cm $ia"`
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "This is not an AWS organizations account"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi

    #echo $count
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i

            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${idfilt[(${c})]}" | tr -d '"'` 
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`

            fi

            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
       
            rname=$(printf "data__%s__%s"  $tft $rname)
            fn=`printf "not-imported/%s__%s.tf" $ttft $rname`
            #echo $fn
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            
            printf "resource \"%s\" \"%s\" {\n" $ttft $rname > $fn
            printf "arn=\"%s\"\n" $cname >> $fn
            printf "}\n"  >> $fn

            # output

            echo "***** Can't import Lakeformation resource ******"
            #echo "Refresh .. data.$ttft.$rname"
            #terraform refresh -target=data.${ttft}.${rname} > /dev/null

        done

        # get the role_arn


    fi


