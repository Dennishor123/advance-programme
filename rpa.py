import pyautogui

while True:
    # Launch CSVBuddy
    pyautogui.hotkey('winleft')
    pyautogui.sleep(2)

    pyautogui.typewrite('CSVBuddy-3_0-32-bit - Shortcut')
    pyautogui.sleep(3)
    pyautogui.hotkey('enter')

    # select file
    pyautogui.sleep(5)
    pyautogui.hotkey('enter')
    pyautogui.sleep(3)
    pyautogui.typewrite('sample_csv.csv') 

    pyautogui.sleep(3)
    pyautogui.hotkey('enter')
    
    #load csv
    pyautogui.sleep(3)
    pyautogui.hotkey('enter') 

    pyautogui.sleep(3)
    pyautogui.hotkey('enter') #press ok
    
    #switch to "Save CSV File" tab
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl','tab')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl','tab')

    pyautogui.sleep(3)
    pyautogui.hotkey('enter')
    pyautogui.sleep(3)

    pyautogui.typewrite('new_csv.csv')
    pyautogui.sleep(3)
    #pyautogui.hotkey('enter')

    # tab 8 times
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)

    # go to the working directory
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(1)
    pyautogui.hotkey('up')
    pyautogui.sleep(3)

    pyautogui.hotkey('enter')
    pyautogui.sleep(3)

    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('enter')
    
    #save file
    pyautogui.sleep(3)
    pyautogui.hotkey('enter')

    pyautogui.sleep(5)

    break





