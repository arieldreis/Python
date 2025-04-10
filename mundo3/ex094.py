import time
lista = []
while True:
    nome_idade = {
        "nome": str(input("Nome: ")),
        "idade": int(input("Idade: "))
    }
    sexo = {"sexo": str(input("Sexo [M/F]: ")).lower().capitalize()}
    if sexo["sexo"] != "M" or sexo["sexo"] != "F":
        print("ERRO! Por favor, digite apenas M ou F.")
        sexo = {"sexo": str(input("Sexo [M/F]: ")).lower().capitalize()}
    else:
        print("OK")
        break