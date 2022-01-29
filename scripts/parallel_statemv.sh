#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi
for st in `ls pi2/$1__*.tfstate` 
do
echo "attempting move $st"
    sl=`echo $((1 + $RANDOM % 10))`
    terraform -state $st state mv -state-out=../terraform.tfstate -lock=true $ttft.$rname $ttft.$rname &> /dev/null
    if [ $? -ne 0 ]; then
        sl=`echo $((1 + $RANDOM % 10))`
        sleep $sl
        echo "state mv retry for $rname"
        terraform -state $st state mv -state-out=../terraform.tfstate -lock=true $ttft.$rname $ttft.$rname  &> /dev/null
        if [ $? -ne 0 ]; then
            echo "error state mv $st"
        else
            echo "ok2 - rm state $st"
            rm -f pi2/$st
        fi
    else
        echo "ok1 - rm state pi2/$st"
        rm -f pi2/$st
    fi

rm -f terr*.backup
echo "state mv done for  $rname"
done