frase = "Seja bem vindo"
print(frase.split())

str1 = "Olá"
str2 = "Mundo"
resultado = str1 + " " + str2  # "Olá Mundo"
print(resultado)

str = "Olá Mundo"
sub_str = str[0:3]  # "Olá"
print(sub_str)

str = "Olá Mundo"
novo_str = str.replace("Mundo", "Python")  # "Olá Python"
print(novo_str)

str = "Olá Mundo Python"
lista = str.split(" ")  # ['Olá', 'Mundo', 'Python']
print(lista)

lista1 = ['Olá', 'Mundo', 'Python']
str = " ".join(lista)  # "Olá Mundo Python"
print(str)

str1 = "Olá Mundo"
maiuscula = str.upper()  # "OLÁ MUNDO"
minuscula = str.lower()  # "olá mundo"
titulo = str.title()  # "Olá Mundo"
print(minuscula)
print(minuscula)
print(titulo)

str = "  Olá Mundo  "
sem_espacos = str.strip()  # "Olá Mundo"
print(sem_espacos)

nome = "Mundo"
str = f"Olá {nome}"  # "Olá Mundo"
print(str)

str = "Olá {}".format(nome)  # "Olá Mundo"

str = "Olá Mundo"
tamanho = len(str)  # 9
