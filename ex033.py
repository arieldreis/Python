a= int(input('Digite um número:'))
b= int(input('Digite um número:'))
c= int(input('Digite outro número:'))
if a<b and a<c:
    menor=a
if b<c and b<a:
    menor=b
if c<a and c<b:
    menor=c
if a>b and a>c:
    maior=a
if b>c and b>a:
    maior=b
if c>a and c>b:
    maior=c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))