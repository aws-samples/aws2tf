excl = {}
with open('../fixtf_aws_resources/aws_no_import.py', 'r') as f:
    for line in f.readlines():
        if '#' not in line:
            if ":" in line and "aws_" in line:
                myline = line.strip('\n').split(
                    ':')[0].strip().strip(',').strip('"')
                excl[myline] = True

with open('../fixtf_aws_resources/aws_not_implemented.py', 'r') as f:
    for line in f.readlines():
        if '#' not in line:
            if ":" in line and "aws_" in line:
                myline = line.strip('\n').split(
                    ':')[0].strip().strip(',').strip('"')
                excl[myline] = True

#for j in excl.keys():
#    exl=str(j)
#    #print(exl)
#    if exl.startswith("aws_rou"):
#        print(j)




dictl = {}
with open('../fixtf_aws_resources/aws_dict.py', 'r') as f:
    for line in f.readlines():
        if '#' not in line:
            if ":" in line and "aws_" in line:
                myline = line.strip('\n').split(':')[-1].strip().strip(',')
                dictl[myline] = True

dictl=dict(sorted(dictl.items()))

with open('../../Terraform-Resources.md', 'w') as f:
    print("\nTerraform resource types currently supported\n")
    f.write("\n## Terraform resource types currently supported\n\n")
    c = 0
    #for myline in dictl.keys():
    for myline,v in dictl.items():
        ms=str(myline)

        isfound = False
            # iterate mylist untik found
        for j in excl.keys():
                if str(myline) == str(j):  isfound = True

        if not isfound:
            print("* "+myline)
            f.write("* "+myline+"\n")
            c =+ 1
print("--------------------\n")
print("AWS Stack set types currectly supported\n")
dictl = {}
with open('../../StackSet-Resources.md', 'w') as f2:

    f2.write("\n## AWS Stack set types currectly supported\n\n")
    with open('../stacks.py', 'r') as f:
        for line in f.readlines():
            if '#' not in line:
                if "::" in line and "aws_" in line and "aws_null" not in line:
                    myline = line.strip('\n').split('==')[-1].split("common.")[0]
                    myline=myline.strip(' ').strip('"').strip('":')
                    dictl[myline] = True
    dictl=dict(sorted(dictl.items()))
    for j in dictl.keys():
        print("* "+j)
        f2.write("* "+j+"\n")
