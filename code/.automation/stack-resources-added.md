# CloudFormation Stack Resource Types - Added to stacks.py

**Date:** 2026-01-11  
**Total Resources Before:** 1,188  
**Total Resources After:** 1,277  
**Resources Added:** 89

## Summary

Added placeholder entries for 89 missing CloudFormation resource types to `code/stacks.py`. All entries use the pattern:
```python
elif type == "AWS::Service::ResourceType": common.call_resource("aws_null", type+" "+pid)
```

This allows aws2tf to recognize these resource types when importing CloudFormation stacks, even though full implementation is pending.

## Resources Added by Service

### AWS::AIOps (CloudWatch Investigations)
- AWS::AIOps::Investigation

### AWS::ARCRegionSwitch (ARC Region Switch)
- AWS::ARCRegionSwitch::RegionSwitch

### AWS::ASK (Alexa Skills Kit)
- AWS::ASK::Skill

### AWS::ApplicationSignals (CloudWatch Application Signals)
- AWS::ApplicationSignals::ServiceLevelObjective

### AWS::AppTest (Mainframe Modernization Application Testing)
- AWS::AppTest::TestCase

### AWS::BCMDataExports (AWS Data Exports)
- AWS::BCMDataExports::Export

### AWS::Bedrock (Amazon Bedrock) - 11 resources
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
- AWS::BedrockAgentCore::AgentVersion

### AWS::Billing (AWS Billing)
- AWS::Billing::BillingView

### AWS::BillingConductor (AWS Billing Conductor) - 4 resources
- AWS::BillingConductor::BillingGroup
- AWS::BillingConductor::CustomLineItem
- AWS::BillingConductor::PricingPlan
- AWS::BillingConductor::PricingRule

### AWS::Cases (Amazon Connect Cases) - 2 resources
- AWS::Cases::Domain
- AWS::Cases::IntegrationAssociation

### AWS::CleanRoomsML (CleanRooms ML)
- AWS::CleanRoomsML::TrainingDataset

### AWS::CodeConnections (AWS CodeConnections) - 3 resources
- AWS::CodeConnections::Connection
- AWS::CodeConnections::RepositoryLink
- AWS::CodeConnections::SyncConfiguration

### AWS::ConnectCampaignsV2 (Amazon Connect Outbound Campaigns V2)
- AWS::ConnectCampaignsV2::Campaign

### AWS::CUR (AWS Cost and Usage Report)
- AWS::CUR::ReportDefinition

### AWS::Deadline (AWS Deadline Cloud) - 9 resources
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
- AWS::DevOpsAgent::AgentConfiguration

### AWS::DSQL (Amazon Aurora DSQL)
- AWS::DSQL::Cluster

### AWS::ECS (Amazon ECS)
- AWS::ECS::ExpressGatewayService

### AWS::EVS (Amazon Elastic VMware Service)
- AWS::EVS::Cluster

### AWS::GameLiftStreams (Amazon GameLift Streams)
- AWS::GameLiftStreams::Stream

### AWS::IoTFleetWise (AWS IoT FleetWise) - 6 resources
- AWS::IoTFleetWise::Campaign
- AWS::IoTFleetWise::DecoderManifest
- AWS::IoTFleetWise::Fleet
- AWS::IoTFleetWise::ModelManifest
- AWS::IoTFleetWise::SignalCatalog
- AWS::IoTFleetWise::Vehicle

### AWS::IoTManagedIntegrations (Managed integrations for AWS IoT Device Management)
- AWS::IoTManagedIntegrations::Integration

### AWS::Invoicing (AWS Invoicing)
- AWS::Invoicing::InvoiceUnit

### AWS::LaunchWizard (AWS Launch Wizard)
- AWS::LaunchWizard::Deployment

### AWS::LookoutEquipment (Amazon Lookout for Equipment)
- AWS::LookoutEquipment::InferenceScheduler

### AWS::MPA (Multi-party approval)
- AWS::MPA::ApprovalRuleTemplate

### AWS::Notifications (Notifications) - 7 resources
- AWS::Notifications::ChannelAssociation
- AWS::Notifications::EventRule
- AWS::Notifications::ManagedNotificationAccountContactAssociation
- AWS::Notifications::ManagedNotificationAdditionalChannelAssociation
- AWS::Notifications::NotificationConfiguration
- AWS::Notifications::NotificationHub
- AWS::Notifications::OrganizationalUnitAssociation

### AWS::NotificationsContacts (NotificationsContacts)
- AWS::NotificationsContacts::EmailContact

### AWS::ObservabilityAdmin (CloudWatch Observability Admin)
- AWS::ObservabilityAdmin::ObservabilityConfiguration

### AWS::ODB (Oracle Database@AWS)
- AWS::ODB::DatabaseInstance

### AWS::PaymentCryptography (AWS Payment Cryptography) - 2 resources
- AWS::PaymentCryptography::Alias
- AWS::PaymentCryptography::Key

### AWS::PCAConnectorSCEP (AWS Private Certificate Authority Connector for SCEP) - 2 resources
- AWS::PCAConnectorSCEP::Challenge
- AWS::PCAConnectorSCEP::Connector

### AWS::PCS (AWS PCS) - 3 resources
- AWS::PCS::Cluster
- AWS::PCS::ComputeNodeGroup
- AWS::PCS::Queue

### AWS::QBusiness (Amazon Q Business) - 6 resources
- AWS::QBusiness::Application
- AWS::QBusiness::DataSource
- AWS::QBusiness::Index
- AWS::QBusiness::Plugin
- AWS::QBusiness::Retriever
- AWS::QBusiness::WebExperience

### AWS::Rbin (Recycle Bin)
- AWS::Rbin::Rule

### AWS::Route53Profiles (Amazon Route 53 Profiles) - 3 resources
- AWS::Route53Profiles::Profile
- AWS::Route53Profiles::ProfileAssociation
- AWS::Route53Profiles::ProfileResourceAssociation

### AWS::RTBFabric (AWS RTB Fabric)
- AWS::RTBFabric::Endpoint

### AWS::SMSVOICE (AWS End User Messaging SMS) - 4 resources
- AWS::SMSVOICE::ConfigurationSet
- AWS::SMSVOICE::OptOutList
- AWS::SMSVOICE::PhoneNumber
- AWS::SMSVOICE::Pool

### AWS::SSMGuiConnect (AWS Systems Manager GUI Connect)
- AWS::SSMGuiConnect::Preferences

### AWS::SSMQuickSetup (AWS Systems Manager Quick Setup)
- AWS::SSMQuickSetup::ConfigurationManager

## Next Steps

These placeholder entries allow aws2tf to recognize and log these resource types when encountered in CloudFormation stacks. To fully implement support for any of these resources:

1. **Check Terraform Support**: Verify the resource exists in the Terraform AWS provider
2. **Add to aws_dict.py**: Define the boto3 client and API methods
3. **Create Get Function**: Implement `get_aws_<resource>()` in appropriate file
4. **Create Handler**: Implement `aws_<resource>()` in appropriate fixtf file
5. **Test**: Follow the testing procedure in `.kiro/steering/new-resource-testing.md`
6. **Update stacks.py**: Replace `aws_null` with actual resource type

## Priority for Implementation

Based on service adoption and user demand:

**High Priority:**
- AWS::Bedrock::* (AI/ML services)
- AWS::QBusiness::* (Amazon Q)
- AWS::Notifications::* (Cross-service notifications)
- AWS::Route53Profiles::* (DNS management)

**Medium Priority:**
- AWS::Deadline::* (Media rendering)
- AWS::IoTFleetWise::* (Automotive IoT)
- AWS::BillingConductor::* (Cost management)

**Low Priority:**
- AWS::EVS::Cluster (VMware migration)
- AWS::ODB::DatabaseInstance (Oracle database)
- AWS::PCS::* (Parallel computing)
