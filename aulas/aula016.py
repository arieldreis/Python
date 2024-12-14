'''lista = []
cont = 0
while cont <= 4:
    solicitacao = int(input("Digite um número inteiro: "))
    lista.append(solicitacao)
    cont+=1
soma = sum(lista)
media = soma / len(lista)
print(f"A soma de todos os valores é igual {soma} e você digitou {cont} números.")
print(f"Analisando os valores o maior será {max(lista)} e a menor é {min(lista)}")
print(f"E a média dos valores é de {media}")
print(lista[3])'''

lista_produtos = ["Iphone" , "Airpod" , "MacBook", "Ipad"]
'''produto_procurado = input("Digite o produto que você procurando: ")
produto_procurado = produto_procurado.lower()
print(produto_procurado in lista_produtos)''' #Essa linha de código verifica se o determinado produto existe na lista retornando um valor booleano.

#Como adicionar um item em uma lista.
lista_produtos.append("Apple watch")
print(lista_produtos)
#Remover um item de uma lista
lista_produtos.remove("Apple watch")
print(lista_produtos)
lista_produtos.pop(2)
print(lista_produtos)
#Editar um item
preco = [1000, 1500, 3000]
preco[0] = 6000 #Essa linha código editou o valor da lista alterando o seu preço antigo.
print(preco)
#Contar quantas vesez um item aparece
lista_produtos = ["Iphone" , "Airpod" , "MacBook", "Ipad", "Iphone", "Iphone", "Ipad", "Airpod"]
print(lista_produtos.count("Airpod"))
#Ordenar uma lista
lista_produtos.sort() #Ordem Crescente
lista_produtos.sort(reverse=True) #Ordem Decrescente
print(lista_produtos)

listavazia = []
for x in range(5):
    numero = float(input("Digite: "))
    listavazia.append(numero)
soma = sum(listavazia)
media = soma / len(listavazia)
print(f"O resultado da soma é {soma}")
print(f"O resultado dessa média é de {round(media, 3)}")