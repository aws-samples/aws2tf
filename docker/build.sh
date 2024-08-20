docker stop  aws2tf && docker rm aws2tf
docker image rm aws2tf
docker build --no-cache -t aws2tf . 