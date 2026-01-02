# CloudWatch Resources Testing Progress

**Date:** 2026-01-02
**Status:** In Progress

## Completed Tests

### Passed (2)
- [x] `aws_cloudwatch_composite_alarm` - ✓ PASSED (requires metric alarms, 0 drift)
- [x] `aws_cloudwatch_dashboard` - ✓ PASSED (simple JSON config, 0 drift)

### Failed (1)
- [x] `aws_cloudwatch_contributor_managed_insight_rule` - ✗ FAILED (composite ID format)
  - Error: "unexpected format for ID, expected more than one part"
  - Requires special handling for composite IDs
  - Test configuration deployed successfully, only import failed

## Remaining Tests (11)

### EventBridge Resources (CloudWatch Events)
- [ ] `aws_cloudwatch_event_api_destination`
- [ ] `aws_cloudwatch_event_archive`
- [ ] `aws_cloudwatch_event_bus_policy`
- [ ] `aws_cloudwatch_event_connection`
- [ ] `aws_cloudwatch_event_endpoint`
- [ ] `aws_cloudwatch_event_permission`

### CloudWatch Logs Resources
- [ ] `aws_cloudwatch_log_data_protection_policy`
- [ ] `aws_cloudwatch_log_destination_policy`
- [ ] `aws_cloudwatch_log_metric_filter`
- [ ] `aws_cloudwatch_log_resource_policy`
- [ ] `aws_cloudwatch_log_subscription_filter`

## Notes

### aws_cloudwatch_contributor_managed_insight_rule
- Get function created in `code/get_aws_resources/aws_cloudwatch.py`
- Filters for managed rules using `ManagedRule` field
- Successfully creates resources but import fails due to composite ID requirement
- Documented in test-failed.md
- Re-commented in aws_not_implemented.py with reason

### Next Steps
1. Test `aws_cloudwatch_event_api_destination` (EventBridge API destination)
2. Continue with remaining EventBridge resources
3. Test CloudWatch Logs policy and filter resources
4. Update tracking files after each test

## Testing Approach
- EventBridge resources may require connections, event buses, or archives as dependencies
- CloudWatch Logs resources may require log groups as dependencies
- Policy resources typically require parent resources (log groups, destinations, etc.)
