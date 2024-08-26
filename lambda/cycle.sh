echo "CLEAN"
./clean.sh
echo "BUILD"
./build.sh
echo "PUSH"
./push.sh
echo "CREATE LAMBDA"
./cre-lambda.sh
echo "Sleep 20"
sleep 20
echo "INVOKE LAMBDA"
date
./run-lambda.sh