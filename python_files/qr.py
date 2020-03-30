#!/usr/bin/env python3

"""Make QR code."""

import qrcode

url = # whatever url
image = qrcode.make(url)
image.save("qr.png", "PNG")

