import Pyqrcode

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=1)

qr.add_data("gianc.net")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")
