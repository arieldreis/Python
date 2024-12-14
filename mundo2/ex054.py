totmaior = 0
totmenor = 0
for x in range(1,8):
    n = int(input('Em que ano nasceu á {}º pessoa: '.format(x)))
    c = 2024 -  2006
    if c >= 18:
        totmaior+=1
    else:
        totmenor+=1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tivemos {} pessoas menores de idade.'.format(totmenor))