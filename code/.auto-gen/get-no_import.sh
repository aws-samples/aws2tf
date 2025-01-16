rm -f aws_no_import.py
ls -l ../provider-data/terraform-provider-aws/website/docs/r/*.markdown | wc -l
echo 'noimport = {' >> aws_no_import.py
for i in `ls ../provider-data/terraform-provider-aws/website/docs/r/*.markdown`; do
res=$(grep Resource: $i | cut -f2 -d':' | tr -d ' ' | grep aws_)
echo $res $i
grep ' id = "' $i &> /dev/null  
if [[ $? -ne 0 ]];then
    echo '    "'${res}'": True,' >> aws_no_import.py
fi

done
echo '}' >> aws_no_import.py
