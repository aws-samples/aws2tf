docker build -t terraform-docker .  
# This command mounts the current directory as the `/terraform` directory inside the Docker container 
# and runs the `init` command using the `terraform` entrypoint defined in the `Dockerfile`.
docker run --rm -v $(pwd):/terraform terraform-docker init  
docker run --rm -v $(pwd):/terraform terraform-docker plan