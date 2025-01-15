for i in `ls orig/aws*.orig`; do
echo $i
j=`echo $i | cut -f2 -d'/' | cut -f1 -d'.'`
echo $j.tf
cp $i $j.tf
done
for i in `ls orig/output__aws*.orig`; do
echo $i
j=`echo $i | cut -f2 -d'/' | cut -f1 -d'.'`
echo $j.tf
cp $i $j.tf
done



rm vpc*
rm sub-*
rm *.orig