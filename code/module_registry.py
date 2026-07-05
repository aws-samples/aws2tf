"""Service module imports and registry for aws2tf resource dispatch."""

from get_aws_resources import aws_acm
from get_aws_resources import aws_amp
from get_aws_resources import aws_amplify
from get_aws_resources import aws_athena
from get_aws_resources import aws_autoscaling
from get_aws_resources import aws_apigateway
from get_aws_resources import aws_apigatewayv2
from get_aws_resources import aws_appmesh
from get_aws_resources import aws_application_autoscaling
from get_aws_resources import aws_appstream
from get_aws_resources import aws_batch
from get_aws_resources import aws_backup
from get_aws_resources import aws_bedrock
from get_aws_resources import aws_bedrock_agent
from get_aws_resources import aws_bedrock_agentcore_control
from get_aws_resources import aws_cleanrooms
from get_aws_resources import aws_cloud9
from get_aws_resources import aws_cloudformation
from get_aws_resources import aws_cloudfront
from get_aws_resources import aws_cloudtrail
from get_aws_resources import aws_cloudwatch
from get_aws_resources import aws_codebuild
from get_aws_resources import aws_codecommit
from get_aws_resources import aws_codeartifact
from get_aws_resources import aws_codedeploy
from get_aws_resources import aws_codepipeline
from get_aws_resources import aws_codeguruprofiler
from get_aws_resources import aws_codestar_notifications
from get_aws_resources import aws_cognito_identity
from get_aws_resources import aws_cognito_idp
from get_aws_resources import aws_config
from get_aws_resources import aws_connect
from get_aws_resources import aws_customer_profiles
from get_aws_resources import aws_datazone
from get_aws_resources import aws_devops_guru
from get_aws_resources import aws_directconnect
from get_aws_resources import aws_dms
from get_aws_resources import aws_docdb
from get_aws_resources import aws_ds
from get_aws_resources import aws_dynamodb
from get_aws_resources import aws_kms
from get_aws_resources import aws_ec2
from get_aws_resources import aws_ecs
from get_aws_resources import aws_efs
from get_aws_resources import aws_ecr_public
from get_aws_resources import aws_ecr
from get_aws_resources import aws_eks
from get_aws_resources import aws_elasticache
from get_aws_resources import aws_elbv2
from get_aws_resources import aws_emr
from get_aws_resources import aws_events
from get_aws_resources import aws_firehose
from get_aws_resources import aws_glue
from get_aws_resources import aws_guardduty
from get_aws_resources import aws_iam
from get_aws_resources import aws_kafka
from get_aws_resources import aws_kendra
from get_aws_resources import aws_kinesis
from get_aws_resources import aws_logs
from get_aws_resources import aws_lakeformation
from get_aws_resources import aws_lambda
from get_aws_resources import aws_license_manager
from get_aws_resources import aws_lightsail
from get_aws_resources import aws_memorydb
from get_aws_resources import aws_mwaa
from get_aws_resources import aws_neptune
from get_aws_resources import aws_network_firewall
from get_aws_resources import aws_networkmanager
from get_aws_resources import aws_organizations
from get_aws_resources import aws_opensearchserverless
from get_aws_resources import aws_ram
from get_aws_resources import aws_rds
from get_aws_resources import aws_redshift
from get_aws_resources import aws_redshift_serverless
from get_aws_resources import aws_resource_explorer_2
from get_aws_resources import aws_route53
from get_aws_resources import aws_route53resolver
from get_aws_resources import aws_s3
from get_aws_resources import aws_s3control
from get_aws_resources import aws_s3tables
from get_aws_resources import aws_s3vectors
from get_aws_resources import aws_sagemaker
from get_aws_resources import aws_schemas
from get_aws_resources import aws_scheduler
from get_aws_resources import aws_securityhub
from get_aws_resources import aws_secretsmanager
from get_aws_resources import aws_servicecatalog
from get_aws_resources import aws_servicediscovery
from get_aws_resources import aws_shield
from get_aws_resources import aws_ses
from get_aws_resources import aws_sesv2
from get_aws_resources import aws_signer
from get_aws_resources import aws_sns
from get_aws_resources import aws_sqs
from get_aws_resources import aws_ssm
from get_aws_resources import aws_sso_admin
from get_aws_resources import aws_transfer
from get_aws_resources import aws_vpc_lattice
from get_aws_resources import aws_waf
from get_aws_resources import aws_wafv2
from get_aws_resources import aws_workspaces
from get_aws_resources import aws_workspaces_web
from get_aws_resources import aws_xray

from fixtf_aws_resources import needid_dict
from fixtf_aws_resources import aws_no_import
from fixtf_aws_resources import aws_not_implemented

# Security Fix #2: Module registry to replace eval()
# This prevents arbitrary code execution via eval()
AWS_RESOURCE_MODULES = {
    'acm': aws_acm,
    'amp': aws_amp,
    'amplify': aws_amplify,
    'athena': aws_athena,
    'autoscaling': aws_autoscaling,
    'apigateway': aws_apigateway,
    'apigatewayv2': aws_apigatewayv2,
    'appmesh': aws_appmesh,
    'application-autoscaling': aws_application_autoscaling,
    'application_autoscaling': aws_application_autoscaling,
    'appstream': aws_appstream,
    'batch': aws_batch,
    'backup': aws_backup,
    'bedrock': aws_bedrock,
    'bedrock-agent': aws_bedrock_agent,
    'bedrock_agent': aws_bedrock_agent,
    'bedrock-agentcore-control': aws_bedrock_agentcore_control,
    'cleanrooms': aws_cleanrooms,
    'cloud9': aws_cloud9,
    'cloudformation': aws_cloudformation,
    'cloudfront': aws_cloudfront,
    'cloudtrail': aws_cloudtrail,
    'cloudwatch': aws_cloudwatch,
    'codebuild': aws_codebuild,
    'codecommit': aws_codecommit,
    'codeartifact': aws_codeartifact,
    'codedeploy': aws_codedeploy,
    'codepipeline': aws_codepipeline,
    'codeguruprofiler': aws_codeguruprofiler,
    'codestar-notifications': aws_codestar_notifications,
    'codestar_notifications': aws_codestar_notifications,
    'cognito-identity': aws_cognito_identity,
    'cognito_identity': aws_cognito_identity,
    'cognito-idp': aws_cognito_idp,
    'cognito_idp': aws_cognito_idp,
    'config': aws_config,
    'connect': aws_connect,
    'customer-profiles': aws_customer_profiles,
    'customer_profiles': aws_customer_profiles,
    'datazone': aws_datazone,
    'devops-guru': aws_devops_guru,
    'directconnect': aws_directconnect,
    'dms': aws_dms,
    'docdb': aws_docdb,
    'ds': aws_ds,
    'dynamodb': aws_dynamodb,
    'kms': aws_kms,
    'ec2': aws_ec2,
    'ecs': aws_ecs,
    'efs': aws_efs,
    'ecr-public': aws_ecr_public,
    'ecr_public': aws_ecr_public,
    'ecr': aws_ecr,
    'eks': aws_eks,
    'elasticache': aws_elasticache,
    'elbv2': aws_elbv2,
    'emr': aws_emr,
    'events': aws_events,
    'firehose': aws_firehose,
    'glue': aws_glue,
    'guardduty': aws_guardduty,
    'iam': aws_iam,
    'kafka': aws_kafka,
    'kendra': aws_kendra,
    'kinesis': aws_kinesis,
    'logs': aws_logs,
    'lakeformation': aws_lakeformation,
    'lambda': aws_lambda,
    'license-manager': aws_license_manager,
    'license_manager': aws_license_manager,
    'lightsail': aws_lightsail,
    'memorydb': aws_memorydb,
    'mwaa': aws_mwaa,
    'neptune': aws_neptune,
    'network-firewall': aws_network_firewall,
    'network_firewall': aws_network_firewall,
    'networkmanager': aws_networkmanager,
    'organizations': aws_organizations,
    'opensearchserverless': aws_opensearchserverless,
    'ram': aws_ram,
    'rds': aws_rds,
    'redshift': aws_redshift,
    'redshift-serverless': aws_redshift_serverless,
    'redshift_serverless': aws_redshift_serverless,
    'resource-explorer-2': aws_resource_explorer_2,
    'resource_explorer_2': aws_resource_explorer_2,
    'route53': aws_route53,
    'route53resolver': aws_route53resolver,
    's3': aws_s3,
    's3control': aws_s3control,
    's3tables': aws_s3tables,
    's3vectors': aws_s3vectors,
    'sagemaker': aws_sagemaker,
    'schemas': aws_schemas,
    'scheduler': aws_scheduler,
    'securityhub': aws_securityhub,
    'secretsmanager': aws_secretsmanager,
    'servicecatalog': aws_servicecatalog,
    'servicediscovery': aws_servicediscovery,
    'shield': aws_shield,
    'ses': aws_ses,
    'sesv2': aws_sesv2,
    'signer': aws_signer,
    'sns': aws_sns,
    'sqs': aws_sqs,
    'ssm': aws_ssm,
    'sso-admin': aws_sso_admin,
    'sso_admin': aws_sso_admin,
    'transfer': aws_transfer,
    'vpc-lattice': aws_vpc_lattice,
    'vpc_lattice': aws_vpc_lattice,
    'waf': aws_waf,
    'wafv2': aws_wafv2,
    'workspaces': aws_workspaces,
    'workspaces-web': aws_workspaces_web,
    'xray': aws_xray,
}
