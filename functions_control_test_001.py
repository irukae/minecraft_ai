# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:47:33 2020

@author: Guillaume
"""

import pyautogui
import time
import numpy as np
from matplotlib import pyplot as plt
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
oak_target = cv2.imread('Block Identifier\Spruce.png')
screenshot_temp = cv2.imread('screenshot_temp.png')
result_search = cv2.matchTemplate(oak_target,screenshot_temp,method)
result_search
time_end = time.time()
print(time_end - time_start, 'seconds elapsed')

print(pyautogui.PAUSE)


len(result_search)
len(result_search[0])
result_search[result_search<0.01]

mn,_,mnLoc,_ = cv2.minMaxLoc(result_search)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = oak_target.shape[:2]

threshold = 0.05
loc_correction = 3
w = 6
h = 6
center_x = 475 - loc_correction
center_y = 235 - loc_correction

target_img = oak_target
screen_img = screenshot_temp

def get_coord_closer(target_img,screen_img,threshold):
    result_search = cv2.matchTemplate(target_img,screen_img,method)
    loc = np.where(result_search <= threshold)
    if np.min(result_search) < threshold:
        index_closer = np.argmin(((loc[0] - center_y) ** 2 + (loc[1] - center_x) ** 2) ** 0.5)
        delta_x = loc[1][index_closer] - center_x
        delta_y = loc[0][index_closer] - center_y
        return [1,delta_x,delta_y]
    else:
        return [0,0,0]

screenshot_temp = cv2.imread('screenshot_temp.png')
get_coord_closer(oak_target,screenshot_temp,0.06)

threshold = 0.005
screenshot_temp = cv2.imread('temp_files\screenshot_temp.png')
target_temp_001 = cv2.imread('Block Identifier\Spruce.png')
target_temp_002 = cv2.imread('Block Identifier\Oak.png')
target_temp_003 = cv2.imread('Block Identifier\Grass.png')
result_search = cv2.matchTemplate(target_temp_003,screenshot_temp,method)
loc = np.where(result_search <= threshold)
print(np.min(result_search))
if np.min(result_search) < threshold:
    index_closer = np.argmin(((loc[0] - center_y) ** 2 + (loc[1] - center_x) ** 2) ** 0.5)
    delta_x = loc[1][index_closer] - center_x
    delta_y = loc[0][index_closer] - center_y
    test = [1,delta_x,-delta_y]
else:
    test = [0,0,0]
test

i = 0
for pt in zip(*loc[::-1]):
    cv2.rectangle(screenshot_temp, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #if i == 16067:
    #    cv2.rectangle(screenshot_temp, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    i += 1
    
# Display the original image with the rectangle around the match.
cv2.imshow('output',screenshot_temp)
# The image is only displayed if we call this
cv2.waitKey(0)


img_rgb = cv2.imread('Spruce.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('screenshot_temp.png')
w, h = template.shape[::-1]
w = 950
h = 470
res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
res = result_search
threshold = 0.1
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)



cv2.imwrite('res.png',img_rgb)
cv2.imwrite()



