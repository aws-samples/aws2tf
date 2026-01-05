of="needid-dict.py"
rm -f $of
for i in `cat aws_resources_paramval.dat`;do
param=$(echo $i | cut -f1 -d',')
tfr=$(echo $i | cut -f2 -d',')
clfn=$(echo $i | cut -f3 -d',')
if [[ $clfn != *"_"* ]];then
    echo "\n$tfr = {" >> $of
    echo "  \"param\": \"$param\"," >> $of
    echo "  \"clfn\": \"$clfn\"" >> $of
    echo "}" >> $of

else

    param1=$(echo $i | cut -f1 -d',')
    param2=$(echo $i | cut -f2 -d',')
    tfr=$(echo $i | cut -f3 -d',')
    clfn=$(echo $i | cut -f4 -d',')
    echo "\n$tfr = {" >> $of
    echo "  \"param\": \"$param1,$param2\"," >> $of
    echo "  \"clfn\": \"$clfn\"" >> $of
    echo "}" >> $of
fi
done

echo "\naws_needid = {" >> $of
for i in `cat aws_resources_paramval.dat`;do
clfn=$(echo $i | cut -f3 -d',')
if [[ $clfn != *"_"* ]];then
    tfr=$(echo $i | cut -f2 -d',')
else
    tfr=$(echo $i | cut -f3 -d',')
fi
echo "  \"$tfr\": $tfr," >> $of

done
echo "}" >> $of