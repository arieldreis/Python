print('====Lojas Marinho====')
valor_compra = float(input('Preço das Compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
decisao = int(input('Qual é a opção? '))
if decisao == 1:
    cash = valor_compra - (valor_compra * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor_compra , cash))
elif decisao == 2:
    vista_cartao = valor_compra - (valor_compra * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor_compra , vista_cartao))
elif decisao == 3:
    parcela_cartao = valor_compra
    print('Sua compra de R${:.2f} não terá alteração nenhuma!'.format(parcela_cartao))
elif decisao == 4:
    total = valor_compra + (valor_compra * 0.2)
    totparcela = int(input('Quantas Parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada {}x de R${:.2f}'.format(totparcela , parcela))
    print('Sua compra R${:.2f} vai custar R${:.2f} no final'.format(valor_compra , total))
else:
    print('Valores inválidos, digite novamente!')