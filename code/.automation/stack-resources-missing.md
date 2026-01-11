# CloudFormation Stack Resource Types - Missing from stacks.py

This document lists AWS CloudFormation resource types that are documented in AWS but not yet implemented in `code/stacks.py`.

**Analysis Date:** 2026-01-11  
**Total Implemented in stacks.py:** 1,188 resource types  
**Status:** This is a preliminary analysis based on AWS documentation

## Methodology

This analysis compares:
1. CloudFormation resource types currently handled in `code/stacks.py`
2. AWS CloudFormation resource type reference documentation
3. Known AWS services with CloudFormation support

## Missing Resource Types by Service

### AWS::AIOps (CloudWatch Investigations)
- AWS::AIOps::Investigation (New service - CloudWatch investigations)

### AWS::Alexa (Alexa Skills Kit)
- AWS::ASK::Skill

### AWS::ApplicationSignals (CloudWatch Application Signals)
- AWS::ApplicationSignals::ServiceLevelObjective (New service)

### AWS::AppTest (Mainframe Modernization Application Testing)
- AWS::AppTest::TestCase (New service)

### AWS::ARCRegionSwitch (ARC Region Switch)
- AWS::ARCRegionSwitch::RegionSwitch (New service)

### AWS::BCMDataExports (AWS Data Exports)
- AWS::BCMDataExports::Export (New service - Cost and Usage Report exports)

### AWS::Bedrock (Amazon Bedrock)
- AWS::Bedrock::Agent
- AWS::Bedrock::AgentAlias
- AWS::Bedrock::DataSource
- AWS::Bedrock::FlowAlias
- AWS::Bedrock::FlowVersion
- AWS::Bedrock::Guardrail
- AWS::Bedrock::GuardrailVersion
- AWS::Bedrock::KnowledgeBase
- AWS::Bedrock::Prompt
- AWS::Bedrock::PromptVersion

### AWS::BedrockAgentCore (Bedrock Agent Core)
- AWS::BedrockAgentCore::AgentVersion (New service)

### AWS::Billing (AWS Billing)
- AWS::Billing::BillingView (New service)

### AWS::BillingConductor (AWS Billing Conductor)
- AWS::BillingConductor::BillingGroup
- AWS::BillingConductor::CustomLineItem
- AWS::BillingConductor::PricingPlan
- AWS::BillingConductor::PricingRule

### AWS::Cases (Amazon Connect Cases)
- AWS::Cases::Domain
- AWS::Cases::IntegrationAssociation

### AWS::CleanRoomsML (CleanRooms ML)
- AWS::CleanRoomsML::TrainingDataset (New service)

### AWS::CodeConnections (AWS CodeConnections)
- AWS::CodeConnections::Connection
- AWS::CodeConnections::RepositoryLink
- AWS::CodeConnections::SyncConfiguration
**Note:** These may replace AWS::CodeStarConnections resources

### AWS::ConnectCampaignsV2 (Amazon Connect Outbound Campaigns V2)
- AWS::ConnectCampaignsV2::Campaign (New version)

### AWS::CUR (AWS Cost and Usage Report)
- AWS::CUR::ReportDefinition

### AWS::Deadline (AWS Deadline Cloud)
- AWS::Deadline::Farm
- AWS::Deadline::Fleet
- AWS::Deadline::LicenseEndpoint
- AWS::Deadline::MeteredProduct
- AWS::Deadline::Monitor
- AWS::Deadline::Queue
- AWS::Deadline::QueueEnvironment
- AWS::Deadline::QueueFleetAssociation
- AWS::Deadline::StorageProfile

### AWS::DevOpsAgent (AWS DevOps Agent)
- AWS::DevOpsAgent::AgentConfiguration (New service)

### AWS::DSQL (Amazon Aurora DSQL)
- AWS::DSQL::Cluster (New service - Aurora DSQL)

### AWS::ECS (Amazon ECS - New Resources)
- AWS::ECS::ExpressGatewayService (New - not in stacks.py)

### AWS::EVS (Amazon Elastic VMware Service)
- AWS::EVS::Cluster (New service)

### AWS::GameLiftStreams (Amazon GameLift Streams)
- AWS::GameLiftStreams::Stream (New service)

### AWS::IoTFleetWise (AWS IoT FleetWise)
- AWS::IoTFleetWise::Campaign
- AWS::IoTFleetWise::DecoderManifest
- AWS::IoTFleetWise::Fleet
- AWS::IoTFleetWise::ModelManifest
- AWS::IoTFleetWise::SignalCatalog
- AWS::IoTFleetWise::Vehicle

### AWS::IoTManagedIntegrations (Managed integrations for AWS IoT Device Management)
- AWS::IoTManagedIntegrations::Integration (New service)

### AWS::Invoicing (AWS Invoicing)
- AWS::Invoicing::InvoiceUnit (New service)

### AWS::LaunchWizard (AWS Launch Wizard)
- AWS::LaunchWizard::Deployment

### AWS::LookoutEquipment (Amazon Lookout for Equipment)
- AWS::LookoutEquipment::InferenceScheduler

### AWS::LookoutMetrics (Amazon Lookout for Metrics)
**Note:** Resources exist in stacks.py but service may have additional resources

### AWS::LookoutVision (Amazon Lookout for Vision)
**Note:** Resources exist in stacks.py but service may have additional resources

### AWS::MPA (Multi-party approval)
- AWS::MPA::ApprovalRuleTemplate (New service)

### AWS::Notifications (Notifications)
- AWS::Notifications::ChannelAssociation
- AWS::Notifications::EventRule
- AWS::Notifications::ManagedNotificationAccountContactAssociation
- AWS::Notifications::ManagedNotificationAdditionalChannelAssociation
- AWS::Notifications::NotificationConfiguration
- AWS::Notifications::NotificationHub
- AWS::Notifications::OrganizationalUnitAssociation

### AWS::NotificationsContacts (NotificationsContacts)
- AWS::NotificationsContacts::EmailContact (New service)

### AWS::ObservabilityAdmin (CloudWatch Observability Admin)
- AWS::ObservabilityAdmin::ObservabilityConfiguration (New service)

### AWS::ODB (Oracle Database@AWS)
- AWS::ODB::DatabaseInstance (New service)

### AWS::PaymentCryptography (AWS Payment Cryptography)
- AWS::PaymentCryptography::Alias
- AWS::PaymentCryptography::Key

### AWS::PCAConnectorSCEP (AWS Private Certificate Authority Connector for SCEP)
- AWS::PCAConnectorSCEP::Challenge
- AWS::PCAConnectorSCEP::Connector

### AWS::PCS (AWS PCS)
- AWS::PCS::Cluster
- AWS::PCS::ComputeNodeGroup
- AWS::PCS::Queue

### AWS::QBusiness (Amazon Q Business)
- AWS::QBusiness::Application
- AWS::QBusiness::DataSource
- AWS::QBusiness::Index
- AWS::QBusiness::Plugin
- AWS::QBusiness::Retriever
- AWS::QBusiness::WebExperience

### AWS::QLDB (Amazon QLDB)
**Note:** Resources are commented out in stacks.py:
```python
#            elif type == "AWS::QLDB::Ledger": common.call_resource("aws_null", type+" "+pid)
#            elif type == "AWS::QLDB::Stream": common.call_resource("aws_null", type+" "+pid)
```
These should be uncommented and properly implemented.

### AWS::Rbin (Recycle Bin)
- AWS::Rbin::Rule

### AWS::Route53Profiles (Amazon Route 53 Profiles)
- AWS::Route53Profiles::Profile
- AWS::Route53Profiles::ProfileAssociation
- AWS::Route53Profiles::ProfileResourceAssociation

### AWS::RTBFabric (AWS RTB Fabric)
- AWS::RTBFabric::Endpoint (New service)

### AWS::S3Tables (Amazon S3 Tables)
**Note:** Some resources exist in stacks.py but may be incomplete

### AWS::S3Vectors (Amazon S3 Vectors)
**Note:** New service - may not have all resources implemented

### AWS::SecurityLake (Amazon Security Lake)
**Note:** Service exists but may have additional resources not in stacks.py

### AWS::SMSVOICE (AWS End User Messaging SMS)
- AWS::SMSVOICE::ConfigurationSet
- AWS::SMSVOICE::OptOutList
- AWS::SMSVOICE::PhoneNumber
- AWS::SMSVOICE::Pool

### AWS::SSMGuiConnect (AWS Systems Manager GUI Connect)
- AWS::SSMGuiConnect::Preferences (New service)

### AWS::SSMQuickSetup (AWS Systems Manager Quick Setup)
- AWS::SSMQuickSetup::ConfigurationManager (New service)

## Services with Potential Missing Resources

The following services are in stacks.py but may have additional resource types not yet implemented:

1. **AWS::EC2** - Very large service, may have new resource types
2. **AWS::Lambda** - May have new resource types for recent features
3. **AWS::RDS** - May have new resource types for recent features
4. **AWS::S3** - May have new resource types for recent features
5. **AWS::IAM** - May have new resource types for recent features

## Implementation Priority Recommendations

### High Priority (Commonly Used Services)
1. AWS::Bedrock::* - AI/ML service gaining adoption
2. AWS::QBusiness::* - New Q Business service
3. AWS::Notifications::* - Cross-service notification system
4. AWS::Route53Profiles::* - DNS management enhancement
5. AWS::Rbin::Rule - Data retention compliance

### Medium Priority (Specialized Services)
1. AWS::Deadline::* - Media/rendering workloads
2. AWS::IoTFleetWise::* - Automotive/IoT applications
3. AWS::PaymentCryptography::* - Financial services
4. AWS::BillingConductor::* - Cost management

### Low Priority (Niche Services)
1. AWS::EVS::Cluster - VMware migration
2. AWS::ODB::DatabaseInstance - Oracle database service
3. AWS::PCS::* - Parallel computing
4. AWS::RTBFabric::* - Specialized networking

## Notes

1. **New Services**: Many of these are recently launched AWS services (2024-2025)
2. **Service Evolution**: AWS continuously adds new resource types to existing services
3. **Terraform Support**: Check if Terraform AWS provider supports these resources before implementing
4. **API Availability**: Verify boto3 API support for listing/describing these resources

## Next Steps

1. Verify which resources have Terraform AWS provider support
2. Check boto3 API availability for each resource type
3. Prioritize implementation based on user demand
4. Create tracking issues for high-priority missing resources

## References

- [AWS CloudFormation Resource Type Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html)
- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
