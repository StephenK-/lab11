import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

#Spliting keys
access_key_id, secret_access_key = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key').read().split(':')



# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key = secret_access_key)

myq = conn.get_queue(sys.argv[1])

# Deleting a queue with the name of..
conn.delete_queue(myq)

print('Delete Complete')

