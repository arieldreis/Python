import tkinter
import mysql.connector
import tkinter.font as TkFont
import tkcalendar
def cadastra():
    nome = nomeEntrada.get()
    sobrenome = sobrenomeEntrada.get()
    nascimento = nascimentoEntrada.get()
    email = emailEntrada.get()
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testePython"
    )
    cursor = conexao.cursor()
    comando = "INSERT INTO usuarios(nome, sobrenome, nascimento, email) VALUES (%s, %s, %s, %s)"
    valores = (nome, sobrenome, nascimento, email)
    cursor.execute(comando, valores)
    conexao.commit()
    print(cursor.rowcount, "Dados Inseridos")
root = tkinter.Tk()
root.geometry("500x500")
root.title("Conexão com Banco de Dados")
root.configure(bg="black")
fonte = tkinter.font.Font(family="Arial", size=15, weight="normal")
nomeText = tkinter.Label(root, text="Nome:", bg="black", fg="white", font=fonte)
nomeText.pack(pady=10)
nomeEntrada = tkinter.Entry(root)
nomeEntrada.pack(pady=5)
sobrenomeText = tkinter.Label(root, text="Sobrenome:", bg="black", fg="white", font=fonte)
sobrenomeText.pack(pady=10)
sobrenomeEntrada = tkinter.Entry(root)
sobrenomeEntrada.pack(pady=5)
nascimentoText = tkinter.Label(root, text="Nascimento: ", bg="black", fg="white", font=fonte)
nascimentoText.pack(pady=10)
nascimentoEntrada = tkcalendar.DateEntry(root) # Calendário em Python
nascimentoEntrada.pack(pady=10)
emailText = tkinter.Label(root, text="Email: ", bg="black", fg="white", font=fonte)
emailText.pack(pady=10)
emailEntrada = tkinter.Entry(root)
emailEntrada.pack(pady=5)
botao = tkinter.Button(root, text="Cadastrar", bg="red", fg="white", font=fonte, cursor="hand2", command=cadastra)
botao.pack(pady=10)
root.mainloop()
