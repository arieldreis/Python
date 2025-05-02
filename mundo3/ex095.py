import pandas as pd
lista = []
dadosjogador = {}
while True:
    dadosjogador["nome_jogador"] = str(input("Nome do Jogador: "))
    dadosjogador["partidas"] = int(input(f"Quantas partidas {dadosjogador['nome_jogador']} jogou: "))
    for cont in range(0, dadosjogador['partidas']):
        dadosjogador['gols'] = int(input(f"Quantos gols na {cont}ª partida: "))
        lista.append(dadosjogador['gols'])
    dadosjogador['soma'] = sum(lista)
    dadosjogador["confirmacao"] = str(input("Quer Continuar [S/N]: "))
    while dadosjogador["confirmacao"] != "S" and dadosjogador["confirmacao"] != "N":
        print("ENTRADA DE DADOS INCORRETA, DIGITE APENAS S OU N.")
        dadosjogador["confirmacao"] = str(input("Quer Continuar [S/N]: "))
    if dadosjogador["confirmacao"] == "N":
        print("TODOS OD JOGADORES FORAM SALVOS COM SUCESSO.")
        break
    if dadosjogador["confirmacao"] == "S":
        print("JOGADOR CADASTRADO COM SUCESSO.")
    dicionario = {
        "nome": dadosjogador['nome_jogador'],
        "gols": lista,
        "total": dadosjogador['soma']
    }
print("=-"*40)
df = pd.DataFrame(lista)

print(df)

'''
Permite iterar sobre sequências enquanto acompanhamos o 
índice de cada elemento. Ela facilita a manipulação dos dados durante a iteração 
e é especialmente útil quando precisamos percorrer várias sequências simultaneamente
'''
