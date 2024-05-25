def aws_kinesis_firehose_delivery_stream(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="custom_time_zone" and tt2=="null":
		t1=tt1+' = "UTC"\n'
	if tt1=="name":
		t1=t1+"\n lifecycle {\n   ignore_changes = [extended_s3_configuration[0].custom_time_zone]\n}\n"
	return skip,t1,flag1,flag2

