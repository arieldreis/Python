import qrcode as qr

url = "https://www.instagram.com/arieldreis/"
myqr = qr.make(url)
myqr.save("myqrcode.png")