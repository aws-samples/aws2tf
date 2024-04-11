#!/bin/bash -xe
echo ECS_CLUSTER=ECS-Schedule-Example-ECSCluster-GgVSDKVwSP3U >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $?          --stack ECS-Schedule-Example         --resource ECSAutoScalingGroup          --region eu-west-1
