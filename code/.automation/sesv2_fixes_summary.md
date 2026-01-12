# SESv2 Resources - boto3 Method Fixes

## Summary
Fixed 6 sesv2 resources that had incorrect boto3 method names in aws_dict.py.

## Fixes Applied

### 1. aws_sesv2_configuration_set_event_destination
- **Error:** `KeyError('describe_configuration_set_event_destination')`
- **Fix:** Changed `descfn` from `describe_configuration_set_event_destination` to `get_configuration_set_event_destinations`
- **Import ID:** Composite format `configuration_set_name|event_destination_name`
- **Get Function:** Created custom function to handle composite IDs

### 2. aws_sesv2_email_identity
- **Error:** `OperationNotPageableError('Operation cannot be paginated: list_email_identities')`
- **Fix:** Changed from paginator to direct API call in get function
- **Import ID:** Email identity name (e.g., `example.com`)

### 3. aws_sesv2_email_identity_feedback_attributes
- **Error:** `KeyError('describe_email_identity_feedback_attributes')`
- **Fix:** Changed `descfn` from `describe_email_identity_feedback_attributes` to `get_email_identity`
- **Import ID:** Email identity name
- **Get Function:** Created custom function that checks for FeedbackForwardingStatus in get_email_identity response

### 4. aws_sesv2_account_vdm_attributes
- **Error:** Would have failed with `KeyError('describe_account_vdm_attributes')`
- **Fix:** Changed `descfn` from `describe_account_vdm_attributes` to `get_account`
- **Import ID:** Fixed singleton ID `ses-account-vdm-attributes`
- **Get Function:** Already existed, uses get_account and checks for VdmAttributes

### 5. aws_sesv2_dedicated_ip_assignment
- **Error:** Would have failed with `KeyError('describe_dedicated_ip_assignment')`
- **Fix:** Changed `descfn` from `describe_dedicated_ip_assignment` to `get_dedicated_ips`
- **Import ID:** Composite format `ip,pool_name` (comma separator)
- **Get Function:** Created custom function to handle composite IDs

### 6. aws_sesv2_email_identity_mail_from_attributes
- **Error:** Would have failed with `KeyError('describe_email_identity_mail_from_attributes')`
- **Fix:** Changed `descfn` from `describe_email_identity_mail_from_attributes` to `get_email_identity`
- **Import ID:** Email identity name
- **Get Function:** Created custom function that checks for MailFromAttributes.MailFromDomain in get_email_identity response

## Files Modified

### code/fixtf_aws_resources/aws_dict.py
- Updated 6 resource definitions with correct boto3 method names

### code/get_aws_resources/aws_sesv2.py
- Added `get_aws_sesv2_configuration_set_event_destination()` - handles composite IDs
- Modified `get_aws_sesv2_email_identity()` - removed paginator, use direct call
- Added `get_aws_sesv2_email_identity_feedback_attributes()` - checks FeedbackForwardingStatus
- Added `get_aws_sesv2_dedicated_ip_assignment()` - handles composite IDs with comma separator
- Added `get_aws_sesv2_email_identity_mail_from_attributes()` - checks MailFromAttributes

## Verification
All boto3 methods now exist and are correctly named. Verified with check_sesv2_methods.py script.

## Notes
- SESv2 API uses `get_email_identity` to retrieve all identity attributes (feedback, mail-from, DKIM, etc.)
- Some resources are "attribute" resources that don't have separate list operations
- Composite ID resources require custom get functions to build the proper import IDs
