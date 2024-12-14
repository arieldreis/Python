import time
primeiro_valor = int(input('Primeiro Valor: '))
segundo_valor = int(input('Segundo valor: '))
escolha = 0
while escolha != 6:
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do Programa')
    escolha = int(input('Qual é a sua escolha: '))
    if escolha == 1:
        s = primeiro_valor + segundo_valor
        print('A soma entre {} + {} = {}'.format(primeiro_valor , segundo_valor, s))
    elif escolha == 2:
        mult = primeiro_valor * segundo_valor
        print('A multiplicação entre {} x {} = {}'.format(primeiro_valor, segundo_valor , mult))
    elif escolha == 3:
        maior = max(primeiro_valor, segundo_valor)
        print('Analisando a sua solicitação o maior valor é {}'.format(maior))
    elif escolha == 4:
        primeiro_valor = int(input('Primeiro Valor: '))
        segundo_valor = int(input('Segundo valor: '))
        print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do Programa')
    elif escolha == 5:
        print('\033[0;45mAguarde...\033[m')
        time.sleep(3)
        break
    else:
        print('Opção inválida, digte novamente!')
print('Obrigado, pela preferência!')