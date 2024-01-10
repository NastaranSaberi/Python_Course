import qrcode

name = input("Please enter your name:")
phone = input("Please enter your phone number:")

img = qrcode.make(name+phone)
img.save("QrCode.png")
