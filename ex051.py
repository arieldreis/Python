print('\033[0;33m=\033[m'*40)
print('\033[0;94m10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA\033[m')
print('\033[0;33m=\033[m'*40)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Qual á Razão: '))
decimo = primeiro + (10 - 1) * razao
for x in range(primeiro,decimo + razao , razao):
    print('{}'.format(x) , end=" - ")
print('Acabou.')