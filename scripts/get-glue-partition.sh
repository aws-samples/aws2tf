#!/bin/bash
if [[ "$1" == "" ]]; then
    echo "must specify catalog id"
    exit
fi
if [[ "$2" == "" ]]; then
    echo "must specify database name"
    exit
fi
if [[ "$3" == "" ]]; then
    echo "must specify tablee name"
    exit
fi

cmd[0]="$AWS glue get-partitions  --catalog-id $1 --database-name $2 --table-name $3"
pref[0]="Partitions"

#if [[ "$4" != "" ]]; then
#    cmd[0]="$AWS glue get-partition --catalog-id $1 --database-name $2 --table-name $3 --partition-values $4"
#    pref[0]="Partition"
#else
#    cmd[0]="$AWS glue get-partitions  --catalog-id $1 --database-name $3 --table-name $3"
#    pref[0]="Partitions"
#fi

idfilt[0]="Values"
tft[0]="aws_glue_partition"

#pks=$(cat $tfa.json | jq .values.partition_keys)
#pcount=`echo $pks | jq ". | length"`
#if [ "$pcount" -gt "0" ]; then
#    pcount=`expr $pcount - 1`
#    for i in `seq 0 $pcount`; do
#        tp=`echo $pks | jq -r ".[(${i})].name"`
#        echo "partition=$tp"
#        ../../scripts/get-glue-partition.sh $catid $dbnam $rname $tp
#    done
 #fi


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi

    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo "found $count partitions"
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i

            cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}[(${c})]"`
            catid=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].CatalogId"`
            dbnam=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].DatabaseName"`
            tbnam=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].TableName"`
            #echo "cname=$cname"
            #echo $awsout | jq -r ".${pref[(${i})]}[(${i})]"
            
 
            
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname//&/_}
            echo "$ttft c__${catid}__${dbnam}__${tbnam}__${cname}"
            fn=`printf "%s__c__%s__%s__%s__%s.tf" $ttft $catid ${dbnam} ${tbnam} $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"c__%s__%s__%s__%s\" {}" $ttft $catid $dbnam ${tbnam} $rname > $fn
            
    
            terraform import $ttft.c__${catid}__${dbnam}__${tbnam}__${rname} "${catid}:${dbnam}:${tbnam}:${cname}" | grep Import
            terraform state show -no-color $ttft.c__${catid}__${dbnam}__${tbnam}__${rname} > t1.txt

            rm -f $fn


            file="t1.txt"
            fl=$(cat $file | wc -l)
            if [[ $fl -eq 0 ]]; then echo "** Empty State show for $dbname ${tbnam} $rname skipping" && continue; fi
            
            echo $aws2tfmess > $fn
            tarn=""
            inttl=0
            doneatt=0
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ "$t1" == *"ttl"* ]]; then inttl=1; fi
                if [[ "$t1" == "}" ]]; then inttl=0; fi

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`             
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_time" ]];then skip=1;fi
                    if [[ ${tt1} == "last_accessed_time" ]];then skip=1;fi
                    if [[ ${tt1} == *"grokPattern"* ]];then skip=1;fi
                fi

                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
        

        done
    fi 
done

#rm -f t*.txt

