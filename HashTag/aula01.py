import pyautogui
import time
import pandas
'''
    pyautogui.click -> clica em algum lugar
    pyautogui.press -> aperta uma tecla
    pyautogui.write -> escreve um texto
    pyautogui.hotkey -> aperta uma combinação teclas
'''

pyautogui.PAUSE = 3
# abre a pagina do edge
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press('enter')
# digita um link no edge
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
# espera 4 segundos
time.sleep(4)
# digita os dados no campo de login
pyautogui.click(854, 458)
pyautogui.write('arieldreis.gmail.com')
pyautogui.press('tab')
pyautogui.write('Ariel2805.a')
pyautogui.click(925, 677)
# Importar a base de dados
tabela = pandas.read_csv("product.csv")
print(tabela)
# cadastrar produtos
pyautogui.click(703, 316)