#Alistamento no execito
nascimento = int(input('Ano de Nascimento: '))
idade_atual = 2024 - nascimento #Essa variável irá calcular a idade atual do soldado.
alistamento_exato = nascimento - 2006 #Aqui irá calcular quantos anos faltam para ele se alistar
atraso = 2006 - nascimento #Essa variável terá a função de mostrar a quantos anos ele não se alistou no exécito.

ano_do_alistamento = 2024 + alistamento_exato
atraso_no_alistamento = 2024 - atraso

if nascimento > 2006:
    print('Quem nasceu em {} tem {} anos em 2024.\nAinda faltam {} anos para o alistamento\nSeu alistamento será em {}.'.format(nascimento, idade_atual, alistamento_exato, ano_do_alistamento))
elif nascimento == 2006:
    print('Você está na idade correta para o alistamento!')
else:
    if nascimento <= 2006:
        print('Quem nasceu em {} tem {} anos em 2024.\nVocê já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(nascimento, idade_atual, atraso, atraso_no_alistamento))