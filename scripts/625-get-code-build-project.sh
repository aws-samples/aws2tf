#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS codebuild list-projects | jq -r '.projects[] | select(.==\"${1}\")'"  
else
    cmd[0]="$AWS codebuild list-projects"
fi

pref[0]="projects"
tft[0]="aws_codebuild_project"
idfilt[0]="name"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=1
    if [ "$1" == "" ]; then
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" == "" ]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})]"`
            else
                cname=`echo $awsout`
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $ttft.$cname.tf
           
            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$cname" 2> /dev/null | grep 'Import '
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #
            #get the buildspec
            bspf=`printf "buildspec__%s__%s.json" $ttft $cname`
            cat data/${tfa}.json | jq -r .values.source[].buildspec > $bspf
            
            rm -f $ttft.$cname.tf

            mv t1.txt t1.txt.sav

            
            echo $aws2tfmess > $fn
            ecrr=""
            trole=""
            vpcid=""
            #echo "vpc cat"
            vpcid=$(cat data/$tfa.json | jq -r .values.vpc_config[0].vpc_id) 
            if [ "$vpcid" != "" ] && [ "$vpcid" != "null" ]; then
                ../../scripts/100-get-vpc.sh $vpcid
                ../../scripts/105-get-subnet.sh $vpcid
                ../../scripts/110-get-security-group.sh $vpcid
            fi

            mv t1.txt.sav t1.txt
            file="t1.txt"
            bspf=""
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

                    if [[ ${tt1} == "service_role" ]];then 
                                skip=0;
                                trole=`echo "$tt2" | rev | cut -d'/' -f 1 | rev | tr -d '"'`
                                #echo $trole
                                echo "depends_on = [aws_iam_role.$trole]" >> $fn              
                                t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
            
                    fi
                    if [[ ${tt2} == *"dkr.ecr"* ]]; then
                        ecrr=`echo $tt2 | cut -f2 -d '/' | tr -d '"'`
                        ecrr=`echo $ecrr | cut -f1 -d ':'`
                    fi

                    if [[ ${tt1} == "buildspec" ]]; then
                        if [[ ${tt2} == *"EOT"* ]]; then
                            t1="buildspec = <<EOT"
                        fi
                        tt2=`echo $tt2 | tr -d ' '`
                        #echo "---> $tt2"

                        if [[ "$tt2" == "jsonencode(" ]]; then
                            #echo "--- HERE ----"       
                            printf "buildspec = file(\"buildspec__%s__%s.json\")\n" $ttft $cname >> $fn
                     
                            skip=1
                            lbc=0
                            rbc=0
                            breq=0
                            
                            while [[ $breq -eq 0 ]];do 
                                if [[ "${t1}" == *"("* ]]; then lbc=`expr $lbc + 1`; fi
                                if [[ "${t1}" == *")"* ]]; then rbc=`expr $rbc + 1`; fi
                                #echo "$lbc $rbc $t1"
                                read line
                                t1=`echo "$line"`
                                if [[ $rbc -eq $lbc ]]; then breq=1; fi
                            done
                        fi
                    fi

                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "rule_id" ]];then skip=1;fi
                    if [[ ${tt1} == "concurrent_build_limit" ]];then 
                        cbl=`echo $tt2 | tr -d '"'`
                        if [[ "$cbl" == "0" ]];then
                            skip=1;
                        fi
                    fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    
                    if [[ ${tt1} == "encryption_key" ]]; then    
                        kmsarn=$(echo $tt2 | tr -d '"')            
                        if [[ $tt2 != *":alias/aws/"* ]]; then
                            kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`   
                            km=`$AWS kms describe-key --key-id $kid --query KeyMetadata.KeyManager | jq -r '.' 2>/dev/null`
                        else
                            kid=`echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"'`
                            kid=${kid//\//_}
                            km="ALIAS"
                        fi                         
      
                        if [[ $km == "AWS" ]];then
                            t1=`printf "%s = data.aws_kms_key.k_%s.arn" $tt1 $kid`
                        elif [[ $km == "ALIAS" ]];then               
                            t1=`printf "%s = data.aws_kms_alias.%s.arn" $tt1 $kid`
                        else
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`
                        fi 
                    fi                  
                    
                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi

                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    t1=${t1//$/&} 
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [[ "$ecrr" != "" ]]; then 
                ../../scripts/get-ecr.sh $ecrr
            fi

            if [[ "$kmsarn" != "" ]]; then 
                ../../scripts/080-get-kms-key.sh $kmsarn
            fi
            ## role arn

            if [[ "$trole" != "" ]]; then
                #echo "*** $trole - from codebuildprof"
                ../../scripts/050-get-iam-roles.sh $trole
            fi

        done
        
    fi
done

rm -f t*.txt

