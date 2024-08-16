


date
lc=0
echo "loop through providers"
pwd
../../scripts/100-get-vpc.sh
../../scripts/105-get-subnet.sh
../../scripts/110-get-security-group.sh
#../../scripts/110-get-security-group-default.sh
../../scripts/launch_template.sh
../../scripts/auto-scaling-groups.sh
../../scripts/elbv2.sh
date


