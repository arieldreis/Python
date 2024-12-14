primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira + segunda) / 2
if media >= 7.0:
    print('Aprovado!!')
elif 5.9  < media  < 7.0:
    print('Recuperação!!')
else:
    if media < 5.0:
        print('Reprovado!!')