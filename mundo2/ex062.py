print('\033[0;34m=-\033[m'*30)
print('\033[0;32mGerador de Pogressão Aritimética\033[m')
print('\033[0;34m=-\033[m'*30)
primeiro = int(input('Primero termo:'))
razao = int(input('Razão da Progressão Aritimética:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total+=mais
    while cont <= total:
        print(f'{termo}', end=' ➜ ')
        cont += 1
        termo += razao
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Aritimética finalizada com {} termos mostrados'.format(total))