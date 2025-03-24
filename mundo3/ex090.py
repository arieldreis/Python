name = {"nome": input("Digite seu nome: ")}
media = {"nota": float(input("Digite a sua nota: "))}
print("=-"*30)
print(f" - Nome é igual a {name["nome"]}")
print(f" - Média é igual a {media["nota"]}")
if media["nota"] >= 7:
    print(" - Situação é igual a Aprovado!")
elif 5 <= media["nota"] < 7:
    print(" - Situação é igual a Recuperação!")
else:
    print(" - Situação é igual a Reprovado!")