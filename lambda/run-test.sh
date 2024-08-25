docker run --name aws2tf --platform linux/arm64 -p 9000:8080 laws2tf
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'