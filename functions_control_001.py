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
import copy
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

threshold = 0.05
loc_correction = 3
w = 6
h = 6
center_x = 475 - loc_correction
center_y = 235 - loc_correction


def get_coord_closer(target_img,screen_img,threshold):
    result_search = cv2.matchTemplate(target_img,screen_img,method)
    loc = np.where(result_search <= threshold)
    print(threshold)
    print(np.min(result_search))
    if np.min(result_search) < threshold:
        index_closer = np.argmin(((loc[0] - center_y) ** 2 + (loc[1] - center_x) ** 2) ** 0.5)
        delta_x = loc[1][index_closer] - center_x
        delta_y = -(loc[0][index_closer] - center_y)
        res = [1,delta_x,delta_y]
    else:
        res = [0,0,0]
    return res

time.sleep(3)    
move_cursor(50,0)

#pyautogui.PAUSE = 0
time.sleep(3)
move_keyboard(['w','d'],1)
#pyautogui.PAUSE = 0.1

time.sleep(3)
pyautogui.size()

pyautogui.PAUSE = 0
time_start = time.time()
region_game = (0,40, 950,470)

screenshot_temp_taken = pyautogui.screenshot(region= region_game)
screenshot_temp_taken.save('temp_files\screenshot_temp.png')
method = cv2.TM_SQDIFF_NORMED
target_temp_001 = cv2.imread('Block Identifier\Spruce.png')
target_temp_002 = cv2.imread('Block Identifier\Oak.png')
target_temp_003 = cv2.imread('Block Identifier\Grass.png')
screenshot_temp = cv2.imread('temp_files\screenshot_temp.png')
screenshot_temp_001 = copy.deepcopy(screenshot_temp)
screenshot_temp_002 = copy.deepcopy(screenshot_temp)
screenshot_temp_003 = copy.deepcopy(screenshot_temp)
#result_search_temp = cv2.matchTemplate(target_temp_001,screenshot_temp,method)
res_001 = get_coord_closer(target_temp_001, screenshot_temp_001, 0.05)
#result_search_temp = cv2.matchTemplate(target_temp_002,screenshot_temp,method)
res_002 = get_coord_closer(target_temp_002, screenshot_temp_002, 0.03)
#result_search_temp = cv2.matchTemplate(target_temp_003,screenshot_temp,method)
res_003 = get_coord_closer(target_temp_003, screenshot_temp_003, 0.005)
time_end = time.time()
print(time_end - time_start, 'seconds elapsed')
pyautogui.PAUSE = 0.1
print(pyautogui.PAUSE)
