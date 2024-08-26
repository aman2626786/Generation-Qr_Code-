import qrcode as qr
img = qr.make("https://github.com/aman2626786")
img.save("My_Github_qrcode.png")