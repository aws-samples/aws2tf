#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS secretsmanager list-secret-version-ids --secret-id $1" 
else
    echo "must specify secret id"
    exit
fi

pref[0]="Versions"
tft[0]="aws_secretsmanager_secret_version"
idfilt[0]="VersionId"
sname=${1//:/_} && sname=${sname//./_} && sname=${sname//\//_}
#rm -f ${tft[0]}.tf
echo "get secret version ........"
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
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            sstring=`$AWS secretsmanager get-secret-value --secret-id $1 --version-id $cname --query SecretString`

                    
            echo "$ttft $sname $rname"
            
            rname=`printf "v-%s" $rname`
            fn=`printf "%s__%s__%s.tf" $ttft $sname $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s__%s\" {}\n" $ttft $sname $rname > $fn
            printf "terraform import %s.%s__%s '%s|%s'" $ttft $sname $rname $1 $cname > data/import_$ttft_$sname_$rname.sh
                 
            cmdi=`printf "terraform import %s.%s__%s '%s|%s'" $ttft $sname $rname $1 $cname`
         
          
            eval $cmdi
            #terraform import $ttft.$sname__$rname '$1|$cname' | grep Import
            
            cmds=`printf "terraform state show -no-color %s.%s__%s > t1.txt" $ttft $sname $rname`
            eval $cmds
            
            tfa=`printf "data/%s.%s__%s" $ttft $sname $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm -f $fn
           
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

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
  

                    if [[ ${tt1} == "id" ]];then 
                        skip=1; 
                        echo "lifecycle {" >> $fn
                        echo "ignore_changes = [secret_string]" >> $fn
                        echo "}" >> $fn
                    
                    fi
                    #if [[ ${tt1} == "name" ]];then 
                    #echo "recovery_window_in_days = 30" >> $fn
                    #fi

                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "resource_owner" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "version_id" ]];then skip=1;fi
                    if [[ ${tt1} == "secret_string" ]];then 
                        skip=0;
                
                        t1=`printf "%s = %s" "$tt1" "$sstring"`

                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"           
            cp t1.txt $tfa.txt
        done

    fi
done

rm -f t*.txt

