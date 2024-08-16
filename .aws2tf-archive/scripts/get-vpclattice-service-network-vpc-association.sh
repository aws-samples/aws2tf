#!/bin/bash
ttft="aws_vpclattice_service_network_vpc_association"
pref="items"
idfilt="id"

cm="$AWS vpc-lattice vpc-lattice list-service-network-vpc-associations"
if [[ "$1" != "" ]]; then
    if [[ "$1" == "sn-"* ]]; then
        cm=$(printf "$AWS vpc-lattice list-service-network-vpc-associations --service-network-identifier $1")
    elif [[ "$1" == "vpc-"* ]]; then
        cm=$(printf "$AWS vpc-lattice list-service-network-vpc-associations --vpc-identifier $1")
    else
        echo "must pass service network or service as a parameter"
        exit
    fi
else
    echo "must pass service network or vpc id as a parameter"
    exit
fi

count=1
#echo $cm
awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "sn-"* ]]; then count=$(echo $awsout | jq ".${pref} | length"); fi
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)
for i in $(seq 0 $count); do
    #echo $i

    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname >$fn
    terraform import $ttft.${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.${rname} >t1.txt

    rm -f $fn
    subnets=()
    file="t1.txt"
    echo $aws2tfmess >$fn
    while IFS= read t1; do
        skip=0
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$t1" | cut -f2- -d'=')
            if [[ ${tt1} == "id" ]]; then skip=1; fi
            if [[ ${tt1} == "create_date" ]]; then skip=1; fi
            if [[ ${tt1} == "arn" ]]; then skip=1; fi
            if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
            if [[ ${tt1} == "status" ]]; then skip=1; fi
            if [[ ${tt1} == "created_by" ]]; then skip=1; fi

            if [[ ${tt1} == "dns_entry" ]]; then
                # skip the block
                tt2=$(echo $tt2 | tr -d '"')
                skip=1
                while [ "$t1" != "]" ] && [ "$tt2" != "[]" ]; do
                    read line
                    t1=$(echo "$line")
                done
            fi
            if [[ ${tt1} == "service_network_identifier" ]]; then
                sni=$(echo $tt2 | tr -d '"')
                t1=$(printf "$tt1 = aws_vpclattice_service_network.%s.id" $sni)
            fi
            if [[ ${tt1} == "service_identifier" ]]; then
                si=$(echo $tt2 | tr -d '"')
                t1=$(printf "$tt1 = aws_vpclattice_service.%s.id" $si)
            fi
            if [[ ${tt1} == "vpc_identifier" ]]; then
                vpcid=$(echo $tt2 | tr -d '"')
                t1=$(printf "%s = aws_vpc.%s.id" $tt1 $vpcid)
            fi
        else

            if [[ "$t1" == *"sg-"* ]]; then
                t1=$(echo $t1 | tr -d '"|,')
                sgs+=$(printf "\"%s\" " $t1)
                t1=$(printf "aws_security_group.%s.id," $t1)
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
    ../../scripts/100-get-vpc.sh $vpcid
    for sg in ${sgs[@]}; do
        sg1=$(echo $sg | tr -d '"')
        echo "calling for $sg1"
        if [ "$sg1" != "" ]; then
            ../../scripts/110-get-security-group.sh $sg1
        fi
    done
done

#rm -f t*.txt
