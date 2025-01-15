cp ../README.md README.md.sav
docdate=$(date +%d-%b-%Y)
echo ""
echo "----"
echo "## Terraform resources supported as of $docdate"
echo ""
for i in $(grep 'tft' *.sh | grep aws_ | cut -f2 -d'=' | tr -d '"' | sort -u | grep -v '\$'); do
echo "* $i"
done
echo ""
echo "----"
echo "## Resources within a Stack Set that can currently be converted to Terraform (-s <stack set name>) as of $docdate"
echo ""
for i in $(grep 'AWS::' get-stack.sh | grep '.sh' | cut -f1 -d')' | tr -d ' ' | sort -u); do
echo "* $i"
done
echo " "
echo "----"
