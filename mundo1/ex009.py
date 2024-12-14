'''digite = int(input('Digite um número para ver a sua tabuada: '))
for x in range(1,11):
    multplicacao = digite * x
    print(f'{digite} x {x} = {multplicacao}')'''

import tkinter as tk
import tkinter.font as tkFont
def tabuada():
    tabuada = int(entrada.get())
    c = 1
    resultado=""
    while c <= 10:
        mult = tabuada * c
        resultado+=f"{tabuada} x {c} = {mult}\n"
        label_resultado['text'] = resultado
        c+=1
root = tk.Tk()
root.geometry("700x400")
root.title("Tabuada")
fonte = tkFont.Font(family="Verdana", size=14, weight="bold")
label = tk.Label(root, text="Digite um número:", font=fonte)
label.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
button = tk.Button(root, text="Clicar!", command=tabuada, font=fonte)
button.pack(pady=10)
label_resultado = tk.Label(root, text="", font=fonte)
label_resultado.pack(pady=10)
root.mainloop()