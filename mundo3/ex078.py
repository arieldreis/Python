lista = []
for x in range(0, 5):
    numero = int(input(f"Digite um número na posição {x}º: "))
    lista.append(numero)
print("-"*40)
print(f"Você digitou os valores {lista}")
for i, valor in enumerate(lista):
    print(f"O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}")
    print(f"O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}")
    break