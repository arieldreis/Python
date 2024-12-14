dicio_produtos = {"airpod":2000 , "ipad":9000, "iphone":6000, "macbook":11000}
#Pegar um Elemento
'''print(dicio_produtos["iphone"])

#Editar um ‘item’ do dicionário
dicio_produtos["iphone"]= dicio_produtos["iphone"] * 1.3
print(dicio_produtos)

#Quantidade de Elementos da lista
print(len(dicio_produtos))

#Retirar um item da lista.
dicio_produtos.pop("airpod")
print(dicio_produtos)

#Adicionar um ‘item’ no dicionário
dicio_produtos["airtag"] = 2500
print(dicio_produtos)

#Vereificar se um item existe em uma lista
if "ipad" in dicio_produtos:
    print("O produto está no estoque")
else:
    print("O produto não está no estoque.")

#Verificar se um valor existe nos valores do dicionário
if 9000 in dicio_produtos.values():
    print("EXISTE")
else:
    print("NÃO EXISTE!")'''

#EXERCÍCIO
nome_produto = str(input("\033[1;35mNome do Produto:\033[m ")).lower()
preco_produto = float(input("\033[1;35mQual é o preço do produto:\033[m "))
if nome_produto in dicio_produtos:
    aumento =  preco_produto + (preco_produto * 0.1)
    print("O produto já está no estoque de vendas.")
    print(f"O seu produto sofreu um reajuste de 10%")
    dicio_produtos[nome_produto] = aumento
    print(dicio_produtos)
else:
    print("O produto foi adicionado ao estoque.")
    dicio_produtos[nome_produto] = preco_produto
    print(dicio_produtos)
for item in dicio_produtos:
    novo_preco = dicio_produtos[item] * 1.1
    dicio_produtos[item] = novo_preco
print(dicio_produtos)
# Cadastrar um novo ("Se o produto não existe").
# Caso o produto exista ele vai editar o produto.
# Além disso, programa tem que atualizar o preço de todos os produtos para os novos valores.
# E os novos produtos têm que ser 10% a mais do que os antigos.