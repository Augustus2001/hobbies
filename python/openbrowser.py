#pyautogui bot
import time
import webbrowser
import pyautogui

"""
test open url and dowload picture
def opensearch(a):
    webbrowser.open("www.google.com")
    pyautogui.sleep(1)
    pyautogui.click(170,490)
    pyautogui.write(a+" map")
    pyautogui.press("enter")
    pyautogui.sleep(1)
    pyautogui.click(156,244)
    pyautogui.sleep(1)
    pyautogui.moveTo(156,384)
    pyautogui.sleep(1)
    pyautogui.rightClick()
    pyautogui.sleep(1)
    pyautogui.press("v")
    pyautogui.sleep(1)
    pyautogui.write(a)
    pyautogui.press("enter")
opensearch("japan")
opensearch("thailand")
opensearch("france")
opensearch("itali")
"""
#more easy way to dowload
#take screen shot pyautogui.screenshot()
url="www.google.com"
webbrowser.open(url)
time.sleep(1)
pyautogui.write("thailand",interval=0.01)
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("{}.jpg".format("thailand"))