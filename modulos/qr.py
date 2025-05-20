import qrcode as qr

url = "https://arieldreis.github.io/HTML-CSS3/Desafios_Propostos/verderEconomY/economiaVerde.html"
myqr = qr.make(url)
myqr.save("myqrcode.png")