solicitacao = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while solicitacao != 'M' and solicitacao != 'F':
    solicitacao = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Dados {} registrado com sucesso.'.format(solicitacao))