#!/usr/bin/env python3
import pyqrcode as qr_code
from time import sleep

# input string which represents the QR Code
link = input("Please enter the link which represents the QR Code: ")
print("Qr Code is generating...")
sleep(2)
# generate qr_code
url = qr_code.create(link)

# save svg and png files
name = input("Enter a name for QR Code: ")
print("Saving...")
sleep(3)
url.svg(f"{name}.svg", scale = 6)

url.png(f"{name}.png", scale = 6)