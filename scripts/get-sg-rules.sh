#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify sg exiting"
    exit
fi
if [ "$2" == "" ]; then
    echo "must specify subtype ingress or egress exiting"
    exit
fi

pref[0]="SecurityGroups"
tft[0]="aws_security_group_rule"
stype=`echo $2`
cname=`echo $1`

#fn=`printf "%s__%s_%s_%s.tf" $ttft $cname $stype $ir`

#if [ -f "$fn" ] ; then echo "$fn exists skipping" && continue; fi



terraform state show aws_security_group.$1 | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
c=0
ttft=${tft[(${c})]}

file="t1.txt"

ir=1


while IFS= read line
do
    skip=1
    # display $line or do something with $line
    t1=`echo "$line"` 
    #echo $t1
    if [[ ${t1} == *"="* ]];then
        tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
        tt2=`echo "$line" | cut -f2- -d'='`
         
            #echo $tt1
            if [[ ${tt1} == "$stype" ]];then   
                    # this is an ingress/egress rule
                    noself=0
                    skip=0
                    lbc=0
                    rbc=0
                    breq=0
                    skipit=0
                    ssgid=""
                    while [[ $breq -eq 0 ]];do 
                                # keep reading until [==] ir incremented within for separate rules
                                if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi 
                                if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                               
                                tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                tt2=`echo "$line" | cut -f2- -d'=' | tr -d '"'`                        

                                if [[ ${tt1} == "{" ]];then 
                                    noself=0
                                    skip=1;
                                fi

                                if [[ ${tt1} == *"}"* ]];then  # end of an egress / ingress individual rule
                                    if [[ ${self} == "true" ]]; then
                                        cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s_self | grep Import" $cname $stype $ir $cname $stype $proto $fromp $top)
                                        impfn=$(printf "imp_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                                        echo $cmd > $impfn
                                        #echo  ""
                                    elif [[ ${sgimp} != "" ]]; then
                                        cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s_%s | grep Import" $cname $stype $ir $cname $stype $proto $fromp $top $sgimp)
                                        impfn=$(printf "imp_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                                        #echo "in cmd2=$cmd"
                                        echo $cmd > $impfn
                                        #echo  ""
                                    elif [[ ${cidr} != "" ]]; then
                                        cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s_%s | grep Import" $cname $stype $ir $cname $stype $proto $fromp $top $cidr)
                                        impfn=$(printf "imp_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                                        #echo "in cmd3=$cmd"
                                        echo $cmd > $impfn
                                        #echo  ""
                                    else
                                        cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s | grep Import" $cname $stype $ir $cname $stype $proto $fromp $top)
                                        echo "in cmd4=$cmd"
                                        echo $cmd
                                        #echo  "" 
                                    fi

                                    if [[ "$skipit" == "1" ]];then  # don't process it
                                        #echo "remove $impfn"
                                        rm -f $impfn

                                    fi 

                                    ir=`expr $ir + 1` 
                                    skipit=0

                                    #echo "**cmd=$cmd  file=$impfn"
                                    skip=1;
                                fi


                                if [[ ${tt1} == "self" ]];then
                                    if [ ${noself} == "1" ]; then
                                        skip=1
                                    fi
                                    self=$(echo $tt2)
                                fi


                                if [[ ${tt1} == "self" ]];then
                                    if [ ${tt2} == "false" ]; then
                                        skip=1
                                    fi
                                fi

                                if [[ ${tt1} == "protocol" ]];then
                                    proto=$(echo $tt2)
                                    if [ ${proto} == "-1" ]; then
                                        proto="all"
                                    fi
                                fi

                                if [[ ${tt1} == "from_port" ]];then
                                    fromp=$(echo $tt2)
                                fi

                                if [[ ${tt1} == "to_port" ]];then
                                    top=$(echo $tt2)
                                    if [[ ${top} == "0" ]]; then
                                        top="65536"
                                    fi
                                fi

                                if [[ ${tt1} == *"."*"."*"."* ]];then
                                    cidr=$(echo $tt2 | tr -d ',')
                                fi

                                if [[ ${tt1} == "security_groups" ]];then
                                    #echo "t1 = $t1 $tt1 $tt2" 
                                    if [[ ${tt2} == *"[]"* ]];then
                                            skip=1  
                                        
                                    elif [[ ${tt2} == *"["* ]];then             
                                            read line 
                                            t1=`echo "$line"`
                                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi  
                                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi  
                                            tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                            tt2=`echo "$line" | cut -f2- -d'=' | tr -d '"'`  
                                            if [[ ${tt2} == *"sg-"* ]];then 
                                                tt2=`echo "$tt2" | tr -d ','`  
                                                #echo "***t1=$t1 tt2=$tt2 $ir"
                                                sgimp=$(echo $tt2)              
                                                t1=$(printf "source_security_group_id = aws_security_group.%s.id" $sgimp)
                                                if [[ ${tt1} == "source_security_group_id" ]];then
                                                    t1=$(printf "source_security_group_id = aws_security_group.%s.id" $tt2)
                                                    
                                                fi
                                           
                                                noself=1
                                                skip=1
                                            fi
                                            read line
                                            t1=`echo "$line"`
                                            tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                            tt2=`echo "$line" | cut -f2- -d'=' | tr -d '"'`
                                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi  
                                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                                    fi
                                    
                                    if [[ ${tt2} == *"sg-"* ]];then
                                        if [[ ${tt1} == "source_security_group_id" ]];then
                                            t1=$(printf "source_security_group_id = aws_security_group.%s.id" $tt2)
                                            echo "!!!!t1=$t1"
                                           
                                            noself=0
                                            skip=1
                                        fi
                                    fi
                                fi

                                
                                if [[ $rbc -eq $lbc ]]; then    # square bracket match
                                    breq=1; 
                                    skip=1
                                fi
                                
                                read line
                                skip=0
                                t1=`echo "$line"`
                              
                    done # bracket break

                    skipit=0
        fi # end egress / ingress type           

    fi   # if first =                 
done <"$file"

sglist=()
#echo "imp files"
#ls imp*.sh
for i in `ls imp_aws_security_group_rule_${1}_${2}*.sh 2> /dev/null`; do

    chmod 755 $i
    i1=$(echo $i | cut -f1 -d'.')
    sname=$(echo $i1 | cut -f6 -d'_')
    stype=$(echo $i1 | cut -f7 -d'_')
    ir=$(echo $i1 | cut -f8 -d'_')
    echo "$ttft $sname $cname $ir terraform file"
    fn=`printf "%s__%s_%s_%s.tf" $ttft $cname $stype $ir`
    if [ -f "$fn" ] ; then echo "$fn exists skipping" && continue; fi
   
    printf "resource \"%s\" \"%s_%s_%s\" {}\n" $ttft $cname $stype $ir > $fn

    echo "Importing $i"
    ./$i

    file=`printf "%s__%s_%s_%s.txt" $ttft $cname $stype $ir`
    terraform state show -no-color $ttft.${sname}_${stype}_${ir} > $file
    rm -f $fn
   
    if [ ! -f "$file" ] ; then echo "$file does not exist skipping" && continue; fi
     
    # Pass 1 - gather some info

    cidr=1
    cidr6=1
    isself=0
    ssgid=0
    sgmatch=0
    while IFS= read line
        do
                t1=`echo "$line"`
                  
                if [[ ${t1} == *"="* ]]; then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='` 

                    if [[ ${tt1} == "cidr_blocks" ]];then 
                        if [ ${tt2} == "[]" ];then
                            cidr=0
                        fi
                    fi 

                    if [[ ${tt1} == "ipv6_cidr_blocks" ]];then 
                        if [ ${tt2} == "[]" ];then
                            cidr6=0
                        fi
                    fi 

                    if [[ ${tt1} == "self" ]];then 
                        if [ ${tt2} == "true" ];then
                            isself=1
                        fi
                    fi

                    if [[ ${tt1} == "source_security_group_id" ]];then 
                        if [ ${tt2} != "" ];then
                            ssgid=1
                        fi
                        ssgsg=$(echo ${tt2} | tr -d '"' | tr -d ' ')
                    fi
                    if [[ ${tt1} == "security_group_id" ]];then 
                        sgsg=$(echo ${tt2} | tr -d '"' | tr -d ' ')
                    fi



                fi     
    done <"$file"


    if [ "$ssgsg" == "$sgsg" ];then sgmatch=1; fi
#echo "cidr=$cidr"
    # set some values

    echo $aws2tfmess > $fn

    while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]]; then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          

                    if [[ ${tt1} == "cidr_blocks" ]];then 
                        if [ "${cidr}" == "0" ];then
                            skip=1
                        fi
                    fi
                    if [[ ${tt1} == "ipv6_cidr_blocks" ]];then 
                        if [ "${cidr6}" == "0" ];then
                            skip=1
                        fi
                    fi
                    if [[ ${tt1} == "self" ]];then 
                        if  [ "${cidr}" == "1" ] || [ "${cidr6}" == "1" ];then
                            skip=1
                        fi
                        if [ "${ssgid}" == "1" ] && [ "$sgmatch" == "0" ];then  # if have source sg id and it's not the same as sg skip   
                            skip=1
                        fi
                    fi
                    if [[ ${tt1} == "source_security_group_id" ]];then 
                        if [ "$sgmatch" == "0" ];then # only write if two sg's dont match - if they do rely on self   
                            tt2=$(echo $tt2 | tr -d '"')
                            sglist+=`printf "\"%s\" " $tt2`
                            t1=$(printf "source_security_group_id = aws_security_group.%s.id" $tt2)
                        else
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "security_group_id" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        t1=$(printf "security_group_id = aws_security_group.%s.id" $tt2)
                    fi

                fi
                if [[ "$skip" == "0" ]]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi

                
    done <"$file" 
       
    for sg1 in ${sglist[@]}; do
                #echo "therole=$therole"
                sg1=`echo $sg1 | tr -d '"'`
                echo "calling SG rule embedded SG for $sg1"
                if [[ "$sg1" != "" ]]; then
                    ../../scripts/110-get-security-group.sh $sg1
                fi
    done 
    
done  # done for import

mkdir -p saved
#rm -f imp_aws_security_group_rule*.sh
mv imp_aws_security_group_rule*.sh saved 2> /dev/null
#terraform fmt > /dev/null
 

rm -f $ttft*.txt