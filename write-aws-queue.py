import requests
import string
import urllib2
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
 
 
#
#Spliting keys
access_key_id, secret_access_key = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key').read().split(':')
 
 
 
# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key = secret_access_key)
 
q = conn.get_queue(sys.argv[1])
 
# Setting Message
message = Message()
message.set_body(str(sys.argv[2]))
q.write(message)
print('Write Message Complete')
