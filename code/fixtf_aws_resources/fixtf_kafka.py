import common
import globals

def aws_msk_broker_nodes(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_msk_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="log_group" and tt2!="null":
		t1=tt1+" = aws_cloudwatch_log_group."+tt2+".name\n"
		common.add_dependancy("aws_cloudwatch_log_group",tt2)
	elif tt1=="delivery_stream" and tt2!="null":
		karn="arn:aws:firehose:"+globals.region+":"+globals.acc+":deliverystream/"+tt2
		tarn=karn.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
		t1=tt1+" = aws_kinesis_firehose_delivery_stream."+tarn+".name\n"
		common.add_dependancy("aws_kinesis_firehose_delivery_stream",tt2)
	elif tt1=="arn" and tt2.startswith("arn:aws:kafka") and ":configuration:" in tt2:
		tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
		t1=tt1+" = aws_msk_configuration."+tarn+".arn\n"
		# pass the arn
		common.add_dependancy("aws_msk_configuration", tt2)
	elif tt1=="volume_throughput" and tt2=="0": skip=1
	#elif tt1=="arn" and tt2!="null":
	#	t1=tt1+" = aws_msk_configuration."+tarn+".arn\n"



		
	return skip,t1,flag1,flag2

def aws_msk_cluster_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_msk_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_msk_kafka_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_msk_replicator(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_msk_scram_secret_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="cluster_arn":
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1+" = aws_msk_cluster."+tarn+".arn\n"
		#common.add_dependancy("aws_msk_cluster", tt2)
	return skip,t1,flag1,flag2

def aws_msk_serverless_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_msk_vpc_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

