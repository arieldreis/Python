'''nome = str(input('Digite o seu Nome: '))
print('Prazer em te conhecer {}'.format(nome))'''
import tkinter as tk
root = tk.Tk()
root.title('APRESENTAÇÃO')
root.geometry("300x200")
label = tk.Label(root, text='Digite o seu nome:')
label.pack()
button = tk.Button(root, text='Clique Aqui!')
button.pack()
root.mainloop()
