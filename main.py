import pyautogui
import time
import klasy


def dubleWeryfication(sciezka):
    while True:
        if pyautogui.locateCenterOnScreen(sciezka, confidence=0.7):
            res = pyautogui.locateCenterOnScreen(sciezka, confidence=0.7)
            pyautogui.doubleClick(res)
            break

def weryfication(sciezka, confidence=0.7, delate=0):
    start = int(time.time())
    while True:
        if pyautogui.locateCenterOnScreen(sciezka, confidence=confidence):
            time.sleep(delate)
            res = pyautogui.locateCenterOnScreen(sciezka, confidence=confidence)
            pyautogui.click(res)
            break
        elif int(time.time())>start+20:
            print("wykonuje wyjątek")
            szukanieRozwiazania()


def szukanieRozwiazania():
    print('Wykonuję krzyzyk')
    if pyautogui.locateCenterOnScreen("grafika/wyjatki/krzyzyk.png", confidence=0.7):
        res = pyautogui.locateCenterOnScreen("grafika/wyjatki/krzyzyk.png", confidence=0.7)
        pyautogui.doubleClick(res)
        return 1

    if pyautogui.locateCenterOnScreen("grafika/wyjatki/prywatnosc.png", confidence=0.7):
        res = pyautogui.locateCenterOnScreen("grafika/wyjatki/prywatnosc.png", confidence=0.7)
        pyautogui.doubleClick(res)
        return 1

    else:
        return 0

for liczba in range(0,1):

    odpalenie = klasy.StartGame()
    #odpalenie.uruchom()
    print("klikniencie na skrut")
    print(int(time.time()))
    time.sleep(3)
    print(int(time.time()))

    odpalenie.dubleWeryfication("grafika/skrut_na_pulpicie.png")

    print("klikniencie na skrut")
    odpalenie.weryfication("grafika/jezyk.png")

    print("klikniencie na skrut")
    odpalenie.weryfication("grafika/polska.png")

    print("okno wprowadzania loginu")
    odpalenie.weryfication("grafika/okno_wprowadzania_loginu.png")

    print("kliknięcie na nik")
    odpalenie.weryfication("grafika/masakra.png")

    print("kliknięcie zaloguj")
    odpalenie.weryfication("grafika/zaloguj.png")

    print("kliknięcie na start")
    odpalenie.weryfication("grafika/start.png")

    print("klikniecie na wejście do gry")
    odpalenie.weryfication("grafika/start.png", 0.9, 10)


    print("klikniencie na zakończ")
    #weryfication("grafika/zalogowany.png")
    while True:
        if pyautogui.locateCenterOnScreen("grafika/zalogowany.png", confidence=0.7):
            time.sleep(2)
            res = pyautogui.locateCenterOnScreen("grafika/krzyzyk.png", confidence=0.7)
            pyautogui.click(res)
            break


print("koniec programu")
