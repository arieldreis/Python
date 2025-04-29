import time
lista = []
dados = {}
while True:
    dados["nome"] = str(input("Nome: "))
    dados["sexo"] =  str(input("Sexo [M/F]: "))
    # Pepetição de dados caso o usuário coloque errada.
    while dados["sexo"] != "M" and dados["sexo"] != "F":
        print("ERRO! Por favor, digite apenas M ou F")
        dados["sexo"] = str(input("Sexo [M/F]: "))
    # Idade do Usuário
    dados["idade"] = int(input("Idade: "))
    # Confirmação para continuar ou parar o código
    dados_usuarios = {
        "nomeuser": dados['nome'],
        "sexouser": dados['sexo'],
        "ageuser": dados['idade']
    }
    lista.append(dados_usuarios)
    dados["confirmacao"] = str(input("Quer continuar [S/N]: ")).lower().capitalize()
    while dados["confirmacao"] != "S" and dados["confirmacao"] != "N":
        print("ERRO! Responda S ou N.")
        dados["confirmacao"] = str(input("Quer continuar [S/N]: ")).lower().capitalize()
    if dados["confirmacao"] == "N":
        print("Todos os usuários foram cadastrados com sucesso.")
        print("Veja os usuários cadastrados logo abaixo.")
        break
    if dados["confirmacao"] == "S":
        print("Usuário cadastrado com sucesso!")
quant = len(lista)
soma_idades = sum(pessoa["ageuser"] for pessoa in lista)
media = soma_idades / quant
print(f"A) Ao todo temos {quant} pessoas cadastradas.")
print(f"B) A média de idade é {media:.2f} anos.")
tothomens = 0
totmulher = 0
for dado in lista:
    if dado["sexouser"] == "M":
        tothomens+=1
    elif dado["sexouser"] == "F":
        totmulher += 1
print(f"C) As mulheres cadastradas foram {totmulher} ao total.")
print("D) Lista das pessoas acima da média: ")
for acima_media in lista:
    print(acima_media)
    if acima_media['ageuser'] >= media:
        # print(f"Nome: {acima_media['nomeuser']}; Sexo: {acima_media['sexouser']}; Idade: {acima_media['ageuser']}")
        for k,v in acima_media.items():
            print(f"{k} = {v}; ", end='; ')
print("<<<ENCERRADO!>>>")
