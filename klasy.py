import pyautogui
import time

class StartGame():
    def szukanieRozwiazania(self):
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

    def dubleWeryfication(self, sciezka):
        while True:
            if pyautogui.locateCenterOnScreen(sciezka, confidence=0.7):
                res = pyautogui.locateCenterOnScreen(sciezka, confidence=0.7)
                pyautogui.doubleClick(res)
                break

    def weryfication(self, sciezka, confidence=0.7, delate=0):
        start = int(time.time())
        time.sleep(delate)
        while True:
            if pyautogui.locateCenterOnScreen(sciezka, confidence=confidence):
                res = pyautogui.locateCenterOnScreen(sciezka, confidence=confidence)
                pyautogui.click(res)
                return 1
                break
            elif int(time.time()) > start + 20:
                print("wykonuje wyjątek")
                return 0






    def uruchom(self):
        print("klikniencie na skrut")
        print(int(time.time()))
        time.sleep(3)
        print(int(time.time()))

        StartGame.dubleWeryfication("grafika/skrut_na_pulpicie.png")

        print("klikniencie na skrut")
        StartGame.weryfication("grafika/jezyk.png")

        print("klikniencie na skrut")
        StartGame.weryfication("grafika/polska.png")

        print("okno wprowadzania loginu")
        StartGame.weryfication("grafika/okno_wprowadzania_loginu.png")

        print("kliknięcie na nik")
        StartGame.weryfication("grafika/masakra.png")

        print("kliknięcie zaloguj")
        StartGame.weryfication("grafika/zaloguj.png")

        print("kliknięcie na start")
        StartGame.weryfication("grafika/odbierz.png")

        print("klikniecie na wejście do gry")
        StartGame.weryfication("grafika/odbierz.png", 0.9, 1)


