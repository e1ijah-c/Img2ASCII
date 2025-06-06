from PIL import Image, ImageOps, ImageEnhance
import numpy as np
import Img2ASCII as asc


img = asc.img

asc.img_ASCII.show()
sobel_img = sobel_img = Image.new("L", ([img.size[0], img.size[1]]), 0)
sobel_img_ASCII = asc.img_ASCII

def xDirKernel(top_left: int, top_center:int, top_right: int, 
               left: int, center: int, right: int, 
               bottom_left: int, bottom_center: int, bottom_right: int):
    
    outputs = []
    outputs.extend((top_left * -1, top_center * 0, top_right, 
                    left * -2, center * 0, right * 2,
                    bottom_left * -1, bottom_center * 0, bottom_right))
    
    return outputs

def yDirKernel(top_left: int, top_center:int, top_right: int, 
               left: int, center: int, right: int, 
               bottom_left: int, bottom_center: int, bottom_right: int):
    
    outputs = []
    outputs.extend((top_left * -1, top_center * -2, top_right * -1, 
                    left * 0, center * 0, right * 0,
                    bottom_left, bottom_center * 2, bottom_right))
    
    return outputs

def SumKernel(kernelOutputs: list):
    return int(np.sum(kernelOutputs))

def GetGradientMag(gX: int, gY: int):
    gXsqr = gX * gX
    gYsqr = gY * gY
    sqrSum = gXsqr + gYsqr
    gMag = np.sqrt(sqrSum)
    
    return gMag

def DrawSlash(x: int, y: int):
    for i in range(2):
        sobel_img_ASCII.putpixel((x+1,y+6-i), (255))
        sobel_img_ASCII.putpixel((x+2,y+5-i), (255))
        sobel_img_ASCII.putpixel((x+3,y+4-i), (255))
        sobel_img_ASCII.putpixel((x+4,y+3-i), (255))
        sobel_img_ASCII.putpixel((x+5,y+2-i), (255))

        sobel_img.putpixel((x+2,y+5-i), (255))
        sobel_img.putpixel((x+1,y+6-i), (255))
        sobel_img.putpixel((x+3,y+4-i), (255))
        sobel_img.putpixel((x+4,y+3-i), (255))
        sobel_img.putpixel((x+5,y+2-i), (255))
    
    sobel_img_ASCII.putpixel((x+6,y+1), (255))
    sobel_img.putpixel((x+6,y+1), (255))

def DrawBackSlash(x: int, y: int):
    for i in range(2):
        sobel_img_ASCII.putpixel((x+1,y+1+i), (255))
        sobel_img_ASCII.putpixel((x+2,y+2+i), (255))
        sobel_img_ASCII.putpixel((x+3,y+3+i), (255))
        sobel_img_ASCII.putpixel((x+4,y+4+i), (255))
        sobel_img_ASCII.putpixel((x+5,y+5+i), (255))

        sobel_img.putpixel((x+1,y+1+i), (255))
        sobel_img.putpixel((x+2,y+2+i), (255))
        sobel_img.putpixel((x+3,y+3+i), (255))
        sobel_img.putpixel((x+4,y+4+i), (255))
        sobel_img.putpixel((x+5,y+5+i), (255))
        
    sobel_img_ASCII.putpixel((x+6,y+6), (255))
    sobel_img.putpixel((x+6,y+6), (255))

def DrawUnderScore(x: int, y: int):
    for i in range(8):
        sobel_img_ASCII.putpixel((x+i,y+7), (255))
        sobel_img.putpixel((x+i,y+7), (255))

def DrawVerticalBar(x: int, y: int):
    for i in range(8):
        sobel_img_ASCII.putpixel((x+3,y+i), (255))
        sobel_img_ASCII.putpixel((x+4,y+i), (255))
        
        sobel_img.putpixel((x+3,y+i), (255))
        sobel_img.putpixel((x+4,y+i), (255))

def ClearSlot(x: int, y:int):
    for i in range(8):
        for n in range(8):
            asc.img_ASCII.putpixel((x+1+n,y+1+i), (0))

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

# get the character slots that are valid anchor positions
anchor_positions = []

for w in range(1, len(xVals)-1):
    for h in range(1, len(yVals)-1):
        anchor_positions.append((xVals[w], yVals[h]))


# create list for ASCII script to reference later
gradientList = []

# create list to store all outline pixels for later
outlinePositions = []

for i in range(len(anchor_positions)-1):
    x = anchor_positions[i][0]
    y = anchor_positions[i][1]

    # get the pixel intensity for each ascii slot in a 3x3 grid, with the anchor slot in the center
    top_left = asc.GetBrightness(x-8, y-8)
    top_center = asc.GetBrightness(x, y-8)
    top_right = asc.GetBrightness(x+8, y-8)
    left = asc.GetBrightness(x-8, y)
    center = asc.GetBrightness(x, y)
    right = asc.GetBrightness(x+8, y)
    bottom_left = asc.GetBrightness(x-8, y+8)
    bottom_center = asc.GetBrightness(x, y+8)
    bottom_right = asc.GetBrightness(x+8, y+8)

    # convolve the values with the x and y kernel matrices
    xKernelOutputs = xDirKernel(top_left, top_center, top_right,
                                left, center, right,
                                bottom_left, bottom_center, bottom_right)

    yKernelOutputs = yDirKernel(top_left, top_center, top_right,
                                left, center, right,
                                bottom_left, bottom_center, bottom_right)

    # sum the convolved values
    gradientX = SumKernel(xKernelOutputs)
    gradientY = SumKernel(yKernelOutputs)

    # calculate the magnitude of the gradient
    gradientMag = GetGradientMag(gradientX, gradientY)

    # if magnitude is above threshold, means there is a sharp change in pixel intensity... 
    # means likely to be an outline therefore place a pixel at the anchor position
    if gradientMag > 400:
        
        angle = float(np.atan2(gradientX, gradientY))
        angle = float(np.round(angle, 2))
        pi = float(np.round(np.pi, 2))
        ClearSlot(x, y)

        if -0.2 <= angle <= 0.2 or -pi+0.2 <= angle <= -pi or pi-0.2 <= angle <= pi:
            DrawUnderScore(x, y)
        elif 0.2 < angle < (pi/2)-0.2 or -pi+0.2 < angle < -(pi/2)-0.2:
            DrawSlash(x, y)
        elif -(pi/2)+0.2 < angle < -0.2  or (pi/2)+0.2 < angle < pi-0.2:
            DrawBackSlash(x, y)
        elif pi/2-0.2 < angle < pi/2+0.2 or  -(pi/2)-0.2< angle < -(pi/2)+0.2:
            DrawVerticalBar(x, y)

asc.img.show()
sobel_img.show()
sobel_img_ASCII.show()