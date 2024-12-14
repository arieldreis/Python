frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    if inverso == junto:
        print('Temos um palíndromo!')
        break
    else:
        print('A frase digitada não é um palíndromo!')
        break