#!/usr/bin/env python3





# end part 1

st1 = False
fr = open('final-cf-resources.dat', 'r')
of = open('cf-stack.py', 'w')
line = fr.readline()
while line:
    line = fr.readline()
    myline = str(line).strip()
    # if "START AUTOGEN" in myline: st1=True
    of.write('\t\t\telif type == "'+myline+'": common.call_resource("aws_null", type+" "+pid)\n')


fr.close()
of.close()


#    elif type == "net" or type == "kms" or type == "iam" or type == "lattice" or type == "test":
#        all_types = resources.resource_types(type)
#        for i in all_types:
#            common.call_resource(i, id)
#
# clfn, descfn, topkey, key, filterid = resources.resource_data(type, id)
#    elif type == "aws_iam_instance_profile":
#        clfn="iam";descfn="get_instance_profile";topkey="InstanceProfile";key="InstanceProfileName";filterid=key
#
#
