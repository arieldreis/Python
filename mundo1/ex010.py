import tkinter as tk
import tkinter.font as tkFont

import requests


def moedas():
    reais = float(entrada.get())
    url = "https://economia.awesomeapi.com.br/last/USD,EUR"
    requisicao = requests.get(url)
    print(requisicao.json())
    dolar = reais * 0.17
    euro = reais * 0.16
    pesomexicano = reais * 3.36
    label_resultado['text'] = (f"Você tem R${reais} na sua carteira, e convertendo para ás seguintes moedas:\n"
                               f"US${round(dolar, 3)}\n"
                               f"€{round(euro, 3)}\n"
                               f"MXN{round(pesomexicano, 3)}")
root = tk.Tk()
root.title('Conversor de Moedas')
root.geometry("500x600")
root.configure(bg="black")
fonte = tkFont.Font(family="Helvética", size=14, weight="bold")
label = tk.Label(root, text='Conversor de Moedas.', bg="black", fg="white", font=fonte)
label.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
button = tk.Button(root,
                   text='Clique Aqui',
                   bg="red", fg="white",
                   command=moedas,
                   font=fonte,
                   cursor="hand2")
button.pack(pady=10)
# button.config(width=7)
# button.config(height=5)
label_resultado = tk.Label(root, text="", bg="black", fg="white", font=fonte)
label_resultado.pack(pady=10)
root.mainloop()
