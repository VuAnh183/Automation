import pyautogui
from AppOpener import open

## Subscribe a youtube channel
'''
1. Open a new tab on the browser
2. Search Youtube.com
3. Search for a channel
4. Click on subscribe button
'''
# hang time
def hang_time(time):
  pyautogui.sleep(time)
  
# Pop up to take input
def pop_up():
  channel_name = pyautogui.prompt(text='', title='Enter channel name')
  
  return channel_name
  

# open a browser window
def open_browser():
  browser = pyautogui.prompt(text='', title='Enter browser name')
  open(browser, match_closest=True)
  
  pyautogui.sleep(3)
  search_button = pyautogui.locateCenterOnScreen('Data\\Browser_Search.png', confidence=0.9)
  
  
# open new tab
def new_tab():
  pyautogui.hotkey('ctrl', 't')


# search youtube
def search_youtube():
  pyautogui.write('youtube.com')
  pyautogui.press('Enter')


# Locate the search bar and click
def search_channel(channel_name):  
  # Search bar location
  search_button = pyautogui.locateCenterOnScreen('Data\\Youtube_Search.png', confidence=0.9)
  
  pyautogui.moveTo(search_button)
  pyautogui.click()
  
  # Write channel 
  pyautogui.write(channel_name)
  pyautogui.hotkey('Enter')
  
  
# Click on the channel
def click_channel():
  channel = pyautogui.locateCenterOnScreen('Data\\Channel_image.png', confidence=0.9)
  
  pyautogui.moveTo(channel)
  pyautogui.click()
  
  
# Click on subscription
def click_subscription():
  subscription = pyautogui.locateCenterOnScreen('Data\\Youtube_Subscribe.png', confidence=0.9)
  
  pyautogui.moveTo(subscription)
  pyautogui.click()
  
if __name__ == '__main__':
  # hang_time(3)
  channel_name = pop_up()
  open_browser()
  # new_tab()
  search_youtube()
  hang_time(5)
  search_channel(channel_name)
  hang_time(5)
  click_channel()
  hang_time(3)
  click_subscription()
  
  
