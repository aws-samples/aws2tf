#!/usr/bin/env python3
f2=open("aws_resources.py","w")

with open('aws_resources.dat', 'r') as f:
    f2.write('import boto3\n\n')
    f2.write('if type == "all":\n\n')
    for line in f.readlines():
        if '#' not in line:
            myline=line.strip('\n').strip(' ')
            f2.write('elif type == "'+myline+'":\n')

f2.close()



