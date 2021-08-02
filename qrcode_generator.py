"""QR Code Generator by Phan Huynh Thien Phuc
This program uses the qrcode module to generate a QR code as a picture in the same folder
with this file, which can be scanned to reveal the meaning of it. Try changing "hello"
on line 7 to something else and see the result. You can surprise your friends with this!"""

import qrcode
img = qrcode.make("hello")
type(img)
img.save('hello.png')