import qrcode

myqr = qrcode.make("https://www.youtube.com/watch?v=IUQVO97zcE0")
myqr.save("MyQr.png", sacle = 7)
