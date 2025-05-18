import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake")
largura = 1000
altura = 600
tela = pygame.display.set_mode((largura, altura))
relogio =  pygame.time.Clock()
# cores
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
# Parametros da cobrinha
tamanha_quadrado = 10
velocidade_cobrinha = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanha_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanha_quadrado) / 20.0) * 20.0
    return comida_x, comida_y
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[1], tamanho, tamanho])
def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()
    while not fim_jogo:
        tela.fill(preto)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
        # desenhar comida
        desenhar_comida(tamanha_quadrado, comida_x, comida_y)
        # desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanha_quadrado, pixels)
        # desenhar pontos
        # atualização de tela
        pygame.display.update()
        relogio.tick(velocidade_cobrinha)
# Criar um loop infinito
# Desenhar os objetos do jogo na tela
# pontuação
# cobrinha
# comida
# criar a lógica de terminar o jogo
# o que acontece
# cobra bateu na parede
rodar_jogo()