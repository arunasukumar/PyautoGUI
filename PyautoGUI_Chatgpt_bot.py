# step 1 go to the chrome
# step 2 open chatgpt
# step 3 type -give me 10 motivational quotes
# step 4 copy the quotes
# step 6 open notes
# step 7 opena new note
# step 8 Write the title "Motivational Quotes"
# step 9 paste the quotes in the note
import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

#step 1 go to the chrome
pyautogui.hotkey('command', 'space', interval=0.25)
time.sleep(1)
pyautogui.typewrite('chrome')
time.sleep(1)
pyautogui.press('enter')

#step 2 open chatgpt
pyautogui.hotkey('command', 't', interval=0.25)
time.sleep(1)
pyautogui.typewrite('https://chat.openai.com/')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#step 3 type -give me 10 motivational quotes
pyautogui.write('give me 10 motivational quotes')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Move to the beginning of the quotes
pyautogui.moveTo(300, 250, duration=0.5)
time.sleep(5)

# Drag to the end of the quotes
pyautogui.dragTo(900, 700, duration=1, button="left")
time.sleep(2)

# step 4 copy the quotes
pyautogui.hotkey('command', 'c', interval=0.25)
time.sleep(1)
pyautogui.hotkey('command', 'space', interval=0.25)
time.sleep(1)

# step 6 open notes
pyautogui.typewrite('notes')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# step 7 opena new note
pyautogui.hotkey('command', 'n', interval=0.25)
time.sleep(1)

# step 8 Write the title "Motivational Quotes"
pyautogui.write("Motivational Quotes", interval=0.05)
pyautogui.press("enter")
pyautogui.press("enter")

# step 9 paste the quotes in the note
pyautogui.hotkey('command', 'v', interval=0.25)
time.sleep(1)




