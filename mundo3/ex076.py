nome_loja = "LISTAGEM DE PREÇO"
print("-"*60)
print(nome_loja.center(60))
print("-"*60)
lista_preco = (
    "Lapis", 1.75,
    "Borracha", 2.00,
    "Caderno", 15.90,
    "Estojo", 25.90,
    "Transferidor", 4.90,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canetas", 22.30,
    "Livro", 34.90
)
for pos in range(0, len(lista_preco)):
    if pos % 2 == 0:
        print(f"{lista_preco[pos]:.<30}", end="")
    else:
        print(f"R${lista_preco[pos]:>1.2f}")