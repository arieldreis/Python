import random
primeiro = str(input("Primeiro Aluno:"))
segundo = str(input("Segundo Aluno:"))
terceiro = str(input("Terceiro Aluno:"))
quarto = str(input("Quarto Aluno: "))
escolha = random.sample([primeiro, segundo, terceiro, quarto] , k=4)
print(f"A ordem da apresentação será\n{escolha}")