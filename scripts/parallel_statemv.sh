#!/bin/bash
rname=""
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi
if [ "$2" != "" ]; then
    rname=$(echo $2)
fi
sl=1
ls pi2/${1}*.tfstate &>/dev/null
if [[ $? -ne 0 ]]; then
    #echo "No state files in pi2 skipping ..."
    exit
else
    echo "Starting state mv for $1"
fi
for st in $(ls pi2/$1_*.tfstate 2>/dev/null); do
    ttft=$(echo $1)
    #if [[ $rname == "" ]]; then
        rname=$(echo $st | rev | cut -f2- -d'.' | rev)
        rname=$(echo $rname | cut -f2 -d'/')
        tfaddr=$(echo $rname | sed 's/__/./')
        ttft=$(echo $tfaddr | cut -f1 -d'.')
        rname=$(echo $tfaddr | cut -f2 -d'.')

        if [[ $rname == *"/"* ]];then
            rname=$(echo $rname | cut -f2 -d'/')
        fi
    #fi

    sl=1
    comm=$(printf "terraform state mv -state %s -state-out=terraform.tfstate -lock=true %s %s 2> /dev/null" $st $tfaddr $tfaddr)
    #echo $comm
    eval $comm > /dev/null
    stat=$(echo $?)
    #echo "-3-> $stat"
    while [[ $stat -ne 0 ]]; do
        sl=`expr $sl + 1`
        #echo "$sl move $ttft $rname"
        if [[ $sl -gt 3 ]];then
            echo "**> State move $ttft $rname failed"
            echo $comm
            break
        fi 
        terraform state list -state terraform.tfstate $ttft.$rname 2>/dev/null
        if [[ $? -eq 0 ]];then 
            #echo "TF list break"
            tfb=1
            break 
        fi
        sleep $sl
        echo "retrying state move - $sl"
        eval $comm >/dev/null
        stat=$(echo $?)
        #echo "-4-> $stat"
    done
    if [[ $sl -le 3 ]];then
        echo "Consolidated state $tfaddr"
        rm -f $st
    fi
    #cfile=$(printf "%s-%s-1.txt" $ttft $rname)
    #nl=$(cat $cfile | wc -l)
    #if [[ $nl -eq 0 ]]; then
    #    echo "--> redoing $cfile"
    #    terraform state show -no-color $tfaddr >$cfile
    #fi
done

rm -f pi2/*.backup
#rm -f pi2/*.log
#rm -f pi2/*.json
#rm -f pi2/${1}*.tfstate


