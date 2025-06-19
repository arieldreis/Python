import tkinter
import tkinter.font
import pygame
import random
def molecula():
    usuario = int(moleculaMolde.get())
    if usuario.strip() == "":
        resultado['text'] = f"Preencha o campo para iniciarmos o nosso jogo!"
    numeroMaquina = random.randint(1, 50)
    if usuario == numeroMaquina:
        resultado['text'] = (f"Parabéns você ganhou!")
        pygame.mixer.init() # Inicia a música
        pygame.mixer.music.load("") # Importa o arquivo da música
        pygame.mixer.music.play() # Toca a música
    elif usuario > 50 or usuario < 0:
        resultado['text'] = (f"Desculpa mais o nosso jogo só aceita valores de 0 até 50.")
    else:
        resultado['text'] = (f"Não foi dessa vez!")
        pygame.mixer.init()  # Inicia a música
        pygame.mixer.music.load("")  # Importa o arquivo da música
        pygame.mixer.music.play()  # Toca a música
root = tkinter.Tk()
fonte = tkinter.font.Font(family="Arial", size=16, weight="bold")
root.title("Jogo de Adivinhação")
root.geometry("500x600")
root.configure(bg="black")
label = tkinter.Label(root, text="Digite o seu palpite: ", bg="black", fg="white", font=fonte)
label.pack(pady=10)
moleculaMolde = tkinter.Entry(root)
moleculaMolde.pack(pady=10)
botao = tkinter.Button(root, text="Click on!", bg="red", fg="white", command=molecula, font=fonte, cursor="hand2")
botao.pack(pady=10)
resultado = tkinter.Label(root, text="", bg="black", fg="white", font=fonte)
resultado.pack(pady=10)
root.mainloop()