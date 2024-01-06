#!/usr/bin/env python3

st1=False
fr=open('../resources.py', 'r')
line = fr.readline()
while line:
    line = fr.readline()
    myline=str(line).strip()
    if 'aws_' in myline and 'elif' in myline and '[' not in myline:
        st1=True
        print(myline.split('"')[1])
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
        print(clfn)

fr.close()


#def aws_eks_addon(t1,tt1,tt2,flag1,flag2):
#    skip=0
#    return skip,t1,flag1,flag2 








