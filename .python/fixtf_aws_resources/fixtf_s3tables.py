def aws_s3tables_table_bucket(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3tables_table(t1,tt1,tt2,flag1,flag2):
    skip=0
    #if tt1=="namespace" and tt2 !="null":
    #    t1=tt1+" = aws_s3tables_namespace."+tt2+".id\n"
    if tt1=="table_bucket_arn" and tt2 !="null":
        barn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
        t1=tt1+" = aws_s3tables_table_bucket."+barn+".arn\n"
 
    
    return skip,t1,flag1,flag2

def aws_s3tables_namespace(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1=="table_bucket_arn" and tt2 !="null":
        barn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
        t1=tt1+" = aws_s3tables_table_bucket."+barn+".arn\n"
    return skip,t1,flag1,flag2