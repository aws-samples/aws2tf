#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi
if [ "$2" == "" ]; then
    echo "must specify resource name (cname)"
    exit
fi
ttft=`echo $1 | tr -d '"'`
cname=`echo $2 | tr -d '"'`
rname=${cname//:/_}
rname=${rname//./_}
rname=${rname//\//_}
#echo "Import $rname"
mkdir -p $ttft-$rname && cd $ttft-$rname

cp ../aws.tf .
#echo "TF Init..."
terraform init -no-color > /dev/null

printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
printf "}" >> $ttft.$rname.tf
#echo "Importing..."           
terraform import $ttft.$rname "$cname" | grep Import 
#echo "local state list"
#terraform state list -no-color

printf "terraform import %s.%s %s" $ttft $rname "$cname" > ../data/import_$ttft_$rname.sh

terraform state show $ttft.$rname > $ttft-$rname-2.txt
cat $ttft-$rname-2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > $ttft-$rname-1.txt
tfa=`printf "%s.%s" $ttft $rname`
#terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > ../data/$tfa.json
            #echo $awsj | jq . 
rm $ttft.$rname.tf
#echo "attempting move"
terraform state mv -state-out=../terraform.tfstate -lock=true $ttft.$rname $ttft.$rname | grep -v $ttft
mv $ttft-$rname-1.txt ..
cd .. 
rm -rf $ttft-$rname
#echo "top level state list"
#terraform state list | grep $ttft.$rname
#echo "exit parallel import"