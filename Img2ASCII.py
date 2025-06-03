from PIL import Image, ImageOps
import numpy as np

size = (1024, 1024)

#img = ImageOps.fit(Image.open("jake.png"), size)
#img_resize = img.resize(size)

imgRaw = Image.open("jake.png")

wCrop = imgRaw.size[0] % 8
hCrop = imgRaw.size[1] % 8

if wCrop != 0:
    if wCrop % 2 != 0:
        wCropL = int((wCrop / 2) + 0.5)
        wCropR = int((wCrop / 2) - 0.5)
    else:
        wCropL = wCropR = wCrop / 2
else:
    wCropL = wCropR = 0

if hCrop != 0:
    if hCrop % 2 != 0:
        hCropT = int((hCrop / 2) + 0.5)
        hCropB = int((hCrop / 2) - 0.5)
    else:
        hCropT = hCropB = wCrop / 2
else:
    hCropT = hCropB = 0

img = imgRaw.crop((wCropL, hCropT, imgRaw.size[0] - wCropR, imgRaw.size[1] - hCropB))
print(img.size)

def GetBrightness(x, y):

    r = int(img.getpixel((x,y))[0])
    g = int(img.getpixel((x,y))[1])
    b = int(img.getpixel((x,y))[2])

    return int((r + g + b) / 3)


width = img.size[0]
length = img.size[1]
debugList = []

for w in range(width):
    for h in range(length):
        brightness = GetBrightness(w,h)
        img.putpixel((w,h), (brightness, brightness, brightness))
        debugList.append(brightness)

img.show()


