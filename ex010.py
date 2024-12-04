import tkinter as tk
import tkinter.font as tkFont
def moedas():
    moedas = float(entrada.get())
    dolar =
    euro =
    peso =
root = tk.Tk()
root.title('Conversor de Moedas')
root.geometry("500x500")
root.configure(bg="black")
label = tk.Label(root, text='Conversor de Moedas.', bg="black", fg="white")
label.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
button = tk.Button(root, text='Clique Aqui', bg="red", fg="white")
button.pack(pady=10)
label_resultado = tk.Label(root, text="", bg="black", fg="white")
root.mainloop()
