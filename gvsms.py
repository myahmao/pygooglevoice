#!/usr/local/bin/python
# coding: utf-8


'''
To install
$ yum install python python-setuptools
$ sudo easy_install simplejson
$ sudo easy_install -U pygooglevoice'''

from googlevoice import Voice
from googlevoice.util import input

voice = Voice()
voice.login()

#import platform
#print platform.python_version()

#phoneNumber = input('Number to send message to: ')
#text = input('Message text: ')

phoneNumbers = [1234567890,9012345678]
text = '哥哥在这里！'

i=1
for phoneNumber in phoneNumbers:
	print i, phoneNumber
	i+=1
	voice.send_sms(phoneNumber, text)
