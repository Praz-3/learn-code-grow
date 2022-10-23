import pyqrcode
import png
from pyqrcode import QRCode
  
print("Enter the youtube link for the qr code.")
link = input()
  

url = pyqrcode.create(link)
  
url.svg("myqr.svg", scale = 8)
  
url.png('myqr.png', scale = 6)