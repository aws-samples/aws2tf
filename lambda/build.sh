docker stop  aws2tf && docker rm laws2tf
docker image rm laws2tf
docker build --no-cache -f Dockerfile.lambda -t  laws2tf . 