import cv2 as cv
import numpy as np
import os
import time

def imgToText(path ,vidFrame = False):
    if vidFrame:
        orgImg = path

    else:
        orgImg = cv.imread(path)

    density = "¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;\"^:,\'.`                                                                  "
    densityLen = len(density)
    quantUnit = 256 / densityLen

    img = cv.cvtColor(orgImg, cv.COLOR_BGR2GRAY)

    height, width = img.shape
    aspectRatio = height / width
    newShape = (64, int(64 * aspectRatio))

    img = cv.resize(img, newShape)
    
    img = np.round(img / quantUnit).astype(int)
    getCharVal = lambda x: density[x]
    getCharValVec = np.vectorize(getCharVal)
    img = getCharValVec(img)

    clr = lambda: os.system('clear')
    
    clr()
    print('\n'.join(''.join(i) for i in img), end = "\r")
    time.sleep(0.05)

    return 0 


if __name__ == "__main__":
    imgToText("image.jpeg")
