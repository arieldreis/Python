metros = float(input('Uma distância em metros: '))
kilometro = metros / 1000
hectometro = metros / 100
decametro = metros / 10
decimetro = metros * 10
centimetro = metros * 100
milimetro = metros * 1000
print('A medida de {} metros corresponde a...')
print('{}Km'.format(kilometro))
print('{}Hm'.format(hectometro))
print('{}Dam'.format(decametro))
print('{}dm'.format(decimetro))
print('{}cm'.format(centimetro))
print('{}mm'.format(milimetro))