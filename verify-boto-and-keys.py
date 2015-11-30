import boto
import urllib2
import string

keyandid = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

keyandid = keyandid.read()
keys = keyandid.split(':')

print ("ID: "+ keys[0])
print ("\nKey: "+keys[1])

print ("\nBoto Version: "+ boto.Version)
