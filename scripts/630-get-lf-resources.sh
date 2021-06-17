#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS lakeformation list-resources " 
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
    awsout=`eval $cm`
    if [ "$awsout" == "" ];then
        echo "This is not an AWS organizations account"
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
       
            rname=$(printf "data__%s__%s"  $tft $rname)
            fn=`printf "data__%s__%s.tf" $ttft $rname`
            #echo $fn
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            
            printf "data \"%s\" \"%s\" {\n" $ttft $rname > $fn
            printf "arn=\"%s\"\n" $cname >> $fn
            printf "}\n"  >> $fn

            # output

            
            echo "Refresh .. data.$ttft.$rname"
            terraform refresh -target=data.${ttft}.${rname} > /dev/null

        done

        # get the role_arn


    fi


