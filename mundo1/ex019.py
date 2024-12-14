import random
primeiro = str(input("Primeiro Aluno:"))
segundo = str(input("Segundo Aluno:"))
terceiro = str(input("Terceiro Aluno:"))
quarto = str(input("Quarto Aluno: "))
sorteio = random.choice([primeiro, segundo, terceiro, quarto])
print(f"A pessoa escolhida será {sorteio}")