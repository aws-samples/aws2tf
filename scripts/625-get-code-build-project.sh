#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS codebuild list-projects" 
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
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})]" | tr -d '"'`
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > import_$ttft_$cname.sh
            terraform import $ttft.$cname $cname
            terraform state show $ttft.$cname > t2.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq .
            
            rm $ttft.$cname.tf
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            mv t1.txt t1.txt.sav
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
            
            echo $aws2tfmess > $fn
            ecrr=""
            trole=""
            vpcid=""
            vpcid=$(cat $tfa.json | jq -r .values.vpc_config[0].vpc_id) 
            if [ "$vpcid" != "" ]; then
                ../../scripts/100-get-vpc.sh $vpcid
                ../../scripts/105-get-subnet.sh $vpcid
                ../../scripts/110-get-security-group.sh $vpcid
            fi

            mv t1.txt.sav t1.txt
            file="t1.txt"
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
                    fi
                    if [[ ${tt1} == "buildspec" ]]; then
                        if [[ ${tt2} == *"EOT"* ]]; then
                            t1="buildspec = <<EOT"
                        fi
                    fi


                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "rule_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    
                    if [[ ${tt1} == "encryption_key" ]]; then                 
                        earn=`echo "$tt2" | rev | cut -d'/' -f 1 | rev | tr -d '"'`
                        t1=`printf "%s = \"data.aws_kms_alias.%s.arn\"" $tt1 $earn`
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
                    echo $t1 >> $fn
                fi
                
            done <"$file"


            if [ "$ecrr" != "" ]; then 
                ../../scripts/get-ecr.sh $ecrr
            fi
            ## role arn
            if [ "$trole" != "" ]; then
                ../../scripts/050-get-iam-roles.sh $trole
            fi

        done
        
    fi
done
terraform fmt
terraform validate
rm -f t*.txt

