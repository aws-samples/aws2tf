
#!/bin/bash
fsg="data/def-sgs.dat"
if [ -f "$fsg" ] ; then
    for i in `cat $fsg`; do

        sgn=$(echo $i | cut -f2 -d':')
        #echo $sgn
        # loop for substitution
        for tft in `grep aws_security_group.${sgn}.id *.tf | cut -f1 -d':'` ;do
            #echo $tft
            # check not already done
            grep data.aws_security_group.${sgn}.id $tft > /dev/null
            if [[ $? -ne 0 ]];then
                cmd=`printf "sed -i'.orig' -e 's/aws_security_group.%s.id/data.aws_security_group.%s.id/g' ${tft}" $sgn $sgn`
                echo "using data.aws_security_group.${sgn} in $tft"
                eval $cmd
            fi
        done
        echo "remove tf file for default SG aws_security_group__${sgn}.tf"
        cp aws_security_group__${sgn}.tf saved 2&> /dev/null
        rm -f aws_security_group__${sgn}.tf > /dev/null
        echo "remove tf state for default security group aws_security_group.${sgn}"
        terraform state rm aws_security_group.${sgn}
    done
fi



