# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
data = "Santanu Banik"

# Generate QR code
url = pyqrcode.create(data)

# Create and save the png file naming "myqr.png"
url.svg("SantanuRQ.svg", scale=8)