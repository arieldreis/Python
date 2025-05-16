lista = []
dici = {}
while True:
    dici["nome"] = input("Nome: ")
    if dici['nome'] == "N":
        print("Ok")
        break
    lista.append(dici.copy())
for item in lista:
    print(f"{item}")
