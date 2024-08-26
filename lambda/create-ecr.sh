aws ecr delete-repository --repository-name laws2tf --force
aws ecr create-repository --repository-name laws2tf --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE