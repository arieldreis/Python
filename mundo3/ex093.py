lista = []
dados = {
    "nome_jogador": str(input("Nome do Jogador: ")),
    "partidas": int(input(f"Quantas partidas {dados['partidas']} jogou: "))
}
for cont in range(0, dados["partidas"]):
    gols = int(f"Quantos gols na {cont}ª partida: ")
