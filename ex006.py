'''number = int(input('Digite um número: '))
dobro = number * 2
triplo = number * 3
raiz = number ** 0.5
print('O dobro de {} vale {}'.format(number,dobro))
print('O triplo de {} vale {}'.format(number,triplo))
print('A raiza quadrada de {} vale {}'.format(number,raiz))'''

import tkinter as tk
import tkinter.font as tkFont

def calcular():
     number = float(input.get())
     dobro = number * 2
     triplo = number * 3
     raiz = number ** 0.5
     label_resultado['text'] = (f"O dobro de {number} vale {dobro}\n"
                                f"O triplo de {number} vale {triplo}\n"
                                f"A raiza quadrada de {number} vale {round(raiz,3)}")
root = tk.Tk()
root.geometry("400x400")
root.title("Dobro Triplo Raiz-Quadrada")
label = tk.Label(root, text="Digite um Número logo abaixo:")
label.pack(pady=10)
input = tk.Entry(root)
input.pack(pady=10)
button = tk.Button(root, text="Click me!", command=calcular)
button.pack(pady=10)
button.config(width=8)
button.config(height=3)
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)
root.mainloop()