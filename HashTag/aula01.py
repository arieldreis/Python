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
# Cadastrar produtos e clicar no primeiro input
for lista in tabela.index:
    pyautogui.click(703, 316)
    codigo = tabela.loc[lista, "codigo"] # O comando loc é comando de localização
    pyautogui.write(codigo)
    pyautogui.press("tab") # Passar para o próximo campo

    marca = tabela.loc[lista, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab") # Passar para o próximo campo

    tipo = tabela.loc[lista, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab") # Passar para o próximo campo

    categoria = tabela.loc[lista, "categoria"]
    pyautogui.write(categoria)
    pyautogui.press("tab") # Passar para o proxímo campo

    preco = tabela.loc[lista, "preco"]
    pyautogui.write(preco)
    pyautogui.press("tab") # Passar para o proxímo campo

    preco_unitario = tabela.loc[lista, "preco_unitario"]
    pyautogui.write(preco_unitario)
    pyautogui.press("tab") # Passar para o proxímo campo

    obs = "AINDA NÃO DEFINIDO"
    pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    '''NOVO COMANDO'''
    '''No comando scroll do pyautogui se vc colocar números positivos a rolagem é para cima se for negativo a rolagem é para baixo.'''
    pyautogui.scroll(10000)
# Passo 5: Repetir todos os produtos
