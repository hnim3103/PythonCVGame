import cv2
import pytesseract
from PIL import ImageGrab 
import numpy as np 
import pyautogui
import time

#direct to pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'E:\Python\Tesseract\tesseract.exe'

while True: 
    #capture the screen
    #bbox = left, top, right, bottom
    img = ImageGrab.grab(bbox=(832, 640, 930, 683))
    
    #set playing-time limit
    limit = 60
    
    #reconizing text from image
    reconized_text = pytesseract.image_to_string(img)
    
    print(reconized_text)

    while(reconized_text.strip() != "START" and limit > 0):
        limit -= 1
        time.sleep(1)
        print(limit)
        img = ImageGrab.grab(bbox=(832, 640, 930, 683))
        reconized_text = pytesseract.image_to_string(img)
    if limit == 0:
        pyautogui.press('esc')
    
    
       