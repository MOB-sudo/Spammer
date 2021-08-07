import pyautogui, time
time.sleep(5)
i=open("ThingToSpam.txt", 'r')
for word in i:
  pyautogui.typewrite(word)
  pyautogui.press("enter")
    
