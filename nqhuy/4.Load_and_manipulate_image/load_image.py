# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:58:35 2022

@author: ADMIN
"""

# load and show an image with Pillow
from PIL import Image
# load the image
image = Image.open("opera_house.jpg")
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()