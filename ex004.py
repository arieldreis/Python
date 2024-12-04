'''entrada = str(input('Digite algo: '))
print('O tipo primitivo desse valor é ',type(entrada))
print("Só tem espaços?",entrada.isspace())
print("É um número?",entrada.isnumeric())
print("É alfabetico?",entrada.isalpha())
print('É alfanumérico',entrada.isalnum())
print("Está em minúscula",entrada.islower())
print("Está em Maiúscula",entrada.isupper())
print("Está capitalizada",entrada.istitle())'''

import tkinter as tk
def variavel():
    frase = str(entrada.get())  # Pega o texto da entrada
    label_resultado['text'] = (f"O tipo primitivo desse valor é {type(frase)}\n"
                               f"É um número? {frase.isnumeric()}\n"
                               f"Só tem espaços? {frase.isspace()}\n"
                               f"É alfabético? {frase.isalpha()}\n"
                               f"É minúscula? {frase.islower()}\n"
                               f"É capitalizada? {frase.istitle()}\n"
                               f"É maiúscula? {frase.isupper()}")

# Configuração da interface gráfica
root = tk.Tk()
root.geometry("400x400")
root.title("Dissecando uma Variável")
# Widgets da interface
label = tk.Label(root, text="Digite algo:")
label.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
button = tk.Button(root, text="CLIQUE", command=variavel)
button.pack(pady=10)
button.config(width=8, height=3)
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)
# Inicia a interface gráfica
root.mainloop()