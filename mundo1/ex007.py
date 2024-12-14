import tkinter as tk 
import tkinter.font as tkFont
def calcular():
    inputone = float(notaone.get())
    inputtwo = float(notatwo.get())
    soma = (inputone + inputtwo) / 2
    if inputone > 10 or inputtwo > 10 or inputone < 0 or inputtwo < 0:
        label_resultado['text'] = (f"Dados Inválidos, digite um valor abaixo entre 0 e 10.")
    elif soma >= 7.0:
        label_resultado['text'] = (f"Você está aprovado ✅, continue estudando.")
    elif soma >= 5.0:
        label_resultado['text'] = (f"Você está de recuperação📚🤔, estude mais um pouco.")
    elif soma < 5.0:
        label_resultado['text'] = (f"Você está de reprovado😞❌")
    else:
        label_resultado['text'] = (f"A média entre {inputone} e {inputtwo} é igual á {round(soma, 2)}")
root = tk.Tk()
root.geometry("400x400")
root.title("Média Final!")
root.configure(bg="black")
fonte = tkFont.Font(family="Arial" , size=14 , weight="bold")
label = tk.Label(root, text="Digite a nota do aluno, logo abaixo: ", font=fonte, fg="white" , bg="black")
label.pack(pady=10)
notaone = tk.Entry(root)
notaone.pack(pady=10)
notatwo = tk.Entry(root)
notatwo.pack(pady=10)
button = tk.Button(root, text="Clique", font=fonte,command=calcular, fg="white", bg="red")
button.pack(pady=10)
label_resultado = tk.Label(root, text="", font=fonte, fg="white", bg="black")
label_resultado.pack(pady=10)
root.mainloop()