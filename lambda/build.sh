#aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
docker stop laws2tf && docker rm laws2tf
docker image rm laws2tf
docker build --no-cache -f Dockerfile.lambda -t  laws2tf . 