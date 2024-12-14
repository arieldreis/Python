print('\033[0;34m=-\033[m'*30)
print('\033[0;32mGerador de Pogressão Aritimética\033[m')
print('\033[0;34m=-\033[m'*30)
primeiro = int(input('Primero termo:'))
razao = int(input('Razão da Progressão Aritimética:'))
termo = primeiro
cont = 1
while cont <= 5:
    print(f'{termo}', end=' ➜ ')
    cont = cont +1
    termo+=razao
print('ACABOU!!!')