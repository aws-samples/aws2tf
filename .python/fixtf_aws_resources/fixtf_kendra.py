def aws_kendra_data_source(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2

def aws_kendra_experience(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	elif tt1=="data_source_ids" and tt2=="[]": skip=1
	elif tt1=="faq_ids" and tt2=="[]": skip=1

	return skip,t1,flag1,flag2

def aws_kendra_faq(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2

def aws_kendra_index(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kendra_query_suggestions_block_list(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2

def aws_kendra_thesaurus(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2

