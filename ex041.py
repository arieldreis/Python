ano = int(input('\033[0;93mAno de Nascimento:\033[m'))
if ano >= 2015:
    mirim = 2024-ano
    print('A sua categoria é Mirim.\nO atleta tem {}'.format(mirim))
elif 2014 <= ano <= 2010:
    infaltil = 2024-ano
    print('A  sua categoria é Infaltil.\nO atleta tem {} anos.'.format(infaltil))
elif 2013 <= ano <= 2005:
    junior = 2024 - ano
    print('A sua categoria é Junior.\nO atleta tem {} anos'.format(junior))
elif 2004 <= ano <= 1999:
    senior = 2024 - ano
    print('A sua categoria é Sênior.\nO atleta tem {} anos'.format(senior))
else:
    if ano <= 1998:
        print('A sua categoria é Master.\nO atleta tem {} anos'.format(ano))