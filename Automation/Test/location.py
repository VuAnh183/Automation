import pyautogui

# Locate center of the image
img_position = pyautogui.locateCenterOnScreen('Data\\Edit.png', confidence=0.9)

if __name__ == '__main__':
  # Print the coordinates of the image's center
  print(img_position)

  # Move the mouse to the center of the image
  pyautogui.moveTo(img_position)