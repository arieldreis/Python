n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
n4 = int(input("Digite outro número: "))
tupla_valores = (n1, n2, n3, n4)
print("=-"*30)
print(f"Você digitou os valores: {tupla_valores}.")
print(f"O valor 9 apareceu: {tupla_valores.count(9)} vezes.")
if 3 in tupla_valores:
    print(f"O valor 3 apareceu na posição {tupla_valores.index(3)}º.")
else:
    print("O valor 3 não não foi digitado.")
print("Os valores pares digitados foram: ")
for num in tupla_valores:
    if num % 2 == 0:
        print(f"{num}", end="➡️")
