resposta = 'Sim'
numero = 0
cont = 0
lista = []
while resposta == 'Sim':
        numero = int(input("Digite um número: "))
        resposta = input("Quer continuar? [Sim/Não] ").lower().capitalize()
        cont+=1
        lista.append(numero)
        if resposta == "Não":
            break
soma = sum(lista)
media = soma / len(lista)
print(f"Você digitou {cont} números e a média é de {round(media, 2)}")
print(f"O maior número foi o {max(lista)} e o menor foi {min(lista)}")
print("Seu Programa foi realizado com sucesso, Parabéns!!!")
