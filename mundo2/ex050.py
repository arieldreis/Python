soma = 0
for x in range(1,7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        soma = soma + n
print('\033[0;34mA soma dos valores Pares é igual á {}\033[m'.format(soma))