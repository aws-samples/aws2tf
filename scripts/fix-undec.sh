undec=$(cat validate.json | jq '.diagnostics')
count=$(echo $undec | jq '. | length' | tail -1)
count=$(expr $count - 1)
#echo $count

for c in $(seq 0 $count); do

    fil=$(echo $undec | jq ".[(${c})] | select(.summary==\"Reference to undeclared resource\")" | jq -r '.range.filename')
    res=$(echo $undec | jq ".[${c}] | select(.summary==\"Reference to undeclared resource\")" | jq -r '.snippet.code' | tr -d ' ' | cut -f2 -d'=')
    if [[ $fil != "" ]]; then
        addr=$(echo $res | cut -f2 -d'.')
        tft=$(echo $res | cut -f1 -d'.')

        if [[ $tft == "aws_s3_bucket" ]]; then
            addr=$(echo $addr | cut -f2 -d'_')
            cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $addr)
            #echo " " ;echo $cmd
            echo "Undeclared Fix --> $res"
            eval $cmd
        fi
        if [[ $tft == "aws_kms_key" ]]; then
            addr=$(echo $addr | cut -f2 -d'_')
            tarn=$(grep $addr data/arn-map.txt | cut -f2 -d',')
            if [[ $tarn != "null" ]]; then
                cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $tarn)
                #echo " " ;echo $cmd
                echo "Undeclared Fix --> $res"
                eval $cmd
            fi
        fi
        if [[ $tft == "aws_vpc" ]] || [[ $tft == "aws_subnet" ]]; then
                cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $addr)
                echo "Undeclared Fix --> $res"
                eval $cmd
        fi

        if [[ $tft == "aws_sns_topic" ]]; then
            addr=$(echo $addr | cut -f2 -d'_')
            tarn=$(grep $addr data/arn-map.txt | cut -f2 -d',')
            ttyp=$(grep $addr data/arn-map.txt | cut -f1 -d',')
            if [[ $ttyp == "aws_sns_topic" ]]; then
                if [[ $tarn != "null" ]]; then
                    cmd=$(printf "sed -i'.orig' -e 's/%s/\"%s\"/g' ${fil}" $res $tarn)
                    #echo " " ;echo $cmd
                    echo "Undeclared Fix --> $res"
                    eval $cmd

                fi
            fi
        fi
    fi

done

# enable_classiclink
for c in $(seq 0 $count); do
    #echo $c
    fil=$(echo $undec | jq ".[(${c})] | select(.summary==\"Argument is deprecated\")" | jq -r '.range.filename')
    res=$(echo $undec | jq ".[${c}] | select(.summary==\"Argument is deprecated\")" | jq -r '.snippet.code' | tr -d ' ' | cut -f1 -d'=')
    #echo "res=$res"
    if [[ $res == *"enable_classiclink"* ]];then
        cmd=$(printf "sed -i'.orig' -e 's/%s/#%s/g' ${fil}" $res $res)
        echo "Depreciated classiclink Fix --> $res"
        echo $cmd
        eval $cmd
    fi
done
