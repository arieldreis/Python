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
label.pack(pady=10)
first = (tk.Entry(root))
first.pack(pady=10)
second = tk.Entry(root)
second.pack(pady=10)
button = tk.Button(root, text="SOMAR" , command=somar)
button.pack(pady=10)
label_resultado = tk.Label(root , text="")
label_resultado.pack(pady=10)
root.mainloop()