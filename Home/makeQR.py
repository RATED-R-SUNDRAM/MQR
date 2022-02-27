#MAKIING QR FROM A WEB URL
import qrcode

# Data to be encoded
data = 'www.facebook.com'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode2.png')