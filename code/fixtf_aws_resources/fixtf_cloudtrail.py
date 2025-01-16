def aws_cloudtrail(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="ends_with" and tt2=="[]": skip=1
	if tt1=="not_ends_with" and tt2=="[]": skip=1
	if tt1=="starts_with" and tt2=="[]": skip=1
	if tt1=="not_starts_with" and tt2=="[]": skip=1
	if tt1=="not_equals" and tt2=="[]": skip=1
	if tt1=="equals" and tt2=="[]": skip=1

	return skip,t1,flag1,flag2

def aws_cloudtrail_event_data_store(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="ends_with" and tt2=="[]": skip=1
	if tt1=="not_ends_with" and tt2=="[]": skip=1
	if tt1=="starts_with" and tt2=="[]": skip=1
	if tt1=="not_starts_with" and tt2=="[]": skip=1
	if tt1=="not_equals" and tt2=="[]": skip=1
	if tt1=="equals" and tt2=="[]": skip=1
	return skip,t1,flag1,flag2

