# Deprecated/Legacy AWS Resources

**Total Deprecated Resources:** 40
**Deprecated Service Groups:** 10

These resources are from AWS services that have been deprecated, discontinued, or replaced by newer services. Testing these resources is **not recommended** as they may be removed from AWS in the future.

---

## aws_cloudsearch

**Status:** Legacy service, largely replaced by Amazon OpenSearch Service

**Resources:**
- `aws_cloudsearch_domain`
- `aws_cloudsearch_domain_service_access_policy`

## aws_datapipeline

**Status:** Replaced by AWS Glue and AWS Step Functions

**Resources:**
- `aws_datapipeline_pipeline`
- `aws_datapipeline_pipeline_definition`

## aws_elastictranscoder

**Status:** Replaced by AWS Elemental MediaConvert

**Resources:**
- `aws_elastictranscoder_preset`

## aws_glacier

**Status:** Rebranded as Amazon S3 Glacier (now part of S3 service)

**Resources:**
- `aws_glacier_vault_lock`

## aws_inspector

**Status:** Replaced by AWS Inspector v2 (Inspector Classic is deprecated)

**Resources:**
- `aws_inspector_assessment_target`
- `aws_inspector_assessment_template`

## aws_opsworks

**Status:** Being phased out, replaced by other deployment tools (AWS Systems Manager, CodeDeploy)

**Resources:**
- `aws_opsworks_application`
- `aws_opsworks_custom_layer`
- `aws_opsworks_instance`
- `aws_opsworks_php_app_layer`
- `aws_opsworks_stack`
- `aws_opsworks_static_web_layer`

## aws_simpledb

**Status:** Legacy service, replaced by Amazon DynamoDB

**Resources:**
- `aws_simpledb_domain`

## aws_waf

**Status:** Replaced by AWS WAFv2 (WAF Classic is deprecated)

**Resources:**
- `aws_waf_byte_match_set`
- `aws_waf_geo_match_set`
- `aws_waf_ipset`
- `aws_waf_rate_based_rule`
- `aws_waf_regex_match_set`
- `aws_waf_regex_pattern_set`
- `aws_waf_rule`
- `aws_waf_rule_group`
- `aws_waf_size_constraint_set`
- `aws_waf_sql_injection_match_set`
- `aws_waf_xss_match_set`

## aws_wafregional

**Status:** Replaced by AWS WAFv2 (WAF Classic Regional is deprecated)

**Resources:**
- `aws_wafregional_byte_match_set`
- `aws_wafregional_geo_match_set`
- `aws_wafregional_ipset`
- `aws_wafregional_rate_based_rule`
- `aws_wafregional_regex_match_set`
- `aws_wafregional_regex_pattern_set`
- `aws_wafregional_rule`
- `aws_wafregional_rule_group`
- `aws_wafregional_size_constraint_set`
- `aws_wafregional_sql_injection_match_set`
- `aws_wafregional_web_acl`
- `aws_wafregional_web_acl_association`
- `aws_wafregional_xss_match_set`

## aws_worklink

**Status:** Service discontinued by AWS (December 2021)

**Resources:**
- `aws_worklink_fleet`
