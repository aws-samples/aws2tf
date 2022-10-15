#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi
ls pi2/${1}*.tfstate &> /dev/null
if [[ $? -ne 0 ]];then
    echo "No state files in pi2 skipping ..."
    exit
else
    echo "Starting state mv for $1"
fi
for st in `ls pi2/$1__*.tfstate 2> /dev/null` 
do
    ttft=$(echo $1)
    rname=${st/pi2\/${1}__/}
    rname=$(echo $rname | cut -f1 -d'.')  
    sl=`echo $((1 + $RANDOM % 10))`
    comm=$(printf "terraform state mv -state %s -state-out=terraform.tfstate -lock=true %s.%s %s.%s" $st $ttft $rname $ttft $rname)
    #echo $comm
    eval $comm > /dev/null
    if [ $? -ne 0 ]; then
        sl=`echo $((1 + $RANDOM % 10))`
        sleep $sl
        echo "state mv retry for $st"
        eval $comm
        if [ $? -ne 0 ]; then
            echo "** error state mv $st"
        else
            #echo "ok2 - rm state $st"
            rm -f $st*
        fi
    else
        #echo "ok1 - rm state $st"
        rm -f $st*
    fi

echo "moved state $ttft.$rname"
cfile=`printf "%s-%s-1.txt" $ttft $rname`
nl=$(cat $cfile | wc -l)
if [[ $nl -eq 0 ]];then
    echo "--> redoing $cfile"
    terraform state show -no-color $ttft.$rname > $cfile
fi
done
rm -f terr*.backup
rm -rf pi2