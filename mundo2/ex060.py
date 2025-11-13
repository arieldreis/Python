import math
print('Siga a orientação do comando abaixo')
n = int(input('Calcular o seu fatorial: '))
fatorial = math.factorial(n)
c = n
while c > 0:
    print('{}'.format(c), end="")
    print(f' x ' if c > 1 else ' = ', end="")
    print('{}' , end=" ".format(fatorial))
    c-=1