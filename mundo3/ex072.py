import num2words
# import inflect
while True:
    tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    numeros = int(input("Digite um número entre 0 e 20: "))
    num_ptbr = num2words.num2words(numeros, lang='pt-br', to='cardinal') # Essa linha coverte um numero para string escrito por extenso.
    if numeros in tupla:
        print(f"Você digitou o número {num_ptbr}.")
        break
    else:
        print("O número digitado, não existe.")