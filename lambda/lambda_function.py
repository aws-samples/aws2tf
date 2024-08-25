import sys
def handler(event, context):
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
# get the command line arguments 'cmla' from events

# needs to call aws2tf.py via os

