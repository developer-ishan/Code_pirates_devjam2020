# Import QR Code library
import qrcode
from user.models import user_profile
# from qrtools import QR 

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

# The data that you want to store
data = "https://ourcodeworld.com/articles/read/554/how-to-create-a-qr-code-image-or-svg-in-python"

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("qr_tag/{}.jpg".format())

