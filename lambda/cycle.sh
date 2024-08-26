echo "CLEAN"
./clean.sh
echo "BUILD"
./build.sh
echo "PUSH"
./push.sh
echo "CREATE LAMBDA"
./cre-lambda.sh
echo "INVOKE LAMBDA"
./run-lambda.sh