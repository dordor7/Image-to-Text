import cv2 as cv
import numpy as np

def imgToText(path):
    orgImg = cv.imread(path)

    density = "¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;\"^:,\'.`                              "
    densityLen = len(density)
    quantUnit = 256 / densityLen

    img = cv.cvtColor(orgImg, cv.COLOR_BGR2GRAY)

    height, width = img.shape
    #print(f"Original image is {height}x{width}")

    img = cv.resize(img, (64, 64))
    
    img = np.round(img / quantUnit).astype(int)
    getCharVal = lambda x: density[x]
    getCharValVec = np.vectorize(getCharVal)
    img = getCharValVec(img)
       
    print('\n'.join(''.join(i) for i in img))

    return 0 


if __name__ == "__main__":
    imgToText("image.jpeg")
