# Install python v3.8 on Amazon Linux 2

sudo yum remove python3
sudo amazon-linux-extras install python3.8
sudo ln -s /usr/bin/python3.8 /usr/bin/python3
sudo ln -s /usr/bin/pip3.8 /usr/bin/pip3
pip3 install boto3 requests