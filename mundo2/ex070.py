import time
loja = "\033[1;32mLOJA SUPER BARATÃO\033[m"
print("\033[1;32m-\033[m"*50)
print(loja.center(50))
print("\033[1;32m-\033[m"*50)
soma = menor = cont = 0
quantidade = 0
barato = ''
while True:
        nome_produto = str(input("\033[1;34mNome do Produto:\033[m "))
        preco = float(input("\033[1;34mPreço: R$\033[m"))
        confirmacao = str(input("\033[1;34mQuer continuar? [Sim/Não]:\033[m ")).lower().capitalize()
        cont+=1
        soma+=preco
        if confirmacao == "Sim":
            print("\033[1;31m-\033[m" * 30)
            print("\033[1;31mAGUARDE...\033[m")
            print("\033[1;31m-\033[m" * 30)
            time.sleep(2)
        if confirmacao == "Não":
            break
        if preco > 1000:
            quantidade+=1
        if cont == 1 or preco < menor:
            menor = preco
            barato = nome_produto
print("\033[1;32m--------------FIM DO PROGRAMA!!!--------------\033[m")
print("\033[1;32mAGUARDE...\033[m")
time.sleep(2)
print(f"O total da compra foi de R${soma:.2f}")
print(f"Temos {quantidade} produtos custando mais de 1000 reais.")
print(f"O produto mais barato foi um(a) {barato} que custa R${menor}")
