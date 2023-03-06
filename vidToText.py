import cv2 as cv
import numpy as np
from imgToText import imgToText

def vidToText(path):
    vid = cv.VideoCapture(path)

    count = 0

    while (True):
        count += 1
        success, frame = vid.read()

        if success == True:
            imgToText(frame, vidFrame = True)

        else:
            break 

    vid.release()

if __name__ == "__main__":
    vidToText("video.mp4")