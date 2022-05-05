import pyautogui
import time

time.sleep(2)

res = pyautogui.locateCenterOnScreen("grafika/skrut_na_pulpicie.png", confidence=0.7)
pyautogui.doubleClick(res)

time.sleep(5)
res = pyautogui.locateCenterOnScreen("grafika/okno_wprowadzania_loginu.png", confidence=0.7)
pyautogui.click(res)

time.sleep(2)
res = pyautogui.locateCenterOnScreen("grafika/masakra.png", confidence=0.7)
pyautogui.click(res)

time.sleep(2)
res = pyautogui.locateCenterOnScreen("grafika/zaloguj.png", confidence=0.7)
pyautogui.click(res)

time.sleep(3)
res = pyautogui.locateCenterOnScreen("grafika/start.png", confidence=0.7)
pyautogui.click(res)

time.sleep(20)
res = pyautogui.locateCenterOnScreen("grafika/start_do_odebrania.png", confidence=0.7)
pyautogui.click(res)

time.sleep(20)
res = pyautogui.locateCenterOnScreen("grafika/krzyzyk.png", confidence=0.7)
pyautogui.click(res)

