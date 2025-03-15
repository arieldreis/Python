import time
lista = []
while True:
    valor = int(input("Digite um valor: "))
    resposta = str(input("Deseja continuar? [Sim/Não]: ")).lower().capitalize()
    if valor in lista:
        print("Esse número é inaválido, pois já está na lista!⚠️⚠️🚨🚨")
    elif valor < 0 or valor > 200:
        print("O número informado está fora do intervalo permitido!⚠️⚠️🚨🚨")
    else:
        lista.append(valor)
        if resposta == "Sim":
            print("Valor adicionado com sucesso!")
            time.sleep(2)
        if resposta == "Não":
            print("Aguarde o fim do programa!")
            time.sleep(2)
            print("-"*50)
            print(f"A lista em ordem crescente: {sorted(lista, reverse=True)}") # Essa linha irá colocar os valores em ordem decrescente.
            print(f"Você digitou {len(lista)} elementos")
            if 5 in lista:
                print("O valor 5 faz parte da lista!")
            else:
                print("O valor 5 não faz parte da lista!")
            print("-"*50)
            break