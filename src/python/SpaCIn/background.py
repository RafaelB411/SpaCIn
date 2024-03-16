import math
import pygame
import random

from rocket import Rocket

# Definições
FONTE_DEFAULT = "Fonts/GamegirlClassic.ttf"
WHITE = (255, 255, 255)
MIDNIGHT_BLUE = (0, 0, 0)
NUM_STARS = 100
# Tela
SIZE_WINDOW_X = 840
SIZE_WINDOW_Y = 480

pygame.init()

# Definição das Fontes 
title_font = pygame.font.Font(FONTE_DEFAULT, 50)
fonte = pygame.font.Font(FONTE_DEFAULT, 25)
fonte_combustivel = pygame.font.Font(FONTE_DEFAULT, 15)

# Cria estrelas
stars = []

# Configuracoes iniciais da janela 
def setDisplay():
    return pygame.display.set_mode([SIZE_WINDOW_X, SIZE_WINDOW_Y])

display = setDisplay()

# Funcao que desenha as estrelas
def draw_stars(surface):
    for star in stars:
        pygame.draw.circle(surface, (255, 255, 255), (star[0], star[1]), 1)

# Funcao que atualiza posicao da estrela
def update_stars():
    for i in range(len(stars)):
        stars[i][1] += 3  # Movimento para baixo

        # Se a estrela sair da tela, reposicione-a no topo
        if stars[i][1] > SIZE_WINDOW_Y:
            stars[i][0] = random.randint(0, SIZE_WINDOW_X)
            stars[i][1] = random.randint(0, SIZE_WINDOW_Y)

# Cria estrelas iniciais
for _ in range(NUM_STARS):
    x = random.randint(0, SIZE_WINDOW_X)
    y = random.randint(0, SIZE_WINDOW_Y)
    stars.append([x, y])

def draw():
    display.fill(MIDNIGHT_BLUE)
    
# Funcao para desenhar um retangulo segmentado
def draw_fuel(surface, color, x, y, width, height, segments, time_elapsed):
    segment_width = width // segments
    for i in range(segments):
        if i < (time_elapsed // 10):
            pygame.draw.rect(surface, MIDNIGHT_BLUE, (x + i * segment_width, y, segment_width, height), 0)
        else:
            pygame.draw.rect(surface, color, (x + i * segment_width, y, segment_width, height), 0)
        pygame.draw.rect(surface, WHITE, (x + i * segment_width, y, segment_width, height), 1)  # Desenha linha de contorno

    # Desenha o texto "Combustivel" acima do retangulo
    texto_combustivel = fonte_combustivel.render("Combustivel", True, WHITE)
    texto_combustivel_retangulo = texto_combustivel.get_rect(center=(x + width // 2, y - 25))
    surface.blit(texto_combustivel, texto_combustivel_retangulo)

# Funcao que desenha o círculo
def draw_circle(angulo):
    draw()
    centro = (SIZE_WINDOW_X // 2, SIZE_WINDOW_Y // 2)
    raio = 50
    largura_linha = 3
    inicio_angulo = math.radians(0)
    fim_angulo = math.radians(angulo)
    pygame.draw.arc(display, WHITE, (centro[0] - raio, centro[1] - raio, raio * 2, raio * 2), inicio_angulo, fim_angulo, largura_linha)

#Funcao que desenha contagem Regressiva
def contagem_regressiva():
    for i in range(3, 0, -1):
        angulo = i * 36
        draw()
        draw_circle(angulo)
        texto = fonte.render(str(i), True, (255, 255, 255))
        texto_retangulo = texto.get_rect(center=(SIZE_WINDOW_X // 2, SIZE_WINDOW_Y // 2))
        display.blit(texto, texto_retangulo)
        pygame.display.flip()
        draw()
        pygame.time.wait(1000)  # Espera 1 segundo

# Função para desenhar a pontuação na tela
# Função para desenhar a pontuação na tela
def draw_score(surface, pontuacao, x, y):
    texto_pontuacao = fonte_combustivel.render(f'Pontuação: {pontuacao:.2f}', True, WHITE)
    texto_pontuacao_retangulo = texto_pontuacao.get_rect(center=(x, y))
    surface.blit(texto_pontuacao, texto_pontuacao_retangulo)



# Funcao que desenha o menu inicial 
def menu():
    draw()
    
    # desenha titulo do Jogo
    titulo = title_font.render("SpaCIN Ship ", True, (255, 255, 255))
    titulo_retangulo = titulo.get_rect(center=(SIZE_WINDOW_X // 2, 50))
    display.blit(titulo, titulo_retangulo)
    
    # desenha instrucao para comecar o jogo 
    texto = fonte.render("Pressione SPACE para Lancar", True, (255, 255, 255))
    texto_retangulo = texto.get_rect(center=(SIZE_WINDOW_X // 2, SIZE_WINDOW_Y // 2))
    display.blit(texto, texto_retangulo)
    draw_stars(display)
    pygame.display.flip()
    draw()
