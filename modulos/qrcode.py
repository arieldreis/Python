import qrcode
data = "https://www.canva.com/design/DAGm-YU-RCw/M9_LWg-tb_wPhjsWunxxVA/edit?utm_content=DAGm-YU-RCw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
qr = qrcode.make(data)
qr.save("myqrcode.png")