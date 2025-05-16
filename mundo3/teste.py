lista = []
dici = {}
while True:
    dici["nome"] = input("Nome: ")
    dici["idade"] = int(input("Idade: "))
    if dici['nome'] == "N":
        print("Ok")
        break
    lista.append(dici.copy())
for item in lista:
    print(f"{item}")
