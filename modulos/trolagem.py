import pyautogui as py
import random
import time

time.sleep(5)
mensagens = ["Tá doidão", "Tudo certo?", "E ai",
             "Partiu", "Coe", "Eita pesado", "Ai, sim", "Tmj", "Eh nois"]
py.click(1166, 1056)
py.click(988, 958)
for contador in range(50):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")