rm -f master-resources-list.dat
ls -l ../provider-data/terraform-provider-aws/website/docs/r/*.markdown | wc -l
for i in `ls ../provider-data/terraform-provider-aws/website/docs/r/*.markdown`; do
grep Resource: $i | cut -f2 -d':' | tr -d ' ' | grep aws_ >> master-resources-list.dat
done
wc -l master-resources-list.dat