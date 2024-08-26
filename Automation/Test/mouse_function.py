# Mouse functions

import pyautogui

def show_resolution():
  print(pyautogui.size())
  
  
def show_mouse_position():
  ## Easy way
  
  pyautogui.displayMousePosition()
  
  
  # ## Alternative way
  # # Place holder for the 1st mouse position
  # org_x, org_y = -1,-1
  
  # # Track current mouse position
  # while True:
  #   current_x, current_y = pyautogui.position()
    
  #   # Only display when mouse move to a new position
  #   if current_x != org_x or current_y != org_y:
  #     print(pyautogui.position()) 
  #     org_x, org_y = current_x, current_y
  #     pyautogui.sleep(0.1)
    
  #   # Stop the program by moving to the top left corner of the screen  
  #   elif current_x == 0 and current_y == 0:
  #     print("Stopping...")
  #     pyautogui.sleep(3)
  #     break
  
  
def mouse_moveTo():
  pyautogui.moveTo(2000, 100, 0.5)
  
def mouse_oneClick():
  pyautogui.leftClick()
  
def mouse_scroll():
  while True:
    pyautogui.scroll(-50)

def mouse_drag():
  pyautogui.mouseDown(871, 797, button='left')
  pyautogui.moveTo(937, 557, duration=5)
  pyautogui.mouseUp()

if __name__ == '__main__':
  pyautogui.sleep(3)
  show_mouse_position()
  # mouse_moveTo()
  # mouse_oneClick()
  # mouse_scroll()
  # mouse_drag()
  print("Ending program...")
  pyautogui.sleep(1)