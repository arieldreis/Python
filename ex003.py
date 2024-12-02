'''n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print(f"{n1} + {n2} = {s}")'''
import tkinter as tk
def somar():
    numberone = int(first.get())
    numbertwo = int(second.get())
    soma = numberone + numbertwo
    label_resultado['text'] = f"A soma entre {numberone} + {numbertwo} = {soma}"
root = tk.Tk()
root.title("SOMA DE DOIS NÚMEROS")
root.geometry("300x400")
label = tk.Label(root , text="Digite dois números nos campos á seguir!")
label.pack()
first = (tk.Entry(root))
first.pack()
second = tk.Entry(root)
second.pack()
button = tk.Button(root, text="SOMAR" , command=somar)
button.pack()
label_resultado = tk.Label(root , text="")
label_resultado.pack()
root.mainloop()