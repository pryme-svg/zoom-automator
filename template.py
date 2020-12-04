#!/usr/bin/python3

import pyautogui
import time

#CONFIGURATION
meet_id = ''
password = ''
#esc clicked to ensure that the win key will open up correctly in the next step
#pyautogui.press('esc',interval=0.1)

#for windows
#pyautogui.press('win',interval=0.1)
#pyautogui.write('zoom')
#pyautogui.press('enter',interval=0.5)


#JOIN THE MEETING

#wait for app to start
#time.sleep(10) #only for windows

r = pyautogui.locateCenterOnScreen('joinButton2.png', confidence=.8)

pyautogui.click(r)
time.sleep(5)

g = pyautogui.locateCenterOnScreen('meet_id_button.png' , confidence=.8)

pyautogui.click(g)

time.sleep(5)


pyautogui.write(meet_id)
pyautogui.press('enter')
time.sleep(5)
#for linux
# a = pyautogui.locateCenterOnScreen('leave_button.png', confidence=.8) #zoom on linux bug

# pyautogui.click(a)

time.sleep(3)

pyautogui.write(password)
pyautogui.press('enter')
