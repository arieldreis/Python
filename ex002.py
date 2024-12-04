'''nome = str(input('Digite o seu Nome: '))
print('Prazer em te conhecer {}'.format(nome))'''
import tkinter as tk
import tkinter.font as tkFont
def apresentacao():
    nome = entrada.get()
    label_resultado['text']= f'Olá {nome}! Bem-vindo ao mundo do Python!'
root = tk.Tk()
root.title('APRESENTAÇÃO')
root.geometry("300x200")
root.configure(bg="black")
fonte = tkFont.Font(family="Arial" , size=14 , weight="bold")
label = tk.Label(root, text='Digite o seu nome:', font=fonte, bg="black",fg="white")
label.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
button = tk.Button(root, text='Clique Aqui!' , command=apresentacao, font=fonte, bg="black",fg="white")
button.pack(pady=10)
label_resultado = tk.Label(root, text="", font=fonte , bg="black", fg="white")
label_resultado.pack(pady=10)
root.mainloop()