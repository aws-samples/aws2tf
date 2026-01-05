api=$(echo $1 | cut -f3 -d':' | tr '[:upper:]' '[:lower:]')
res=$(echo $1 | cut -f5 -d':' | tr '[:upper:]' '[:lower:]')
echo "Fine"
grep $api aws_resources.dat | grep $res

echo "Resource"
grep $res aws_resources.dat 

echo "API"
grep $api aws_resources.dat 

