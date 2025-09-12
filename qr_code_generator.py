import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename (with .png or .jpg): ").strip()

if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
    filename += ".png"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
image.save(filename)

print(f'QR code saved as "{filename}"')
