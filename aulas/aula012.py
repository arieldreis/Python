'''nome = str(input('Qual é o seu nome:'))
if nome == 'Ariel':
    print('Que nome bonito {}'.format(nome))
    print('Tenha um otimo dia {}'.format(nome))
elif nome == 'Gustavo' or nome == 'Maria' or nome == 'Kevin':
    print('Seu nome é bem popular no brasil!')
elif nome in 'Malcon Osvaldo Carol':
    print('Seu nome é estranho')
else:
    print('Seu nome é bem comum!')'''
'''comando = int(input("Digite um número: "))
match comando % 2:
    case 0:
        print(f"O número {comando} é par")
    case 1:
        print(f"O número {comando} é impar")'''

'''vendas = float(input("Qual foi o valor das vendas esse mês: "))
match vendas:
    case vendas if vendas >=2000:
        bonus = 0.13 * vendas
        print(f"O bonus que você ganhará esse mês será de {bonus}")
    case vendas if vendas >= 1300:
        bonus = 0.1 * vendas
        print(f"O bonus que você ganhará esse mês será de {bonus}")
    case vendas if vendas < 1300:
        bonus = 0
        print(f"O bonus que você ganhará esse mês será de {bonus}")'''

lista_produto = ["iphone" , "macbook", "appleWatch", "airpods", "tagApple"]
produto_procurado = input("Qual produto você deseja procurar: ").lower()
match produto_procurado:
    case produto_procurado if produto_procurado in lista_produto:
        print("Produto no estoque.")
    case _:
        print("Produto não Encontrado.")