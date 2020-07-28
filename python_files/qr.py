#!/usr/bin/env python3

"""Make QR code."""

import qrcode

url = "https://www.mikewaterman.com/"
image = qrcode.make(url)
image.save("qr.png", "PNG")
