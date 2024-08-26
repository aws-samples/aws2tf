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
    com="ls -al /tmp"
    rout = rc(com)
    stc=rout.stdout.decode().rstrip() 
    print(str(stc)) 
    return 'Hello from AWS Lambda using Python ' + str(event['payload'])
# get the command line arguments 'cmla' from events

# needs to call aws2tf.py via os

