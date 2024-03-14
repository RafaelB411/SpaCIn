import math
import pygame
import random
import sys

from background import SIZE_WINDOW_X, WHITE, contagem_regressiva, draw, draw_fuel, draw_stars, menu, update_stars, setDisplay
from rocket import Rocket
from trash import LixoEspacial

FPS = 60

# Cria classe de desenhaveis da biblioteca
drawGroup = pygame.sprite.Group()

# Cria foguete e adiciona ao grupo 
rocket = Rocket(drawGroup)

# Cria lixo e adiciona ao grupo
trash_group = pygame.sprite.Group()

display = setDisplay()
pygame.display.set_caption("Rocket Launch")

#Clock para atualizacao de tela
clock = pygame.time.Clock()

#Flags de Controle
gameloop = True
gameStart = False
time_elapsed = 0

last_trash_time = 0  # Variável para rastrear o tempo desde a última geração de lixo espacial

#loop principal do jogo 
while gameloop:

    clock.tick(FPS)
    #time_elapsed = pygame.time.get_ticks() / 1000  # Tempo decorrido em segundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           gameloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gameStart:
                contagem_regressiva()
                gameStart = True
        elif not gameStart:
            menu()


    if gameStart:
        draw()
        update_stars()
        draw_stars(display)
        drawGroup.update()
        drawGroup.draw(display)
        time_elapsed += 1 / 60 
        draw_fuel(display, WHITE, SIZE_WINDOW_X - 200, 50, 180, 50, 18, time_elapsed)

        # Verificar se é hora de adicionar um novo lixo espacial
        current_time = pygame.time.get_ticks()
        if current_time - last_trash_time > 2000:  # Adicionar um novo lixo espacial a cada 2 segundos
            i = 0  # Contador para controlar a geração de lixo espacial
            while i < random.randint(1, 5):
                trash = LixoEspacial(drawGroup, trash_group)
                trash_group.add(trash)
                last_trash_time = current_time
                i += 1

        # Movimento dos lixos espaciais
        for trash in trash_group:
            trash.move_down(3, time_elapsed)

        # Verificar colisão entre o foguete e o lixo espacial
        if pygame.sprite.spritecollide(rocket, trash_group, False):
            gameloop = False  # Encerra o jogo se houver colisão

        trash_group.update()
        trash_group.draw(display)

        pygame.display.update()