# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:47:33 2020

@author: Guillaume
"""

import pyautogui
import time
import pydirectinput
import cv2
import os
os.chdir('D:\Projets\Minecraft AI')

def move_cursor(x,y):
    timing = (x ** 2 + y ** 2 ) ** 0.5 * 0.015
    pyautogui.move(x, y, duration=timing)

def move_keyboard(letters,timing = 0.1):
    #pydirectinput.press(letter)
    for letter in letters:
        pydirectinput.keyDown(letter)
    time.sleep(timing)
    for letter in letters:
        pydirectinput.keyUp(letter)

time.sleep(3)    
move_cursor(50,0)

#pyautogui.PAUSE = 0
time.sleep(3)
move_keyboard(['w','d'],1)
#pyautogui.PAUSE = 0.1

time.sleep(3)
pyautogui.size()

time_start = time.time()
region_game = (0,40, 950,470)
#test = pyautogui.locateOnScreen('Block Identifier\Grass.png', region= region_game)
#test = pyautogui.locateOnScreen('Block Identifier\Grass.png', region= region_game)
test = pyautogui.screenshot(region= region_game)
test.save('screenshot_temp.png')
method = cv2.TM_SQDIFF_NORMED
oak_target = cv2.imread('Block Identifier\Grass.png')
screenshot_temp = cv2.imread('screenshot_temp.png')
result_search = cv2.matchTemplate(oak_target,screenshot_temp,method)
result_search
time_end = time.time()
print(time_end - time_start, 'seconds elapsed')
list(test)

print(pyautogui.PAUSE)

mn,_,mnLoc,_ = cv2.minMaxLoc(result_search)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = oak_target.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(screenshot_temp, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',screenshot_temp)

# The image is only displayed if we call this
cv2.waitKey(0)


