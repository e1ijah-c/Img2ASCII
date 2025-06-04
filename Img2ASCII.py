from PIL import Image, ImageOps

# get reference to desired image
imgRaw = Image.open("testimages/donut.png")
 
# the following section crops the image to the nearest multiple of 8 so that the ASCII characteres will fit perfectly when converted
# get width and height of image and check if it is perfectly divisible by 8
wCrop = imgRaw.size[0] % 8
hCrop = imgRaw.size[1] % 8

# if not perfectly divisible by 8, split pixels to be cropped between the left and right so that it is more even. 
if wCrop != 0:
    if wCrop % 2 != 0:
        wCropL = int((wCrop / 2) + 0.5)
        wCropR = int((wCrop / 2) - 0.5)
    else:
        wCropL = wCropR = wCrop / 2
else:
    wCropL = wCropR = 0

# same function but for the height
if hCrop != 0:
    if hCrop % 2 != 0:
        hCropT = int((hCrop / 2) + 0.5)
        hCropB = int((hCrop / 2) - 0.5)
    else:
        hCropT = hCropB = wCrop / 2
else:
    hCropT = hCropB = 0

# crop the image, and convert its type to RGBA if not already
img = imgRaw.crop((wCropL, hCropT, imgRaw.size[0] - wCropR, imgRaw.size[1] - hCropB))
img = img.convert("RGBA")

# create new blank image of the exact same image
img_ASCII = Image.new("RGB", img.size)

# Checks if entire ASCII character slot (8x8 square of pixels) is transparent
def CheckTransparent(x: int, y: int):
    for i in range(8):
        for n in range(8):
            alpha = img.getpixel((x+i,y+n))[3]
            if alpha > 0:
                return False
    return True

# calculate brightness for each ASCII character slot (8x8 square of pixels)
def GetBrightness(x: int, y: int):
    sum = 0    
    for w in range(8):
        for h in range(8):

            r = img.getpixel((x+w,y+h))[0]
            g = img.getpixel((x+w,y+h))[1]
            b = img.getpixel((x+w,y+h))[2]
            sum += (r+g+b)

    return int(sum / 192)

def DrawDot(x: int, y: int):
    img_ASCII.putpixel((x+3,y+6), (255, 255, 255))
    img_ASCII.putpixel((x+4,y+6), (255, 255, 255))
    img_ASCII.putpixel((x+3,y+5), (255, 255, 255))
    img_ASCII.putpixel((x+4,y+5), (255, 255, 255))

def DrawPlus(x: int, y: int):
    for i in range(6):
        img_ASCII.putpixel((x+1+i,y+3), (255, 255, 255))

    for i in range(5):    
        img_ASCII.putpixel((x+3,y+1+i), (255, 255, 255))
        img_ASCII.putpixel((x+4,y+1+i), (255, 255, 255))

def DrawHash(x: int, y: int):
    for i in range(8):
        img_ASCII.putpixel((x+i,y+2), (255, 255, 255))
        img_ASCII.putpixel((x+i,y+5), (255, 255, 255))
    
    for i in range(6):
        img_ASCII.putpixel((x+1,y+1+i), (255, 255, 255))
        img_ASCII.putpixel((x+2,y+1+i), (255, 255, 255))
        img_ASCII.putpixel((x+5,y+1+i), (255, 255, 255))
        img_ASCII.putpixel((x+6,y+1+i), (255, 255, 255))

def DrawO(x: int, y: int):
    for i in range(4):
        img_ASCII.putpixel((x+2+i,y+2), (255, 255, 255))
        img_ASCII.putpixel((x+2+i,y+6), (255, 255, 255))

    for i in range(2):
        img_ASCII.putpixel((x+1+i,y+3), (255, 255, 255))
        img_ASCII.putpixel((x+5+i,y+3), (255, 255, 255))
        img_ASCII.putpixel((x+1+i,y+4), (255, 255, 255))
        img_ASCII.putpixel((x+5+i,y+4), (255, 255, 255))
        img_ASCII.putpixel((x+1+i,y+5), (255, 255, 255))
        img_ASCII.putpixel((x+5+i,y+5), (255, 255, 255))

def DrawAsterisk(x: int, y: int):
    for i in range(8):
        img_ASCII.putpixel((x+i,y+3), (255, 255, 255))
    
    for i in range(4):
        img_ASCII.putpixel((x+2+i,y+2), (255, 255, 255))
        img_ASCII.putpixel((x+2+i,y+4), (255, 255, 255))
    
    img_ASCII.putpixel((x+1,y+1), (255, 255, 255))
    img_ASCII.putpixel((x+2,y+1), (255, 255, 255))
    img_ASCII.putpixel((x+5,y+1), (255, 255, 255))
    img_ASCII.putpixel((x+6,y+1), (255, 255, 255))

    img_ASCII.putpixel((x+1,y+5), (255, 255, 255))
    img_ASCII.putpixel((x+2,y+5), (255, 255, 255))
    img_ASCII.putpixel((x+5,y+5), (255, 255, 255))
    img_ASCII.putpixel((x+6,y+5), (255, 255, 255))

def DrawAnd(x: int, y: int):
    for i in range(4):
        img_ASCII.putpixel((x+4+i,y+4), (255, 255, 255))
    
    for i in range(3):
        img_ASCII.putpixel((x+3+i,y), (255, 255, 255))
        img_ASCII.putpixel((x+3+i,y+2), (255, 255, 255))
        img_ASCII.putpixel((x+2+i,y+3), (255, 255, 255))
        img_ASCII.putpixel((x+2+i,y+6), (255, 255, 255))
    
    for i in range(2):
        img_ASCII.putpixel((x+2+i,y+1), (255, 255, 255))
        img_ASCII.putpixel((x+5+i,y+1), (255, 255, 255))
        img_ASCII.putpixel((x+1+i,y+4), (255, 255, 255))
        img_ASCII.putpixel((x+1+i,y+5), (255, 255, 255))
        img_ASCII.putpixel((x+5+i,y+5), (255, 255, 255))
        img_ASCII.putpixel((x+6+i,y+6), (255, 255, 255))
    
def DrawSquare(x: int, y: int):
    for i in range(8):
        for n in range(8):
            img_ASCII.putpixel((x+n,y+i), (255, 255, 255))

# get number and location (top left coordinates) of ASCII character slots
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


for w in range(len(xVals)):
    for h in range(len(yVals)):
        # if 8x8 slot is transparent then leave it blank
        if CheckTransparent(xVals[w], yVals[h]) == True:
            exit
        
        # calculate brightness of 8x8 slot
        brightness = GetBrightness(xVals[w], yVals[h])

        # draw ASCII characters depending on brightness levels
        if 0 <= brightness <= 5:
            exit
        elif 6 <= brightness <= 29:
            DrawDot(xVals[w], yVals[h])
        elif 30 <= brightness <= 99:
            DrawPlus(xVals[w], yVals[h])
        elif 100 <= brightness <= 159:
            DrawO(xVals[w], yVals[h])
        elif 160 <= brightness <= 219:
            DrawAsterisk(xVals[w], yVals[h])
        elif 220 <= brightness <= 255:
            DrawHash(xVals[w], yVals[h])

# display finished ASCII image
img_ASCII.show()


#img_ASCII.save("ascii_apple.png")



