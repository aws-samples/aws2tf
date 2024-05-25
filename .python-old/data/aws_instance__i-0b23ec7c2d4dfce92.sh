#!/bin/bash -xe
sudo yum update -y aws-cfn-bootstrap
sudo dnf update -y
sudo dnf install -y mariadb105
sudo dnf install -y postgresql15
