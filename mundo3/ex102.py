def fatorial(numero):
    cont = 1
    mult = 1
    resultado = 1
    while cont <= numero:
        print(f'{cont}', end="")
        if cont < user:
            print(" x ", end="")
        else:
            print(f" = ", end="")
            print(resultado)
        resultado *= cont
        cont += 1

user = int(input("Digite: "))
print(fatorial(user))