cont = soma = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    soma+=numero
    cont+=1
print(f"A soma de todos os valores é igual {soma}")
print(f"E você digitou {cont} números.")