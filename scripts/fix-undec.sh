echo "--> Validate Fixer"
vl=$(cat validate.json | jq '.diagnostics | length')
#echo $vl
if [[ $vl -eq 0 ]]; then exit; fi
undec=$(cat validate.json | jq '.diagnostics')
count=$(echo $undec | jq '. | length' | tail -1)
count=$(expr $count - 1)
#echo $count

for c in $(seq 0 $count); do
    summ=$(echo $undec | jq ".[(${c})].summary")
    echo $summ
    if [[ "$summ" == *"Reference to undeclared resource"* ]]; then
        fil=$(echo $undec | jq -r ".[(${c})].range.filename")
        code=$(echo $undec | jq -r ".[${c}].snippet.code" | tr -d ' ')
        echo "code snip =$code"
        if [[ $code == *"="* ]];then
            res=$(echo $code | cut -f2 -d'=')
        else
            res=$(echo $code)
        fi
        echo "res =$res"
        if [[ $fil != "" ]]; then
            addr=$(echo $res | cut -f2 -d'.')
            tft=$(echo $res | cut -f1 -d'.' | tr -d '"')
            echo "ttft=$tft  addr=$addr"

            if [[ $tft == "aws_s3_bucket" ]]; then
                addr=$(echo $addr | cut -f2 -d'_')
                cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $addr)
                #echo " " ;echo $cmd
                echo "** Undeclared Fix: $res --> $addr"
                eval $cmd
            fi
            if [[ $tft == "aws_kms_key" ]]; then
                addr=$(echo $addr | cut -f2 -d'_')
                tarn=$(grep $addr data/arn-map.txt | cut -f2 -d',')
                if [[ $tarn != "null" ]]; then
                    cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $tarn)
                    echo " " ;echo $cmd
                    echo "** Undeclared Fix: $res --> $addr"
                    eval $cmd
                fi
            fi
            if [[ $tft == "aws_vpc" ]] || [[ $tft == "aws_subnet" ]] || [[ $tft == "aws_ec2_transit_gateway_vpc_attachment" ]] || [[ $tft == "aws_vpc_peering_connection" ]]; then
                cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $addr)
                echo "** Undeclared Fix: $res --> $addr"
                eval $cmd
            fi

            if [[ $tft == "aws_sns_topic" ]]; then
                addr=$(echo $addr | cut -f2 -d'_')
                tarn=$(grep $addr data/arn-map.txt | cut -f2 -d',')
                ttyp=$(grep $addr data/arn-map.txt | cut -f1 -d',')
                if [[ $ttyp == "aws_sns_topic" ]]; then
                    if [[ $tarn != "null" ]]; then
                        cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $tarn)
                        echo " " ;echo $cmd
                        echo "** Undeclared Fix: $res --> $addr"
                        eval $cmd

                    fi
                fi
            fi
        fi
    fi
done

# enable_classiclink
for c in $(seq 0 $count); do
    #echo $c
    summ=$(echo $undec | jq ".[(${c})].summary")
    if [[ "$summ" == *"Argument is deprecated"* ]]; then
        fil=$(echo $undec | jq ".[(${c})].range.filename")
        res=$(echo $undec | jq -r ".[(${c})].snippet.code" | tr -d ' ' | cut -f1 -d'=')

        if [[ $res == *"enable_classiclink"* ]]; then
            cmd=$(printf "sed -i'.orig' -e 's/%s/#%s/g' ${fil}" $res $res)
            echo "Depreciated classiclink Fix --> $res"
            #echo $cmd
            eval $cmd
        fi
    fi
done

# name_prefix conflict
for c in $(seq 0 $count); do
    summ=$(echo $undec | jq ".[(${c})].summary")
    if [[ "$summ" == *"Conflicting configuration arguments"* ]]; then
        #echo $c
        fil=$(echo $undec | jq ".[(${c})].range.filename")
        res=$(echo $undec | jq ".[${c}].snippet.code" | tr -d ' ' | cut -f1 -d'=')
        line=$(echo $undec | jq ".[${c}].range.start.line")

        if [[ $det == *"name_prefix"* ]]; then
            cmd=$(printf "sed -i -e '%ss/.*/\#/' ${fil}" $line)
            echo "Deleted conflicting name fix --> $res"
            #echo $cmd
            eval $cmd

        fi
    fi
done
ofil=""

for c in $(seq 0 $count); do
    summ=$(echo $undec | jq ".[(${c})].summary")
    if [[ "$summ" == *"Value for unconfigurable attribute"* ]]; then
        #echo $undec | jq ".[(${c})]"
        fil=$(echo $undec | jq ".[(${c})].range.filename")
        res=$(echo $undec | jq -r ".[${c}].snippet.code" | tr -d ' ' | cut -f1 -d'=')
        line=$(echo $undec | jq ".[${c}].range.start.line")
        #code=$(echo $undec | jq ".[${c}].snippet.code")
        if [[ $line != "" ]]; then
            cmd=$(printf "sed -i -e '%ss/.*//' ${fil}" $line)
            echo "Unconfigurable attribute fix --> $res"
            #echo $cmd
            eval $cmd
        else
            echo "skipping $summ"

        fi
    fi
done

for c in $(seq 0 $count); do
    summ=$(echo $undec | jq ".[(${c})].summary")
    if [[ "$summ" == *"Invalid or unknown key"* ]]; then
        #echo $undec | jq ".[(${c})]"
        fil=$(echo $undec | jq ".[(${c})].range.filename")
        res=$(echo $undec | jq -r ".[${c}].snippet.code" | tr -d ' ' | cut -f1 -d'=')
        line=$(echo $undec | jq ".[${c}].range.start.line")
        #code=$(echo $undec | jq ".[${c}].snippet.code")
        if [[ $line != "" ]]; then
            cmd=$(printf "sed -i -e '%ss/.*/ /' ${fil}" $line)
            echo "Unconfigurable attribute fix --> $res"
            #echo $cmd
            eval $cmd
        else
            echo "skipping $summ"

        fi
    fi
done

for c in $(seq 0 $count); do
    summ=$(echo $undec | jq ".[(${c})].summary")
    if [[ "$summ" == *"Missing required argument"* ]]; then
        #echo $undec | jq ".[(${c})]"
        fil=$(echo $undec | jq ".[(${c})].range.filename")
        res=$(echo $undec | jq -r ".[${c}].snippet.code" | tr -d ' ' | cut -f1 -d'=')
        line=$(echo $undec | jq ".[${c}].range.start.line")
        code=$(echo $undec | jq -r ".[${c}].snippet.code" | tr -d ' ')

        if [[ $line != "" ]]; then
            if [[ $code == "ipv6_netmask_length=0" ]]; then
                cmd=$(printf "sed -i -e '%ss/.*/ /' ${fil}" $line)
                echo "Missing required argument fix --> $res"
                #echo $cmd
                eval $cmd
            fi
        else
            echo "skipping $summ"

        fi
    fi
done
