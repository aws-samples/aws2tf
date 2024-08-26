#curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"-t vpc -r eu-west-2"}'
aws lambda invoke \
--payload '{"payload":"-t vpc -r eu-west-2"}' --function-name laws2tf \
--invocation-type Event \
--cli-binary-format raw-in-base64-out \
/dev/stdout