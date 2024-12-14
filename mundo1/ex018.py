import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
coceno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O Ângulo de {}° tem o seno de {:.2f}".format(angulo, seno))
print(f"O Ângulo de {angulo}° tem o cosseno de {round(coceno,2)}")
print(f"O Ângulo de {angulo}° tem a tanjente de {round(tangente,2)}")