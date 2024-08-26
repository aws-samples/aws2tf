import sys
import os
import subprocess

def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol = len(out.stdout.decode('utf-8').rstrip())
    el = len(out.stderr.decode().rstrip())
    if el != 0:
         errm = out.stderr.decode().rstrip()
         # print(errm)
         # exit(1)

    # print(out.stdout.decode().rstrip())
    return out


def handler(event, context):
    print("Command line arguments:", str(event))
    cla=str(event['payload'])
    #os.chdir("/tmp/aws2tf") 
    com="ls -al"
    rout = rc(com)
    stc=rout.stdout.decode().rstrip() 
    print(str(stc)) 
    com="python3 ./aws2tf.py "+cla
    print("com=",com)
    rout = rc(com)
    stc=rout.stdout.decode().rstrip() 
    ste=rout.stderr.decode().rstrip()
    print("com err=",str(ste))
    print("com out=",str(stc))
    return 'aws2tt: ' + stc
# get the command line arguments 'cmla' from events

# needs to call aws2tf.py via os

