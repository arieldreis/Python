numero = int(input('Digite um número qulquer: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 100
m = numero // 1000 % 1000
print('Ao analisar o número posso perceber que ele possui...')
print('{} Unidades'.format(u))
print('{} Dezenas'.format(d))
print('{} Centenas'.format(c))
print('{} Unidade de Milhar'.format(m))