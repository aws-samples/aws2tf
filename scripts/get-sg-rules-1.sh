#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify sg exiting"
    exit
fi

for stype in ingress egress; do
    c=0
    pref[0]="SecurityGroups"
    cname=$(echo $1)

    ttft="aws_security_group_rule"
    file=$(echo aws_security_group-$cname-1.txt)

    ir=1

    while IFS= read line; do
        skip=1
        # display $line or do something with $line
        t1=$(echo "$line")
        #echo $t1
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$line" | cut -f2- -d'=')

            #echo $tt1
            if [[ ${tt1} == "$stype" ]]; then
                # this is an ingress/egress rule
                noself=0
                skip=0
                lbc=0
                rbc=0
                breq=0
                skipit=0
                ssgid=""
                echo "Generating imp2 $ttft $cname $stype $ir"
                impfn2=$(printf "imp2_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                rm -f $impfn2

                while [[ $breq -eq 0 ]]; do
                    # keep reading until [==] ir incremented within for separate rules
                    if [[ "${t1}" == *"["* ]]; then lbc=$(expr $lbc + 1); fi
                    if [[ "${t1}" == *"]"* ]]; then rbc=$(expr $rbc + 1); fi

                    tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                    tt2=$(echo "$line" | cut -f2- -d'=' | tr -d '"')

                    if [[ ${tt1} == "{" ]]; then
                        noself=0
                        skip=1
                    fi

                    #impfn2=$(printf "imp2_%s.sh" $ttft)


                    if [[ ${tt1} == *"}"* ]]; then # end of an egress / ingress individual rule
                        if [[ ${self} == "true" ]]; then
                            #cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s_self | grep Importing" $cname $stype $ir $cname $stype $proto $fromp $top)
                            cmd2=$(printf "../../scripts/parallel_import3.sh aws_security_group_rule %s %s_%s_%s sg2=%s_%s_%s_%s_%s_%s &" $cname $cname $stype $ir $cname $stype $proto $fromp $top "self")

                            #impfn=$(printf "imp_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                            #echo $cmd >$impfn
                            echo $cmd2 >>$impfn2
                            #echo  ""
                        elif [[ ${sgimp} != "" ]]; then
                            #cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s_%s | grep Importing" $cname $stype $ir $cname $stype $proto $fromp $top $sgimp)
                            cmd2=$(printf "../../scripts/parallel_import3.sh aws_security_group_rule %s %s_%s_%s sg3=%s_%s_%s_%s_%s_%s &" $cname $cname $stype $ir $cname $stype $proto $fromp $top $sgimp)

                            #impfn=$(printf "imp_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                            #echo "in cmd2=$cmd"
                            #echo $cmd >$impfn
                            echo $cmd2 >>$impfn2

                            #echo  ""
                        elif [[ ${cidr} != "" ]]; then
                            #cmd=$(printf "#terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s_%s | grep Importing" $cname $stype $ir $cname $stype $proto $fromp $top $cidr)
                            cmd2=$(printf "../../scripts/parallel_import3.sh aws_security_group_rule %s %s_%s_%s sg1=%s_%s_%s_%s_%s_%s &" $cname $cname $stype $ir $cname $stype $proto $fromp $top $cidr)
                            #impfn=$(printf "imp_%s_%s_%s_%s.sh" $ttft $cname $stype $ir)
                            echo $cmd2 >>$impfn2
                            #echo  ""
                        else
                            cmd=$(printf "terraform import aws_security_group_rule.%s_%s_%s %s_%s_%s_%s_%s | grep Importing" $cname $stype $ir $cname $stype $proto $fromp $top)
                            echo "in cmd4=$cmd"
                            echo $cmd
                            #echo  ""
                        fi

                        if [[ "$skipit" == "1" ]]; then # don't process it
                            #echo "remove $impfn"
                            rm -f $impfn

                        fi
                        ## increment ir
                        ir=$(expr $ir + 1)
                        skipit=0

                        #echo "**cmd=$cmd  file=$impfn"
                        skip=1
                    fi

                    if [[ ${tt1} == "self" ]]; then
                        if [ ${noself} == "1" ]; then
                            skip=1
                        fi
                        self=$(echo $tt2)
                    fi

                    if [[ ${tt1} == "self" ]]; then
                        if [ ${tt2} == "false" ]; then
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "protocol" ]]; then
                        proto=$(echo $tt2)
                        if [ ${proto} == "-1" ]; then
                            proto="all"
                        fi
                    fi

                    if [[ ${tt1} == "from_port" ]]; then
                        fromp=$(echo $tt2)
                    fi

                    if [[ ${tt1} == "to_port" ]]; then
                        top=$(echo $tt2)
                        if [[ ${top} == "0" ]]; then
                            top="65536"
                        fi
                    fi

                    if [[ ${tt1} == *"."*"."*"."* ]]; then
                        cidr=$(echo $tt2 | tr -d ',')
                    fi

                    if [[ ${tt1} == "security_groups" ]]; then
                        #echo "t1 = $t1 $tt1 $tt2"
                        if [[ ${tt2} == *"[]"* ]]; then
                            skip=1

                        elif [[ ${tt2} == *"["* ]]; then
                            read line
                            t1=$(echo "$line")
                            if [[ "${t1}" == *"["* ]]; then lbc=$(expr $lbc + 1); fi
                            if [[ "${t1}" == *"]"* ]]; then rbc=$(expr $rbc + 1); fi
                            tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                            tt2=$(echo "$line" | cut -f2- -d'=' | tr -d '"')
                            if [[ ${tt2} == *"sg-"* ]]; then
                                tt2=$(echo "$tt2" | tr -d ',')
                                #echo "***t1=$t1 tt2=$tt2 $ir"
                                sgimp=$(echo $tt2)
                                t1=$(printf "source_security_group_id = aws_security_group.%s.id" $sgimp)
                                if [[ ${tt1} == "source_security_group_id" ]]; then
                                    t1=$(printf "source_security_group_id = aws_security_group.%s.id" $tt2)

                                fi

                                noself=1
                                skip=1
                            fi
                            read line
                            t1=$(echo "$line")
                            tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                            tt2=$(echo "$line" | cut -f2- -d'=' | tr -d '"')
                            if [[ "${t1}" == *"["* ]]; then lbc=$(expr $lbc + 1); fi
                            if [[ "${t1}" == *"]"* ]]; then rbc=$(expr $rbc + 1); fi
                        fi

                        if [[ ${tt2} == *"sg-"* ]]; then
                            if [[ ${tt1} == "source_security_group_id" ]]; then
                                t1=$(printf "source_security_group_id = aws_security_group.%s.id" $tt2)
                                echo "!!!!t1=$t1"

                                noself=0
                                skip=1
                            fi
                        fi
                    fi

                    if [[ $rbc -eq $lbc ]]; then # square bracket match
                        breq=1
                        skip=1
                    fi

                    read line
                    skip=0
                    t1=$(echo "$line")

                done # bracket break

                skipit=0
            fi # end egress / ingress type

        fi # if first =
    done <"$file"
    #echo "wait" >>$impfn2
done # ingress egress
