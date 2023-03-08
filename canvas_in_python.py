#!/bin/python3
import requests
from config import API_KEY

header = {'Authorization' : 'Bearer {}'.format(API_KEY)}
#get all courses
url = 'https://overlake.instructure.com/api/v1/courses/'
r = requests.get(url, headers=header)
print("Current classes")
for i in r.json():
    print("{} -- id: {}".format(i["name"], i['id']))