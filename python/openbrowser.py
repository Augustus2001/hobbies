#pyautogui bot
import time
import webbrowser
import pyautogui
"""
def opensearch(a):
    webbrowser.open("www.google.com")
    pyautogui.sleep(1)
    pyautogui.click(170,490)
    time.sleep(1)
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
    time.sleep(1)
    pyautogui.hotkey("ctrl","w")
opensearch("japan")
opensearch("thailand")
opensearch("france")
opensearch("itali")

"""
#more easy
#take screen shot pyautogui.screenshot()itali

def load(word):
    url="www.google.com"
    webbrowser.open(url)
    time.sleep(1)
    pyautogui.write(word)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.screenshot("{}.jpg".format(word))
    time.sleep(1)
    pyautogui.hotkey("ctrl","w")
def main():
    return
if __name__=="__main__":
    load("thailand")
    load("england")
