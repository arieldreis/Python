teste = []
teste.append("Ariel")
teste.append(16)
galera = []
galera.append(teste[:])
teste[0] = "Maria" # Irá mudar os dados.
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
for p in galera:
    print(f"Nome: {p[0]} e Idade: {p[1]}")

galera = []
dados = []
for cont in range(0, 3):
    nome, idade = map(str, input("Digite: ").split())
    dados.append(nome)
    dados.append(idade)
    galera.append(dados[:])
print(galera)