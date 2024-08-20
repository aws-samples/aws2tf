docker run  --name aws2tf --rm -v $(pwd):/aws2tf aws2tf -t vpc -v 
docker run  --name aws2tf --rm -v $(pwd)/generated:/aws2tf/generated aws2tf
docker run  --name aws2tf -d -t -v $(pwd):/aws2tf aws2tf 
#docker logs -t aws2tf
docker exec -it aws2tf sh  
docker stop  aws2tf && docker rm aws2tf