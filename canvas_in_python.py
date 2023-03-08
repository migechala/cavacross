#!/bin/python3
import requests
from config import API_KEY

header = {'Authorization' : 'Bearer {}'.format(API_KEY)}

#simple course
url = 'https://overlake.instructure.com/api/v1/courses/9682'
r = requests.get(url, headers=header)

print(r.status_code)
print(r.json()["name"])

#simple assignments
    
url = 'https://overlake.instructure.com/api/v1/courses/9682/assignments'
r = requests.get(url, headers=header)

print(r.status_code)
print(r.json()[0]['description'])
