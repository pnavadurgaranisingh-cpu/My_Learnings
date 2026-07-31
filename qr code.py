import qrcode

data = "www.linkedin.com/in/navadurga-rani-singh-p-435603384"

qr = qrcode.make(data)

qr.save("C:/my def/python/qrcode.png")
