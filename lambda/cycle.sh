date
echo "CLEAN"
./clean.sh
echo "BUILD"
./build.sh
echo "PUSH"
./push.sh
echo "Sleep 10"
sleep 10
echo "CREATE LAMBDA"
./cre-lambda.sh
echo "Sleep 20"
sleep 20
echo "INVOKE LAMBDA"
./run-lambda.sh
date