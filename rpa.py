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

    #select file
    pyautogui.sleep(3)
    pyautogui.hotkey('enter')
    pyautogui.sleep(3)

    #name the file to "new_csv.csv"
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

    #select the working directory
    pyautogui.hotkey('enter')
    pyautogui.sleep(3)

    #go to button "open"
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

    import smtplib, ssl

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "dennis092589@gmail.com"
    receiver_email = "horjiayang@graduate.utm.my"
    password = input("Type your password and press enter:")
    message = """
    Subject: from python

    file succesfully copied."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    break





