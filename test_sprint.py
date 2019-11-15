#!/usr/bin/python

import sys
import traceback
import re
import base64
import logging
import datetime
import json
import urllib2

import requests
from requests.auth import HTTPBasicAuth

giturl = "https://api.github.com/repos/satish-bhonsle/Rectangle-project/contents/sprint-version.txt?ref=satish-dev"
AUTH_TOKEN = 'token a309fb650340d6b5196a02494b149e2bd851d642'
#sha = '5d0f3c164ee633022dfe32e49985467f0b783a6b'
sha = '5d0f3c164ee633022dfe32e49985467f0b783a6b'
payload = '1234'
# headers_data = {
#     'Content-Type': 'plain/text'
# }
# r = requests.get(str(giturl))
# print r.ok
# r = requests.get(str(giturl),headers={'Authorization': AUTH_TOKEN})
# print r.json()['sha']

# #r = requests.put(str(giturl), data=json.dumps(put_data), headers={'Authorization': AUTH_TOKEN, 'accept': 'application/json'})

# # r.Content-Type = 'application/json'
# # print (r.json())
# print (r.status_code)
# #print dir(r.json())
# decodedString = base64.b64decode(r.json()['content'])
# print decodedString

encodedString = base64.b64encode(payload)

put_data = { "branch": 'satish-dev', "content": encodedString, "message": "commit_message", "sha": sha, "committer": { "name": "satish-bhonsle", "email": "satish.sanju@gmail.com"}}


r = requests.put(str(giturl), data=json.dumps(put_data), headers={'Authorization': AUTH_TOKEN})
print (r.status_code)
print r.request

r = requests.get(str(giturl),headers={'Authorization': AUTH_TOKEN})
print r.json()['sha']
print (r.status_code)
#print dir(r.json())
decodedString = base64.b64decode(r.json()['content'])
print decodedString



