#!/bin/bash
for cmd in `ls ../../scripts/*get-aws_*.sh | rev | cut -f1 -d'/' | rev`;do
    #echo "cmd=$cmd"
    tft=${cmd#*"get-"}
    tft=`echo $tft | cut -f1 -d'.'`
    #echo "tft=$tft"
    #echo "Check tf file exists for $tft states"
    sync
    #echo "retry state moves for $tft"
    #../../scripts/local_statemv.sh $tft

    for i in `terraform state list 2> /dev/null | grep "${tft}\."`;do 
        rname=$(echo $i | cut -f2 -d'.')
        #echo "rname=$rname"
        f1=`printf "%s__%s.tf" $tft $rname`
        #echo $f1
        if [[ ! -f $f1 ]];then
            cname=$(echo $rname | cut -f2 -d'_')
            echo "State missing - $tft.$rname for $f1 not found - getting $cname"
            ../../scripts/$cmd $cname
            ../../scripts/local_statemv.sh $tft__$rname
        fi 

    done
    #echo "Checking for data/*.notfound for $tft"
    for i in `ls data/${tft}*.notfound 2> /dev/null`;do
        mv $i $i.done
        bc=$(echo $i | cut -f1 -d'.' | cut -d'/' -f2) 
        bc2=${bc#"${tft}__"}
        f1=`printf "%s__%s.tf" $tft $bc2`
        if [[ ! -f $f1 ]];then
            cname=$(echo $bc2 | cut -f2 -d'_')
            echo "HCL missing for - $f1 getting $cname"
            ../../scripts/$cmd $cname
            ../../scripts/local_statemv.sh $tft__$bc2
        fi
    done
done
