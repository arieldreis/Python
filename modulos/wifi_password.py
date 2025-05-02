import time

import pyautogui
pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
app = "Whatszapp Web"
pyautogui.write(app)
pyautogui.press("enter")
pyautogui.click(336, 524)
time.sleep(4)
pyautogui.click(369, 235)
nome_contato = "+551196728-2605"
pyautogui.write(nome_contato)
pyautogui.press("enter")
pyautogui.click(994, 951)
for cont in range(1, 100):
    numero = cont+1
    pyautogui.write(numero)
    pyautogui.press("enter")
