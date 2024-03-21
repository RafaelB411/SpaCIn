import pygame

GRAVITY = .1

class Falling(pygame.sprite.Sprite):
  
    def __init__(self, type, pos):
        super().__init__()
        ## mudam propulsores caindo ao serem desaclopados
        if type == 1:
            original_image = pygame.image.load("./sprites/Propellant/Propellant1.png")
        elif type == 2:
            original_image = pygame.image.load("./sprites/Propellant/Propellant2.png")
        elif type == 3:
            original_image = pygame.image.load("./sprites/Propellant/Propellant3.png")

        original_width, original_height = original_image.get_size()
        scaled_width = original_width // 2
        scaled_height = original_height // 2
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed_y = 0

    def falling(self, speed):
        self.speed_y += GRAVITY
        self.rect.y += speed
 
