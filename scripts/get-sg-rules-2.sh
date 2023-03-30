#!/bin/bash
ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=`expr $ncpu \* 1`
for i in $(ls imp2_aws_security_group_rule*.sh 2>/dev/null); do
    #echo "Para Import"
    echo $i
    chmod 755 $i
    . ./$i 
    #Throttle
    jc=`jobs -r | wc -l | tr -d ' '`
    while [ $jc -gt $ncpu ];do
        echo "Throttling - $jc jobs in progress"
        sleep 4
        jc=`jobs -r | wc -l | tr -d ' '`
    done
done
wait
#mv imp2_aws_security_group_rule*.sh saved 2>/dev/null


