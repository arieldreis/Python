import time
lista = []
while True:
    numero = int(input("Digite um número: "))
    resposta = str(input("Quer continuar? [Sim/Não]")).lower().capitalize()
    if numero in lista:
        print("Esse valor já está na lista.")
    else:
        lista.append(numero)
        if resposta == "Sim":
            print("Valor adicionado com sucesso!")
            time.sleep(2)
        if resposta == "Não":
            print("Fim do Programa!")
            print("AGUARDE...")
            time.sleep(2)
            print(f"A lista em ordem crescente: {sorted(lista)}")
            break