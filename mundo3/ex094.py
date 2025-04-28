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
        print(lista)
        break
    if dados["confirmacao"] == "S":
        print("Usuário cadastrado com sucesso!")
