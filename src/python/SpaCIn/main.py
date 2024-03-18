import math
import pygame
import random
import sys

from background import SIZE_WINDOW_X, WHITE, MIDNIGHT_BLUE , FONTE_DEFAULT, contagem_regressiva, draw, draw_fuel, draw_score, draw_stars, menu, update_stars, setDisplay
from rocket import Rocket
from trash import LixoEspacial
from gameOver import GameOver
from rocket_falling import Falling
 
def main():
    FPS = 60

    drawGroup = pygame.sprite.Group()
    rocket = Rocket(drawGroup)
    trash_group = pygame.sprite.Group()
    display = setDisplay()
    pygame.display.set_caption("Rocket Launch")
    clock = pygame.time.Clock()
    falling = None ## inicia escondido

    gameloop = True
    gameStart = False
    gameOver = False
    game_win = False
    time_elapsed = 0
    fator_pontuacao = 0.1
    notPressBotom = True    
    cache_level = 0
    last_trash_time = 0  # Variável para rastrear o tempo desde a última geração de lixo espacial

    #loop principal do jogo 
    while gameloop:
        clock.tick(FPS)
        #time_elapsed = pygame.time.get_ticks() / 1000  # Tempo decorrido em segundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT: ## se está no jogo e aperta em sair
                gameloop = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameStart: # se não está no jogo e pressiona space
                    contagem_regressiva()
                    gameStart = True
            elif not gameStart: # Se não tem nada jogando e nenhum QUIT. Então mostra Menu
                menu()


        if gameStart:
            draw()
           
            rckt =  rocket.level
            if cache_level != rckt[0]:
                falling = Falling( rckt[0], [rckt[1],rckt[2]])
                cache_level = rocket.level[0]

            if falling:
                falling.falling(1)
                display.blit(falling.image, falling.rect) 

            update_stars()
            draw_stars(display)
            drawGroup.update()
            drawGroup.draw(display)
            time_elapsed += 1 / 60 
            pontuacao = time_elapsed * (fator_pontuacao + time_elapsed / 100)
            draw_fuel(display, WHITE, SIZE_WINDOW_X - 200, 50, 180, 50, 18, time_elapsed)
            draw_score(display, pontuacao, SIZE_WINDOW_X - 200 + 90, 120)

            # Verificar se é hora de adicionar um novo lixo espacial
            current_time = pygame.time.get_ticks() / 1000
            if current_time - last_trash_time > 3:  # Adicionar um novo lixo espacial a cada 2 segundos
                i = 0  # Contador para controlar a geração de lixo espacial
                while i < random.randint(1, 6):
                    trash = LixoEspacial(drawGroup, trash_group)
                    trash_group.add(trash)
                    last_trash_time = current_time
                    i += 1

            # Movimento dos lixos espaciais
            for trash in trash_group:
                trash.move_down(3, time_elapsed)

            # Verificar colisão entre o foguete e o lixo espacial
            if pygame.sprite.spritecollide(rocket, trash_group, False) or rocket.status:
                gameStart = False  # Encerra o jogo se houver colisão
                gameOver = True
            
            if rocket.end:
                game_win = True


            trash_group.update()
            trash_group.draw(display)

            pygame.display.update()

        if gameOver:
            ## chama tela de game over e espera retorno do press buttom
            background = GameOver(display, FONTE_DEFAULT,  MIDNIGHT_BLUE, "Game Over")
          
            while notPressBotom:
                notPressBotom = background.getReturnButton()
                pygame.display.update() 
            
        if game_win:
            ## chama tela de game over e espera retorno do press buttom
            background = GameOver(display, FONTE_DEFAULT,  MIDNIGHT_BLUE, "END! You won.")
          
            while notPressBotom:
                notPressBotom = background.getReturnButton()
                pygame.display.update() 

        if not notPressBotom:
            main()

if __name__ == "__main__": 
    main()
