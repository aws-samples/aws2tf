#!/bin/bash
if [[ "$1" == "" ]]; then
    echo "must specify catalog id"
fi
if [[ "$2" == "" ]]; then
    echo "must specify database name"
fi

if [[ "$3" != "" ]]; then
    cmd[0]="$AWS glue get-table --database-name $2 --name $3"
    pref[0]="Table"
else
    cmd[0]="$AWS glue get-tables --database-name $2"
    pref[0]="TableList"
fi

idfilt[0]="Name"
tft[0]="aws_glue_catalog_table"


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$3" != "" ]]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [[ "$3" != "" ]]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}"`
                catid=`echo $awsout | jq -r ".${pref[(${c})]}.CatalogId"`
                dbnam=`echo $awsout | jq -r ".${pref[(${c})]}.DatabaseName"`
            else
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
                catid=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].CatalogId"`
                dbnam=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].DatabaseName"`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname//&/_}
            echo "$ttft c__${catid}__${dbnam}__${cname}"
            fn=`printf "%s__c__%s__%s__%s.tf" $ttft $catid ${dbnam} $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"c__%s__%s__%s\" {}" $ttft $catid $dbnam $rname > $fn
            
    
            terraform import $ttft.c__${catid}__${dbnam}__${rname} "${catid}:${dbnam}:${cname}" | grep Import
            terraform state show -no-color $ttft.c__${catid}__${dbnam}__${rname} > t1.txt
            tfa=`printf "%s.c__%s__%s__%s" $ttft $catid $dbnam $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json

            rm -f $fn
           

            file="t1.txt"
            fl=$(cat $file | wc -l)
            if [[ $fl -eq 0 ]]; then echo "** Empty State show for $dbname $rname skipping" && continue; fi
            
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
                    # these are difficult to process so skip for now
                    if [[ ${tt1} == *"grokPattern"* ]];then 
                       
                        tt2=$(echo $tt2 | sed 's/^"//')
                        tt2=$(echo $tt2 | sed 's/"$//')
                        tt2=${tt2//\\/\\\\}
                        tt2=${tt2//%\{/%%\{}
                        tt2=$(echo $tt2 | sed 's/"/\\"/g')
                        
                        t1=`printf "\"grokPattern\" = \"%s\"" "$tt2"`
                    fi
                    
                    if [[ ${tt1} == *"input.format"* ]];then 
                    
                        tt2=$(echo $tt2 | sed 's/^"//')
                        tt2=$(echo $tt2 | sed 's/"$//')
                        tt2=${tt2//\\/\\\\}
                        tt2=${tt2//%\{/%%\{}
                        tt2=$(echo $tt2 | sed 's/"/\\"/g')
                        t1=`printf "\"input.format\" = \"%s\"" "$tt2"`
                    
                    fi
                    if [[ ${tt1} == *"input.regex"* ]];then 
                    
                        tt2=$(echo $tt2 | sed 's/^"//')
                        tt2=$(echo $tt2 | sed 's/"$//')
                        tt2=${tt2//\\/\\\\}
                        tt2=${tt2//%\{/%%\{}
                        tt2=$(echo $tt2 | sed 's/"/\\"/g')
                        t1=`printf "\"input.regex\" = \"%s\"" "$tt2"`           
                    
                    fi
                    if [[ ${tt1} == "type" ]];then 
                        tt2=`echo "$tt2" | tr -d '"'`
                        tt2=${tt2//\\/\\\\}
                        if [[ ${tt2} == *"struct"* ]];then 
                            tt2=$(echo $tt2 | sed 's/^ //')
                                #r1=$(echo $RANDOM | md5sum | head -c 20; echo;)
                                #gn=`printf "glue-var-%s.tf" $r1`
                                #printf "variable \"g-%s\" {\n" $r1 > $gn
                                #printf "    type = string \n" >> $gn
                                #printf "    default = \"%s\" \n" $tt2 >> $gn
                                #printf "}\n" >> $gn
                                #t1=`printf "type = var.g-%s" $r1`
                            t1=`printf "type = \"%s\"" "$tt2"`
                        fi
                    fi
                fi

                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            # get the partitons
            ../../scripts/get-glue-partition.sh $catid $dbnam $rname
            
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
       

        done # for i
    fi 
done # for c

#rm -f t*.txt

