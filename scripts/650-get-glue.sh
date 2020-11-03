cmd[0]="$AWS glue get-crawlers"
pref[0]="Crawlers"
tft[0]="aws_glue_crawler"
cmd[1]="$AWS glue get-jobs"
pref[1]="Jobs"
tft[1]="aws_glue_job"

for c in `seq 0 1`; do
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Name" | tr -d '"'`
            echo $cname
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            terraform import $ttft.$cname $cname
            terraform state show $ttft.$cname > t2.txt
            rm $ttft.$cname.tf
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
            file="t1.txt"
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"`
                
                if [[ ${t1} == *"arn"*"="* ]];then
				    #echo "in arn"
					skip=1
				fi
				
                if [[ ${t1} == *"id"*"="* ]];then
                    skip=1
                fi
				
                if [[ ${t1} == *"role_arn"*"="* ]];then skip=0;fi
                if [[ ${t1} == *"number_of_workers"*"="* ]];then skip=1;fi
				if [[ ${t1} == *"allocated_capacity"*"="* ]];then skip=1;fi

				if [ "$skip" == "0" ]; then
					#echo $skip $t1
					echo $t1 >> $ttft.$cname.tf
				fi
            done <"$file"
            
        done
    fi
done
rm -f t*.txt

