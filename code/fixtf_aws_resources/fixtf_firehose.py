import context

def aws_kinesis_firehose_delivery_stream(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="custom_time_zone" and tt2=="null":
		t1=tt1+' = "UTC"\n'
	elif tt1=="name":
		t1=t1+"\n lifecycle {\n   ignore_changes = [extended_s3_configuration[0].custom_time_zone]\n}\n"
	elif tt1=="destination_id": skip=1
	elif tt1=="msk_source_configuration":
		context.kinesismsk=True

	elif tt1=="server_side_encryption" and context.kinesismsk : skip=1


	return skip,t1,flag1,flag2

