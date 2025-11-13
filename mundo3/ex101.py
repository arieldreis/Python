import datetime
def votar(idade):
    if 18 <= idade < 70:
        print("Voto Obrigatório.")
    elif 16 >= idade < 18 or idade > 70:
        print("Voto facultativo.")
    else:
        print("Você ainda não pode votar.")

eleitor = int(input("Em que ano você nasceu? "))
calculo_idade = datetime.date.today().year - eleitor
votar(calculo_idade)