import qrcode

# Data to encode
data = "Lund Lelo 🖕"

# Generate and save the QR code
img = qrcode.make(data)

img.save("Happy.png")

print("QR Code generated successfully!")