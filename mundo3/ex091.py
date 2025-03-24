import time
import random
lista = []
lista_numeros = {
    "Jogador1": random.randint(1, 6),
    "Jogador2": random.randint(1,6),
    "Jogador3": random.randint(1,6),
    "Jogador4": random.randint(1,6)
}
print("VALORES SORTEADOS")
for index, cont in lista_numeros.items():
    print(f"{index} tirou {cont} no dado.")
    time.sleep(1)

print("-="*30)
print(" == RANKING DOS JOGADORES == ")
lista.append(lista_numeros)
for x in lista:
    print(f"{x}° lugar: {sorted(lista_numeros.keys())}")



