jogador =  {
    "jogados": str(input("Nome do jogador: ")),
}
total = 0
lista = []
partidas = int(input(f"Quantas partidas {jogador["jogados"]} jogou: "))
for c in range(0, partidas):
    gols = {
        "gols_marcados": int(input(f"Quantos gols na partida {c}: ")),
    }
    lista.append(gols["gols_marcados"])
    total += gols["gols_marcados"]
print("=-"*30)
dic = {
    "nome_jogador": jogador["jogados"],
    "numero_de_goals": lista,
    "saldo_goals": total
}
print(f"{dic}")
print("=-"*30)
print(f"O campo nome tem o valor {jogador['jogados']}")
print(f"O campo goals tem o valor {dic['numero_de_goals']}")
print(f"O campo total tem o valor {total}")
print("=-"*30)
print(f"O jogador {jogador['jogados']} jogou {partidas} partidas.")
for x in range (0, partidas):
    print(f"Na partida {x}, fez {lista[x]} goals.")
print(f"Foi um total de {total} goals.")
