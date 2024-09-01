import sys
import os
import subprocess
import aws2tf


def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)

    # print(out.stdout.decode().rstrip())
    return out


def handler(event, context):
    #print("Command line arguments:", str(event))
    cla=str(event['payload'])
    if "-la" not in cla: cla=cla+" -la"
    os.chdir("/tmp/aws2tf") 
    com="python3 aws2tf.py "+cla
    print("com=",com)
    rout = rc(com)
    stc=rout.stdout.decode().rstrip() 
    ste=rout.stderr.decode().rstrip()

    print("STD OUT aws2tf.py ..........")
    print("aws2tf com out=",str(stc))
    print("STD ERROR aws2tf.py .........")
    print("aws2tf com err=",str(ste))
    return 'aws2tf: ' + stc
# get the command line arguments 'cmla' from events

# needs to call aws2tf.py via os

