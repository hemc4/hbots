import pyautogui
import time
import sys


for i in range(int(sys.argv[1])):
  print i
  time.sleep(0.2)
  pyautogui.click(pyautogui.position())
