nome = str(input('Qual é o seu nome:'))
if nome == 'Ariel':
    print('Que nome bonito {}'.format(nome))
    print('Tenha um otimo dia {}'.format(nome))
elif nome == 'Gustavo' or nome == 'Maria' or nome == 'Kevin':
    print('Seu nome é bem popular no brasil!')
elif nome in 'Malcon Osvaldo Carol':
    print('Seu nome é estranho')
else:
    print('Seu nome é bem comum!')