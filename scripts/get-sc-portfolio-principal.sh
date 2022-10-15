#!/bin/bash
if [[ "$1" == "port-"* ]]; then
        cmd[0]="$AWS servicecatalog list-principals-for-portfolio --portfolio-id $1"
        
    else
        echo "must pass a portfolio id"
        exit
    fi

c=0
cm=${cmd[$c]}

tft[0]="aws_servicecatalog_principal_portfolio_association"
idfilt[0]="PrincipalARN"
pref[0]="Principals"

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
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname $1"
            fn=`printf "%s__%s__%s.tf" $ttft $rname $1`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi

            printf "resource \"%s\" \"%s__%s\" {" $ttft $rname $1 > $fn
            printf "}" >> $fn

            #cname=principl, $1 = portfolioid

            terraform import $ttft.${rname}__${1} "en,${cname},${1}" | grep Import
         
            terraform state show -no-color $ttft.${rname}__${1} > t1.txt
            rm -f $fn
 
            file="t1.txt"
            trole=""
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
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "created_time" ]];then skip=1;fi

                    if [[ ${tt1} == "portfolio_id" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        t1=$(printf "%s = aws_servicecatalog_portfolio.%s.id" $tt1 $tt2)
                    fi      

                    if [[ ${tt1} == "principal_arn" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":iam:"* ]]; then
                            tarn=`echo $tt2 | tr -d '"'`
                            if [[ "$tarn" == *":user"* ]];then
                                trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev)
                                trole=${trole//:/_} && trole=${trole//./_} && trole=${trole//\//_}
                                t1=`printf "%s = aws_iam_user.%s.arn" $tt1 $trole`
                            fi
                            if [[ "$tarn" == *":role"* ]];then
                                trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev)
                                trole=${trole//:/_} && trole=${trole//./_} && trole=${trole//\//_}
                                t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                            fi
                        fi                 
                    fi


                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [[ "$trole" != "" ]];then
                if [[ "$tarn" == *":user"* ]];then
                    ../../scripts/030-get-iam-users.sh $tarn
                fi
                if [[ "$tarn" == *":role"* ]];then
                    ../../scripts/050-get-iam-roles.sh $tarn
                fi
            fi
            

            
        done # end for
        if [[ "$1" == *"port-"* ]]; then
                #echo "--- HERE --- $1"
                ../../scripts/810-get-sc-portfolio.sh $1
        fi

    fi
done

rm -f t*.txt

