n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
media = (n1 + n2) / 2
if media >= 6.0:
    print("Sua média foi boa! \033[1;34mPARABÉNS\033[m")
else:
    print("Sua média foi ruim! \033[1;33mESUDE MAIS!\033[m")