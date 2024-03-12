import pygame
import random

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.points = []  # Lista para armazenar os pontos
        self.generate_points()  # Gera os pontos inicialmente

    def generate_points(self):
        # Gera pontos aleatórios na parte superior da tela
        for _ in range(200):  # Você pode ajustar a quantidade de pontos conforme necessário
            x = random.randint(0, 840)  # Posição aleatória no eixo X
            y = random.randint(0, 100)  # Posição aleatória no eixo Y
            speed = random.randint(1, 5)  # Velocidade aleatória
            self.points.append([x, y, speed])

    def update(self, *args):
        # Atualiza a posição dos pontos
        for point in self.points:
            point[1] += point[2]  # Incrementa a posição Y pelo valor da velocidade
            if point[1] > 480:  # Se o ponto passar da parte inferior da tela
                # Reseta sua posição para cima, na parte superior da tela
                point[1] = random.randint(0, 100)
                point[0] = random.randint(0, 840)
