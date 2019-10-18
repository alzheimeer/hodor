#!/usr/bin/python3
"""Hodor 0"""
import requests


try:
    ID = int(input("Input number the ID: "))
except ValueError:
    print("PLEASE: input number integer.")
    exit(98)
try:
    votes = int(input("Input number the votes: "))
except ValueError:
    print("PLEASE: input number integer.")
    exit(98)
url = 'http://158.69.76.135/level0.php'
data = {'id': ID, 'holdthedoor': 'Submit'}
success = 'Hold the Door challenge - Level 0'
ok = 0
fail = 0
response = requests.get(url)
votescurrent = 0
txt = response.text.split()
txtid = txt.index(str(ID))
if ((txt[txtid+3]).isdigit()):
    votescurrent = int(txt[txtid+3])

print("------------------------------------------------------------------")
print("Hello Alzheimeer: ID: {}, VOTES CURRENT: {}, URL: {}\
".format(ID, votescurrent, url))
print("------------------------------------------------------------------")
print(success)
print("------------------------------------------------------------------")

for i in range(votescurrent, votes):
    response = requests.post(url, data)
    if response.status_code is 200 and success in response.text:
            ok += 1
            print("{} Ok".format(ok), end='\r', flush=True)
    else:
            fail += 1
            print("{} Fail".format(fail), end='\r', flush=True)

print()
print("------------------------------------------------------------------")
print("Finally Alzheimeer: Ok {}, Fail {}".format(ok, fail))
