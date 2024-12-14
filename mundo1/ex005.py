'''digite = int(input('Digite um número: '))
s = digite + 1
m = digite - 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(digite,m,s))'''

import tkinter as tk
import tkinter.font as tkFont
def calcular():
    number = int(entrada.get())
    sucessor = number + 1
    antecessor = number - 1
    label_resultado['text'] = (f"O sucessor de {number} será {sucessor}\n"
                               f"O Antecessor de {number} será {antecessor}")
root = tk.Tk()
root.geometry("500x500")
root.title("Sucessor e Antecessor")
fonte_entrada = tkFont.Font(family="Arial" , size=14 , weight="bold")
label = tk.Label(root, text="Digite um número:" , font=fonte_entrada)
label.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
button = tk.Button(root, text="Calcular" , command=calcular , font=fonte_entrada)
button.pack(pady=10)
label_resultado = tk.Label(root, text="" , font=fonte_entrada)
label_resultado.pack(pady=10)
root.mainloop()