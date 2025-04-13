lista = []
dadosjogador = {}
dadosjogador["nome_jogador"] = str(input("Nome do Jogador: "))
dadosjogador["partidas"] = int(input(f"Quantas partidas {dadosjogador['nome_jogador']} jogou: "))
for cont in range(0, dadosjogador['partidas']):
    dadosjogador['gols'] = int(input(f"Quantos gols na {cont}ª partida: "))
    lista.append(dadosjogador['gols'])
dadosjogador['soma'] = sum(lista)
dicionario = {
    "nome": dadosjogador['nome_jogador'],
    "gols": lista,
    "total": dadosjogador['soma']
}
print("=-"*30)
print(f"{dicionario}")
print("=-"*30)
print(f"O campo nome tem o valor {dicionario['nome']}")
print(f"O campo gols tem o valor {dicionario['gols']}")
print(f"O campo total tem o valor {dicionario['total']}")
print("=-"*30)
print(f"O jogagor {dicionario['nome']} jogou {dadosjogador['partidas']} partidas")
for indice, gol in enumerate(lista):
    print(f" => Na patida {indice}, fez {gol} gols.")
print("=-"*30)

'''Permite iterar sobre sequências enquanto acompanhamos o 
índice de cada elemento. Ela facilita a manipulação dos dados durante a iteração 
e é especialmente útil quando precisamos percorrer várias sequências simultaneamente'''
