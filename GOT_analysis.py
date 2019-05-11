#note: this is reading the mp4 video and only taking one capture per second of video 
videoFile = "video.mp4"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = str(int(x)) + ".jpg";x+=1
        cv2.imwrite(filename, frame)

cap.release()
print ("Done!")

import os
from PIL import Image
import time
import random
import math
import os

method = "rgb_average"

def genAvgRGB(img):

    #converting image to rgb
    img = img.convert("RGB")
    colors = img.getcolors(img.size[0] * img.size[1])
    #average
    avg = tuple([sum([y[1][x] * y[0] for y in colors]) / sum([z[0] for z in colors]) for x in range(3)])
    return avg

#getting images
images = ["screenshot_images/"+x for x in os.listdir("screenshot_images/")]
images.sort(key=lambda x: int(x[7:-4]))

barColors = []

#getting the color for each jpg
for img in images:
    img = Image.open(img).resize((25,25))

    #applying correct method
    if method.lower() == "rgb_average":
        color = genAvgRGB(img)
    barColors.append(color)
    
#Plotting the color values
import numpy as np
from PIL import Image

barColors = (np.array(barColors)).astype(np.uint8)

title = "GameOfTones"
cols = len(barColors)
rows = max([1,int(cols/2.5)])

#Color Array
barFullData = np.tile(barColors, (rows,1)).reshape(rows, cols, 3)
#Create Image from Array
barImg = Image.fromarray(barFullData, 'RGB')

barImg = barImg.resize((2000,1000), resample=0)
barImg
barImg.save("Season8Ep3.png".format(title,method))
