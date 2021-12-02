from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (390,280)
    dinosaur = (155,285)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')

def imageGrab():
    box = (190,280,244, 310)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def playGame():
    restartGame()
    while True:
        # print(imageGrab())
        if imageGrab() != 1867:
            pressSpace()
            print('Jump...Jump...')
            # time.sleep(0.1)
        print('Run... ')

playGame()