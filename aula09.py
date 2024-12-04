frase = "Seja bem vindo"
print(frase.split())

str1 = "Olá"
str2 = "Mundo"
resultado = str1 + " " + str2  # "Olá Mundo"

str = "Olá Mundo"
sub_str = str[0:3]  # "Olá"

str = "Olá Mundo"
novo_str = str.replace("Mundo", "Python")  # "Olá Python"

str = "Olá Mundo Python"
lista = str.split(" ")  # ['Olá', 'Mundo', 'Python']

lista = ['Olá', 'Mundo', 'Python']
str = " ".join(lista)  # "Olá Mundo Python"

str = "Olá Mundo"
maiuscula = str.upper()  # "OLÁ MUNDO"
minuscula = str.lower()  # "olá mundo"
titulo = str.title()  # "Olá Mundo"

str = "  Olá Mundo  "
sem_espacos = str.strip()  # "Olá Mundo"

nome = "Mundo"
str = f"Olá {nome}"  # "Olá Mundo"

str = "Olá {}".format(nome)  # "Olá Mundo"

str = "Olá Mundo"
tamanho = len(str)  # 9