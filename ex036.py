valor_casa = float(input('Qual é o valor da casa que você irá comprar: '))
salario_comprador = float(input('Qual é o seu salário atualmente R$'))
anos = int(input('Em quantos anos você irá pagar essa casa: ')) #Lembrando que você tem que digitar em meses para se realizar o calculo

total_meses = anos * 12 #Aqui irá converter meses em anos

prestacao_mesal = valor_casa / total_meses

limitacao_prestcao = salario_comprador * 0.3
if salario_comprador <= prestacao_mesal:
    print('Para pegar uma casa no valor de R${} em {} anos a prestação mensal será de R${:.2f}'.format(valor_casa, anos, prestacao_mesal))
    print('O seu emprétimo foi aceito!')
else:
    print('Para pegar uma casa no valor de R${} em {} anos a prestação mensal ficará no valor de R${:.2f} '.format(valor_casa, anos, prestacao_mesal))
    print('Seu empréstimo foi negado!')