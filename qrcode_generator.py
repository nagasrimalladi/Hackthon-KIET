import qrcode

file_name = input("Enter file name:")
website = input("Enter the data / website link for the QR:")

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


img = qrcode.make(f"{website}")
img.save(f"{file_name}.png")

qr.add_data(website)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="black")
img.save("medium.png")