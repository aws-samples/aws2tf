for i in `ls ../aws_resources/fixtf_*.py`; do
it=$(echo $i | cut -f3 -d '/' | cut -f1 -d '.')
echo "from aws_resources import $it"
done