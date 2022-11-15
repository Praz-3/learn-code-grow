""" This code is to generate a QR code from a YouTube link
For this we need to import qrcode package
img is the qrcode which will be saved in program folder
"""
import qrcode

YT_link = input("Enter the link of YouTube video to generate qr code -\n")

img = qrcode.make(YT_link) 
img.save("QRCode.jpg") 

#qrcode generated and saved as img of name QRCode.jpg
