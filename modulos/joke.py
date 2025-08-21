import tkinter as tk
import tkinter.font as tkFont
import requests
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    requisicao = requests.get(url)
    dadosJson = requisicao.json()
    jokeQuestion = dadosJson["setup"]
    jokeAnswer = dadosJson["delivery"]
    resposta['text'] = f"Question: {jokeQuestion}\nAnswer: {jokeAnswer}"
root = tk.Tk()
root.title("JOKES API")
root.geometry("600x400")
root.configure(bg="black")
fonte = tkFont.Font(family="Arial", size=14, weight="normal")
label1 = tk.Label(root,
                  text="Clickon button and receive a joke.",
                  bg="black",
                  fg="white", font=fonte)
label1.pack(pady=10)
botao = tk.Button(root,
                  text="JOKES",
                  bg="red",
                  fg="white",
                  cursor="hand2",
                  font=fonte,
                  command=get_joke)
botao.pack(pady=10)
resposta = tk.Label(root,
                  text="",
                  bg="black",
                  fg="white", font=fonte)
resposta.pack(pady=10)
root.mainloop()