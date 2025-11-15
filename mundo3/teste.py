'''lista = []
dici = {}
while True:
    dici["nome"] = input("Nome: ")
    dici["idade"] = int(input("Idade: "))
    if dici['nome'] == "N":
        print("Ok")
        break
    lista.append(dici.copy())
for item in lista:
    print(f"{item}")'''

lista = [["João", 100], ["Malcon", 75], ["Elton", 75], ["John", 100], ["Kaique", 67]]
for index in lista:
    maior = max(index[1])
    print(maior)
