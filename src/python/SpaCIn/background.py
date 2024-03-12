import pygame
import random

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.points = []  # Lista para armazenar os pontos
        self.generate_points()  # Gera os pontos inicialmente

    def generate_points(self):
        # Gera pontos aleat�rios na parte superior da tela
        for _ in range(200):  # Voc� pode ajustar a quantidade de pontos conforme necess�rio
            x = random.randint(0, 840)  # Posi��o aleat�ria no eixo X
            y = random.randint(0, 100)  # Posi��o aleat�ria no eixo Y
            speed = random.randint(1, 5)  # Velocidade aleat�ria
            self.points.append([x, y, speed])

    def update(self, *args):
        # Atualiza a posi��o dos pontos
        for point in self.points:
            point[1] += point[2]  # Incrementa a posi��o Y pelo valor da velocidade
            if point[1] > 480:  # Se o ponto passar da parte inferior da tela
                # Reseta sua posi��o para cima, na parte superior da tela
                point[1] = random.randint(0, 100)
                point[0] = random.randint(0, 840)
