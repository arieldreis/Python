#Programa de par ou ímpar
par_impar = int(input('Digite um número: '))
num = (par_impar%2 == 0)
impar = (par_impar%2 == 1)
if num:
    print('O número {} é par'.format(par_impar))
else:
    print('O número {} é ímpar'.format(par_impar))