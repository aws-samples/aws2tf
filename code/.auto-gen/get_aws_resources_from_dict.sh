echo "be patient! ..... "
for i in `cat ../aws_resources/aws_dict.py`; do
echo $i | grep 'aws_' | grep ':' | tr -d '"|:'
done