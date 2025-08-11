import tkinter as tk
import tkinter.font as tkFont
import requests
def teste():
    requisicao = requests.get("https://zenquotes.io/api/quotes/random")
    dados = requisicao.json()
    print(requisicao.json())
    entrada = dados[0].get('q')
    resposta['text'] = f"{entrada}"
root = tk.Tk()
root.title("Frases Motivacionais")
root.geometry("600x400")
root.configure(bg="black")
fonte = tkFont.Font(family="Arial", size=14, weight="normal")
label1 = tk.Label(root,
                  text="Clique no botão para receber uma frase motivacional",
                  bg="black",
                  fg="white", font=fonte)
label1.pack(pady=10)
botao = tk.Button(root,
                  text="FRASES MOTIVACIONAIS",
                  bg="red",
                  fg="white",
                  cursor="hand2",
                  font=fonte,
                  command=teste)
botao.pack(pady=10)
resposta = tk.Label(root,
                  text="",
                  bg="black",
                  fg="white", font=fonte)
resposta.pack(pady=10)
root.mainloop()