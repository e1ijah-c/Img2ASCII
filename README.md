<h3 align="center">
    Img2ASCII
</h3>

<p align="center">
  <img width="300" src="https://github.com/user-attachments/assets/d3de3b9f-1d4a-4c93-9a57-6f2ae195b4f9">
</p>

<p align="center">
  <i>
    A simple program to revisualise images as ASCII text.
  </i>
</p>

<details>

<summary>Contents</summary>

1. [About the Project](#-about-the-project)
    - [The Process & How It Works](#the-process--how-it-works) 
2. [Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Roadmap](#-roadmap)
4. [Contact](#%EF%B8%8F-contact)

</details>



## 🚀 About the Project
> _Img2ASCII is <ins>free to use</ins> and serves as a personal coding project that has intrigued me ever since watching [this](https://youtu.be/gg40RWiaHRY?si=JBFu_-3ykr3s3N7P) YouTube video on 'ASCII Rendering' by [Acerola](https://github.com/GarrettGunnell)._

Written in _**Python**_ and utilising the [**_Pillow_**](https://pillow.readthedocs.io/en/stable/) library — it generates uploaded images as if comprised of ASCII characters. The program aims to be straightforward and uncomplicated,
built for those who want to achieve the familiar 'retro' aesthetic for their art without spending hours typing out individual characters. 

### The Process & How It Works

> ###### While my insipiration for this project is certainly drawn from other's creations, I have decided to implement my own method as a _'proof-of-concept'_ and to develop my own programming knowledge and skills.

To start, I have decided make the program capable of handling any image size. To achieve this, it divides the width and height dimensions of the image by 8 (as each ASCII character occupies an 8x8 pixel area) and crops out the remainder split evenly among the left-right and top-bottom. 

The code snippet below demonstrates how this was done for the width (same process can be applied for height).  
```python
wCrop = imgRaw.size[0] % 8

if wCrop != 0:
    if wCrop % 2 != 0:
        wCropL = int((wCrop / 2) + 0.5)
        wCropR = int((wCrop / 2) - 0.5)
    else:
        wCropL = wCropR = wCrop / 2
```
Another aspect of the 'pre-processing' of the image is to enhance both the sharpness and contrast to make the output image have more defined edges and distinction between colours, resulting in better looking ASCII art. 

This is conveniently done using _Pillow's_ built in class <ins>ImageEnhance</ins>: 
```python
img = ImageEnhance.Contrast(img).enhance(3.0)
img = ImageEnhance.Sharpness(img).enhance(2.0)
```

Moving on, calculating the top-left coordinates of each '8x8 slot' it ensures each ASCII character is drawn from the frame of reference each time.
```python
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
```

The individual brightness of a single pixel is calculated by taking the average of each image band (i.e. R, G & B) and dividing by 3:

<p align="center">
    $Brightness=\frac{(R+G+B)}{3}$
</p>

However, in this case we need to do this but for our 8x8 plane — this means summing all the R, G & B values across the plane and dividing by 192 (64 pixels each with 3 values). This allows us to know which corresponding ASCII character to draw, while filtering out transparent pixels (i.e. alpha = 0) commonly found on ".png" files.
```python
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
```
The result is a decently accurate reflection of the original image, but loses visual clarity when there is not enough contrast (though this is currently being addressed). Furthermore, it assumes the input image has a transparent background (.png files) so that the ASCII characters can be displayed cleanly without the addition of background details which may clutter the final output. 


## 📘 Getting Started 
> Img2ASCII was built on Python (ver. 3.13) using Pillow (ver. 11.2.1), hence these versions are recommended to ensure the program functions as intended.

### Prerequisites
- _Python_ (ver. 3.13 or later) — see [this guide](https://wiki.python.org/moin/BeginnersGuide/Download) for installation help.
- _Pillow_ (ver. 11.2.1 or later)

### Installation
1. Install the latest verion of [_pip_](https://pip.pypa.io/en/stable/) for _Python_.
```bash
python3 -m ensurepip --upgrade
```

2. Install _Pillow_ library using pip
```bash
python3 -m pip install pillow
```

3. Clone the repo
```bash
git clone https://github.com/e1ijah-c/Img2ASCII.git
```

4. Set git remote url to avoid pushes to base project
```bash
git remote set-url origin  https://github.com/e1ijah-c/Img2ASCII.git
git remote -v
```

## 🚙 Roadmap

- [x] Make working program
- [x] Finish README file
- [x] Improve output quality by first increasing contrast of original image

## ☎️ Contact

**Email:** elijahchia255@gmail.com\
**Project Link:** https://github.com/e1ijah-c/Img2ASCII



