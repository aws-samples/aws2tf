#!/usr/bin/env python3
rlist={}
print("check dict doesn't have resources that don't exist")

try:
    file = open('master-resources-list.dat', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()

        rlist[line] = True

except:
    print("No master-resource-list.dat file found ?")
    pass



dictl={}
with open('../aws_resources/aws_dict.py', 'r') as f:
    for line in f.readlines():
        if '#' not in line:
            if ":" in line and "aws_" in line:
                myline=line.strip('\n').split(':')[-1].strip().strip(',')
                dictl[myline] = True

c=0
for myline in dictl.keys():          
    isfound=False
    # iterate mylist untik found
    for j in rlist.keys():
        if str(myline) == str(j): isfound=True

    if not isfound:
        print("In dict found "+myline+ " which is not in master_resources")
        c=c+1
print(str(c)+" resources not found")


print("Check all resources in master list exist in dict")

for i in rlist.keys():
    isfound=False
    for j in dictl.keys():
        if str(i) in str(j):
            isfound=True
    
    if not isfound: print("Could not find "+ str(i)+ " in dict")








            