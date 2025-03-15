impares = []
while True:
    numeros = int(input("Digite um número: "))
    resposta = str(input("Deseja continuar [SIM/NÃO]: ")).lower().capitalize()
    if numeros in lista:
        print("Esse número é inaválido, pois já está na lista!⚠️⚠️🚨🚨")
    elif numeros < 0 or numeros > 100:
        print("O número informado está fora do intervalo permitido!⚠️⚠️🚨🚨")
    else:
        lista.append(numeros)
        if numeros % 2 == 0:
            pares.append(numeros)
        else:
            impares.append(numeros)

        if resposta == "Sim":
            print("Valor adicionado com sucesso!")
            time.sleep(1)
        if resposta == "Não":
            print("Aguarde o fim do programa!")
            time.sleep(1)
            break

print(f"A lista de forma completa: {lista}")
print(f"A lista de números pares: {pares}")
print(f"A lista de números impares: {impares}")