# Keyboard funtions

import pyautogui

def hang_time(time):
  pyautogui.sleep(time)
  
# Write on mouse position  
def keyboard_write(content):
  pyautogui.write(content)

# Press a single key  
def keyboard_press(content):
  pyautogui.press(content)
  

# Combination of keys  
def keyboard_hotkey():
  
  pyautogui.hotkey("ctrl", "2")
  
  
if __name__ == "__main__":
  hang_time(3)
  keyboard_write("123")
  

