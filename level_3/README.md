Level 3
Has to have a WINDOW's user agent.

Has to use pytesseract to read a CAPTCHA image off the server.

Has to parse the hidden 'key' field's 'value' from a GET request

Has to add the user's 'id' and 'holdthedoor' fields to POST request.

Votes successfully 1024 times.


What is tesseract?
Tesseract is a powerful OCR engine free to use.

While proprietary software was developed by Hewlett Packard,
after years without evolution, in 2005 it ended up being released the code originally.
It is currently developed by Google.

Install of Tesseract

sudo apt update
sudo apt install tesseract-ocr
sudo apt-get install tesseract-ocr-spa

Dependencies

sudo apt install imagemagick

Install of pytesseract

sudo pip3 install pytesseract
sudo pip3 install opencv-python