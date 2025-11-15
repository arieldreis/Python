dados = []
totPesoMaior = 0
totPesoMenor = 0
while True:
    nome = input("Digite seu nome: ")
    peso_int = float(input("Digite o seu peso: "))
    pessoas = (nome, peso_int)

    confirmacao = input("Quer Continuar? [S/N] ").lower().capitalize()
    dados.append(pessoas)
    totalPessoas = len(dados)
    if
    if confirmacao == "S":
        continue
    if confirmacao == "N":
        print("=-" * 30)
        break

if totalPessoas > 1:
    print(f"Ao todo temos {totalPessoas} pessoas cadastradas.")
else:
    print(f"Ao todo temos {totalPessoas} pessoa cadastrada.")

print(f"Os maiores pesos registrados foram de {totPesoMaior} pelas pessoas")
print(f"Os menores pesos registrados foram de {totPesoMenor} pelas pessoas.")
