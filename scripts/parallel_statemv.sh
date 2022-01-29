#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi
for st in `ls pi2/$1__*.tfstate` 

do
    echo "attempting move $st"
    ttft=$(echo $1)
    rname=${st/pi2\/aws_cloudwatch_log_group__/}
    rname=$(echo $rname | cut -f1 -d'.')
    echo "moving $ttft $rname"
    sl=`echo $((1 + $RANDOM % 10))`
    #terraform state mv -state $st -lock=true $ttft.$rname $ttft.$rname > /dev/null
    comm=$(printf "terraform state mv -state %s -lock=true %s.%s %s.%s" $st $ttft $rname $ttft $rname)
    echo $comm
    eval $comm
    if [ $? -ne 0 ]; then
        sl=`echo $((1 + $RANDOM % 10))`
        sleep $sl
        echo "state mv retry for $st"
        eval $comm
        if [ $? -ne 0 ]; then
            echo "** error state mv $st"
        else
            echo "ok2 - rm state $st"
            rm -f pi2/$st
        fi
    else
        echo "ok1 - rm state pi2/$st"
        rm -f pi2/$st
    fi

rm -f terr*.backup
echo "state mv done for $1"
done