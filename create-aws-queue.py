import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

key_id, secret_access_key = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read().split(':')
conn = boto.sqs.connect_to_region("eu-west-1",aws_access_key_id=key_id, aws_secret_access_key=secret_access_key)
q = conn.create_queue(sys.argv[1])
