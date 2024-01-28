def aws_acmpca_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_acmpca_certificate_authority(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "expiration_in_days":
		tt2=tt2.strip('\"')
		if tt2 == "0": skip=1
	return skip,t1,flag1,flag2

def aws_acmpca_certificate_authority_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_acmpca_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_acmpca_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

