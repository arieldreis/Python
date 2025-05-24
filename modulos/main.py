from typing import Hashable

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
    comida_x = round(random.randrange(0, largura - tamanha_quadrado) / float(tamanha_quadrado)) * float(tamanha_quadrado)
    comida_y = round(random.randrange(0, altura - tamanha_quadrado) / float(tamanha_quadrado)) * float(tamanha_quadrado)
    return comida_x, comida_y
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1],tamanho, tamanho])
def desenha_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Arial", 30, bold=True, italic=False)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [4, 3])
def selecionar_velocidade(tecla):
    velocidade_x = 0
    velocidade_y = 0
    # Se o usuário apertar a tecla para baixo
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanha_quadrado
    # Se o usuário apertar a tecla para cima
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanha_quadrado
    # Se o usuário apertar a tecla para direita
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanha_quadrado
        velocidade_y = 0
    # Se o usuário apertar a tecla da esquerda
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanha_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y
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
            # Aqui ele reconhece ás teclas presionadas
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        # desenhar comida
        desenhar_comida(tamanha_quadrado, comida_x, comida_y)
        # Atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura: # Caso a cobrinha bata na parede
            fim_jogo = True
        x += velocidade_x
        y += velocidade_y
        # desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        # Se a cobrinha bateu no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanha_quadrado, pixels)
        # desenhar pontos
        desenha_pontuacao(tamanho_cobra - 1)
        # atualização de tela
        pygame.display.update()
        # Criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_cobrinha)
'''O QUE SERÁ FEITO NO JOGO SNAKE NOKIA'''
# Criar um loop infinito
# Desenhar os objetos do jogo na tela
# pontuação
# cobrinha
# comida
# criar a lógica de terminar o jogo
# o que acontece
# cobra bateu na parede
rodar_jogo()