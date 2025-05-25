'''
A função open(), após a declaração da variável que receberá a função, necessita de dois parâmetros: primeiramente o nome do arquivo e, depois, o modo como estamos abrindo esse arquivo.
Na sintaxe apresentada acima foi utilizado o ‘w’ para fazer a escrita em um arquivo.
Caso o arquivo não exista nesse modo, o código criará um arquivo com o nome escrito no primeiro parâmetro.
'''

arquivo = open('test.txt', 'w')

arquivo.write("Curso de Python.\n")
arquivo.write("Aula Prática\n")
arquivo.close()

# Leitura do arquivo texto
leitura = open('test.txt', 'r')
print(leitura.read())
leitura.close()