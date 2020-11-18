# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:12:23 2020

@author: Guillaume
"""

import pyautogui
import time
import pydirectinput
import os
os.chdir('D:\Projets\Minecraft')


#screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
#currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.#
#pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
#pyautogui.click() # Click the mouse at its current location.
#pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
#pyautogui.move(0, 100)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
##pyautogui.doubleClick() # Double click the mouse at the
#pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
#pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
#pyautogui.press('esc') # Simulate pressing the Escape key.
#pyautogui.keyDown('shift')
#pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
#pyautogui.keyUp('shift')
#pyautogui.hotkey('ctrl', 'c')
    

def my_func():
    time.sleep(5)
    print("Hey")
my_func()

def move_mouse(x,y):
    currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    pyautogui.moveTo(currentMouseX + x, currentMouseY + y, duration=0.1, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.

def move_w():
    pyautogui.keyDown('w')
    time.sleep(3)
    pyautogui.keyUp('w')
    time.sleep(3)
    pyautogui.press('w')
time.sleep(3)
move_mouse(0,20)
move_mouse(20,20)
move_mouse(20,0)

time.sleep(3)
pydirectinput.keyDown('w')
time.sleep(0.5)
pydirectinput.keyUp('w')

move_w()
print('sup1')
time_start = time.time()
im1 = pyautogui.screenshot(region=(0,40, 950,470))
time_end = time.time()
print(time_end - time_start, 'seconds elapsed')
print('sup2')


for pos in pyautogui.locateAllOnScreen('Couleurs\grass.png'):
    print(pos)
list(pyautogui.locateAllOnScreen('Couleurs\grass.png'))

time_start = time.time()
region_game = (0,40, 950,470)
test = pyautogui.locateOnScreen('Couleurs\grass.png', region= region_game)
time_end = time.time()
print(time_end - time_start, 'seconds elapsed')


