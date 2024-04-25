for i in `cat boto3-error.plog`;do
    res=$(echo $i | grep 'type=' | cut -d'=' -f2 | tr -d ' ')
    if [[ $res == *"aws_"* ]]; then
        t1=`printf "\t\"%s\": True," $res`
        echo $t1
    fi
done