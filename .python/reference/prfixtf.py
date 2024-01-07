#!/usr/bin/env python3

st1=False
fr=open('../resources.py', 'r')
line = fr.readline()
while line:
    line = fr.readline()
    myline=str(line).strip()
    if "START AUTOGEN" in myline: st1=True
    if st1:
        if '#' in myline: continue
        if 'aws_' in myline and 'elif' in myline and '[' not in myline:
            awsr=myline.split('"')[1]
            line = fr.readline()
            myline2=str(line).strip()
            clfn=myline2.split(';')[0]
            try:
                clfn=clfn.split('"')[1]
            except:
                print("indexerror on clfn="+clfn)
                print(myline)
                print(myline2)
                exit()
            print(awsr+":"+clfn)
            of=open('fixtf_'+clfn+'.py', 'a')
            of.write('def '+awsr+'(t1,tt1,tt2,flag1,flag2):\n')
            of.write('\tskip=0\n')
            of.write('\treturn skip,t1,flag1,flag2\n\n')
fr.close()










