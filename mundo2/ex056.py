somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for x in range (1,5):
    print('-----{}º pessoa-----'. format(x))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade+=idade
    if x == 1 and sexo in 'M m':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F f' and idade < 20:
        totmulher20+=1
mediaidade = somaidade/4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem , nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))