#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    pref="aws_"
else
    pref=$(echo $1)
fi
sync;sync
echo "listing in local state move"
#ls -l ${pref}*.tfstate
ls ${pref}*.tfstate &> /dev/null
if [[ $? -ne 0 ]];then
    echo "No ${pref} state files exiting ..."
    exit
else
    echo "Starting state mv for $pref"
fi
for st in `ls ${pref}*.tfstate 2> /dev/null` 
do
    ttft=${st%__*}

    #rname=${st#\/${1}__/}
    rname=${st#${ttft}__}
    rname=$(echo $rname | cut -f1 -d'.')  
    echo $st $ttft $rname
    sl=`echo $((1 + $RANDOM % 10))`
    terraform state rm $ttft.$rname 2> /dev/null
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

    echo ">> moved state $ttft.$rname"
    #cfile=`printf "%s-%s-1.txt" $ttft $rname`
    #nl=$(cat $cfile | wc -l)
    #if [[ $nl -eq 0 ]];then
    #    echo "--> redoing $cfile"
    #    terraform state show -no-color $ttft.$rname > $cfile
    #   fi
done
rm -f terr*.backup
rm -rf pi2