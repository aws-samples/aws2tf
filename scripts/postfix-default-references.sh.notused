terraform state list | grep aws_default_security_group > tfd.tmp
for i in `cat tfd.tmp` ; do
j=`echo $i | cut -d'.' -f2`
k=`printf "aws_security_group.%s" $j`
for f in `ls aws_*.tf` ; do
grep $k $f > /dev/null
if [ $? -eq 0 ]; then
    echo $f
    mv $f $f.orig
    cmd=`printf "sed 's/%s/aws_default_security_group.%s/g' %s.orig > %s" $k $j $f $f` 
    echo $cmd 
    eval $cmd
fi
done
done