#!/usr/bin/env python3
drl=[]
srl=[]
fr=open('../fixtf_aws_resources/needid_dict.py', 'r')
Lines = fr.readlines()
for line in Lines:
    if "aws_" in line and "{" in line:
        drl.append(line.split("=")[0].strip())
    elif "aws_" in line and ":" in line: 
        srl.append(line.split(":")[0].strip().strip('"'))


for i in drl:
    if i not in srl:
        print('"'+i+'": '+i+',')

print("\n--------------------------------------------")

for i in srl:
    if i not in drl:
        print('"'+i+'": '+i+',')