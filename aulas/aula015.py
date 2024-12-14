soma = 0
cont = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma+=numero
    cont+=1
    print(f"A soma dos valores é igual {soma}")
print(f"VocÊ digitou {cont} números")