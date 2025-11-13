# Exemplo F
while True:
    quantidade = int(input())
    lista = []
    for index in range(quantidade):
        requisicoes = map(int, input().split())
        lista.append(requisicoes)
        maior_valor = max(lista)
        min_valor = min(lista)
        print(maior_valor, min_valor)

    