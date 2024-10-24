soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        soma+=x
        cont+=1
        print('\033[0;94mA soma de todos os {} valores é igual á {}\033[m'.format(cont, soma))