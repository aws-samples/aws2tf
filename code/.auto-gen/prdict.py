#!/usr/bin/env python3

st1 = False
fr = open('../resources.py', 'r')
line = fr.readline()
while line:
    line = fr.readline()
    myline = str(line).strip()
    # if "START AUTOGEN" in myline: st1=True
    # if st1:
    if '#' in myline:
        continue
    if 'aws_' in myline and 'elif' in myline and '[' not in myline:
        awsr = myline.split('"')[1]
        line = fr.readline()
        myline2 = str(line).strip()
        clfn = myline2.split(';')[0].split('=')[1]
        descfn = myline2.split(';')[1].split('=')[1].strip('\"')
        topkey = myline2.split(';')[2].split('=')[1].strip('\"')
        key = myline2.split(';')[3].split('=')[1].strip('\"')
        filterid = myline2.split(';')[4].split('=')[1].strip('\"')
        try:
            clfn = clfn.split('"')[1]
        except:
            print("indexerror on clfn="+clfn)
            print(myline)
            print(myline2)
            exit()
        # print(awsr+": cl="+clfn+": des="+descfn+": tk="+topkey+": ky="+key+"; fil="+filterid)
        if filterid == 'key':
            filterid = key
        print(awsr+": cl="+clfn+": des="+descfn+": tk=" +
              topkey+": ky="+key+"; fil="+filterid)
        of = open('aws_dict.py', 'a')
        of.write(awsr + ' = {\n')
        of.write('\t"clfn":\t\t"' + clfn + '",\n')
        of.write('\t"descfn":\t"' + descfn + '",\n')
        of.write('\t"topkey":\t"' + topkey + '",\n')
        of.write('\t"key":\t\t"' + key + '",\n')
        of.write('\t"filterid":\t"' + filterid + '"\n')
        of.write('}\n\n')


of.close()

# end part 1

st1 = False
fr = open('../resources.py', 'r')
line = fr.readline()
of = open('aws_dict.py', 'a')
of.write('aws_resources = {\n')
while line:
    line = fr.readline()
    myline = str(line).strip()
    # if "START AUTOGEN" in myline: st1=True
    # if st1:
    if '#' in myline:
        continue
    if 'aws_' in myline and 'elif' in myline and '[' not in myline:
        awsr = myline.split('"')[1]
        print(awsr)
        of.write('\t"'+awsr+'": ' + awsr + ',\n')


of.write('}\n\n')
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
