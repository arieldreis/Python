'''nome = str(input('Digite o seu Nome: '))
print('Prazer em te conhecer {}'.format(nome))'''
import tkinter as tk
def apresentacao():
    nome = entrada.get()
    label_resultado['text']= f'Olá {nome}! Bem-vindo ao mundo do Python!'
root = tk.Tk()
root.title('APRESENTAÇÃO')
root.geometry("300x200")
label = tk.Label(root, text='Digite o seu nome:')
label.pack()
entrada = tk.Entry(root)
entrada.pack()
print("")
button = tk.Button(root, text='Clique Aqui!' , command=apresentacao)
button.pack()
label_resultado = tk.Label(root, text="")
label_resultado.pack()
root.mainloop()