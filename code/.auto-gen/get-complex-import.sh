rm -f complex-import-list.dat
ls -l ../provider-data/terraform-provider-aws/website/docs/r/*.markdown | wc -l
for i in `ls ../provider-data/terraform-provider-aws/website/docs/r/*.markdown`; do
res=$(grep Resource: $i | cut -f2 -d':' | tr -d ' ' | grep aws_)
grep ' id = "' $i | grep -v 'arn:' | grep ':\|/' &> /dev/null
if [[ $? -eq 0 ]];then
    id=$(grep ' id = "' $i | grep -v 'arn:' | grep ':\|/')
    echo $res,$id >> complex-import-list.dat
fi
done
