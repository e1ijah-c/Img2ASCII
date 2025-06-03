from PIL import Image, ImageOps


imgRaw = Image.open("fish.png")

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
img = img.convert("RGBA")
img_ASCII = Image.new("RGB", img.size)

print(img.getpixel((0,0)))

def CheckTransparent(x: int, y: int):
    for i in range(8):
        for n in range(8):
            alpha = img.getpixel((x+i,y-n))[3]
            if alpha > 0:
                return False
    return True

def GetBrightness(x: int, y: int):

    sum = 0    
    for w in range(8):
        for h in range(8):

            r = img.getpixel((x+w,y-h))[0]
            g = img.getpixel((x+w,y-h))[1]
            b = img.getpixel((x+w,y-h))[2]
            sum += (r+g+b)

    return int(sum / 192)

def DrawDot(x: int, y: int):
    img_ASCII.putpixel((x+3,y-6), (255, 255, 255))
    img_ASCII.putpixel((x+4,y-6), (255, 255, 255))
    img_ASCII.putpixel((x+3,y-5), (255, 255, 255))
    img_ASCII.putpixel((x+4,y-5), (255, 255, 255))

def DrawPlus(x: int, y: int):
    for i in range(6):
        img_ASCII.putpixel((x+1+i,y-3), (255, 255, 255))

    for i in range(5):    
        img_ASCII.putpixel((x+3,y-1-i), (255, 255, 255))
        img_ASCII.putpixel((x+4,y-1-i), (255, 255, 255))

def DrawHash(x: int, y: int):
    for i in range(8):
        img_ASCII.putpixel((x+i,y-2), (255, 255, 255))
        img_ASCII.putpixel((x+i,y-5), (255, 255, 255))
    
    for i in range(6):
        img_ASCII.putpixel((x+1,y-1-i), (255, 255, 255))
        img_ASCII.putpixel((x+2,y-1-i), (255, 255, 255))
        img_ASCII.putpixel((x+5,y-1-i), (255, 255, 255))
        img_ASCII.putpixel((x+6,y-1-i), (255, 255, 255))

def DrawAsterisk(x: int, y: int):
    for i in range(8):
        img_ASCII.putpixel((x+i,y-3), (255, 255, 255))
    
    for i in range(4):
        img_ASCII.putpixel((x+2+i,y-2), (255, 255, 255))
        img_ASCII.putpixel((x+2+i,y-4), (255, 255, 255))
    
    img_ASCII.putpixel((x+1,y-1), (255, 255, 255))
    img_ASCII.putpixel((x+2,y-1), (255, 255, 255))
    img_ASCII.putpixel((x+5,y-1), (255, 255, 255))
    img_ASCII.putpixel((x+6,y-1), (255, 255, 255))

    img_ASCII.putpixel((x+1,y-5), (255, 255, 255))
    img_ASCII.putpixel((x+2,y-5), (255, 255, 255))
    img_ASCII.putpixel((x+5,y-5), (255, 255, 255))
    img_ASCII.putpixel((x+6,y-5), (255, 255, 255))

def DrawSquare(x: int, y: int):
    for i in range(8):
        for n in range(8):
            img_ASCII.putpixel((x+n,y-i), (255, 255, 255))



wFactor = int(img.size[0] / 8)
hFactor = int(img.size[1] / 8)
xVals = []
yVals = []

for i in range(wFactor):
    x = i * 8
    xVals.append(x)

for i in range(hFactor):
    y = i * 8
    yVals.append(y)

print(xVals)
print(yVals)


for w in range(len(xVals)):
    for h in range(len(yVals)):
        brightness = GetBrightness(xVals[w], yVals[h])

        if 0 <= brightness <= 50 and CheckTransparent(xVals[w], yVals[h]) == False:
            exit
        elif 51 <= brightness <= 101 and CheckTransparent(xVals[w], yVals[h]) == False:
            DrawPlus(xVals[w], yVals[h])
        elif 102 <= brightness <= 152 and CheckTransparent(xVals[w], yVals[h]) == False:
            DrawHash(xVals[w], yVals[h])
        elif 153 <= brightness <= 203 and CheckTransparent(xVals[w], yVals[h]) == False:
            DrawAsterisk(xVals[w], yVals[h])
        elif 204 <= brightness <= 255 and CheckTransparent(xVals[w], yVals[h]) == False:
            DrawSquare(xVals[w], yVals[h])



img_ASCII.show()

#print(topLeft)


#width = img.size[0]
#length = img.size[1]
#debugList = []

# for w in range(width):
#     for h in range(length):
#         brightness = GetBrightness(w,h)
#         img.putpixel((w,h), (brightness, brightness, brightness))
#         debugList.append(brightness)

#img.show()


