jogadoresArray = []
jogadoresDicio = {}
somaGols = []
while True:
    jogadoresDicio["jogador"] = str(input("Nome do jogador: "))
    jogadoresDicio["numeroPartidas"] = int(input(f"Quantas partidas {jogadoresDicio['jogador']} jogou: "))
    for cont in range(0, jogadoresDicio['numeroPartidas']):
        jogadoresDicio['numeroGols'] = int(input(f"Quantos gols na partida {cont}: "))
    confirmacao = str(input("Quer Continuar [S/N]: ")).capitalize().lower()
    while confirmacao != "S" and confirmacao != "N":
        print("ERRO! Responda S ou N.")
        confirmacao = str(input("Quer Continuar [Sim/Não]: ")).capitalize().lower()
    if confirmacao == "N":
        print("Todos os usuários foram cadastrados com sucesso.")
        break
    if confirmacao == "S":
        print("Usuário cadastrado com sucesso!")
    somaGols.append(jogadoresDicio['numeroGols'])
    players = {
        "nomeJogador": jogadoresDicio['jogador'],
        "gols": jogadoresDicio['numeroGols'],
        "total": sum(somaGols)
    }
print(players)
'''Permite iterar sobre sequências enquanto acompanhamos o 
índice de cada elemento. Ela facilita a manipulação dos dados durante a iteração 
e é especialmente útil quando precisamos percorrer várias sequências simultaneamente'''
