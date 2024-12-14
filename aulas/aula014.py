'''for x in range(1, 10+1):
    print(x)
print('Fim do Programa!!!!')'''
'''c = 1
while c < 10:
    print(c)
    c+=1
print('Fim')'''
'''n = 1
while n != 10:
    n = int(input('Digite um número: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
        n = int(input('Digite um valor: '))
        r = str(input('Quer continuar? [S/N]')).upper() 
print('Fim do Programa')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par+=1
        else:
            impar+=1
print('Você digitou {} pares e {} ímpares'.format(par, impar))

'''numero = 1
while numero < 10:
    print(numero)
    numero+=1 #Se vc tirar essa linha de código irá ocorrer um loop infinito. 
#OBS: Em um loop while, é importante que cuidemos dos critérios de parada.'''
'''c = 1
while c < 10:
    print(c , end=' ')
    c+=1'''
'''soma = 0
n = int(input('Digite um número (0 para parar):'))
while n != 0:
    n = int(input('Digite um número (0 para parar):'))
    soma+=n
print(f'A soma dos valores é igual {soma}')'''
