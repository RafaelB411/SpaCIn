from typing import Any
import pygame

import os, sys
from fcntl import ioctl
from rocket_falling import Falling

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

BOTAO_ESQ = 0X7
BOTAO_DIR = 0xE
UPDATE_FOGAO = 0xB

EJETA_PROP_1 = 0xFFF
EJETA_PROP_2 = 0x3F
EJETA_PROP_3 = 0x0

NUM_SWITCH = 18
NUM_SWITCH_STATE_1 = 0
NUM_SWITCH_STATE_2 = 1
NUM_SWITCH_STATE_3 = 2

INITIAL_X = 370
INITIAL_Y = 150

SIZE_WINDOW_X = 1280

fd = os.open(sys.argv[1], os.O_RDWR)
all_leds_on = 0xFFFFF
ioctl(fd, WR_RED_LEDS)
leds = os.write(fd, all_leds_on.to_bytes(4, 'little'))

def led_fuel(num_led):
    global all_leds_on
    ioctl(fd, WR_RED_LEDS)
    
    num_led = 1 << num_led
    all_leds_on = all_leds_on ^ num_led
    leds = os.write(fd, all_leds_on.to_bytes(4, 'little'))
    

class Rocket(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        all_leds_on = 0xFFFFF
        ioctl(fd, WR_RED_LEDS)
        leds = os.write(fd, all_leds_on.to_bytes(4, 'little'))

        self.image = pygame.image.load("sprites/Rocket/Rocket_FULL.png")
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [width//2, height//2])
        #self.image = pygame.transform.scale(self.image, [50, 250])
        self.rect = pygame.Rect([INITIAL_X, INITIAL_Y, width//2, height//2])
        self.switchs = [True]*NUM_SWITCH
        self.state_foguete = 0
        self.status = False
        self.end = False
        self.level = [0,0,0]

    def set_foguete(self):
        self.check_switch()
        width = 0
        height = 0

        if self.state_foguete == 1:
            self.image = pygame.image.load("sprites/Rocket/Rocket1.png")
            width, height = self.image.get_size()
        elif self.state_foguete == 2:
            self.image = pygame.image.load("sprites/Rocket/Rocket2.png")
            width, height = self.image.get_size()               
        elif self.state_foguete == 3:
           self.image = pygame.image.load("sprites/Rocket/Rocket3.png")
           width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [width//2, height//2])
        self.rect.height = height//2
        self.rect.width = width // 2
        self.level = [self.state_foguete , self.rect.x, self.rect.y + height//2]
    
    def check_switch(self):

        primeira_ocorrencia_True = None
        #print(self.switchs)

        for i in range(len(self.switchs)):
            if self.switchs[i]:
                primeira_ocorrencia_True = i - 1
                break

        #print(primeira_ocorrencia_True)       
        if primeira_ocorrencia_True == NUM_SWITCH_STATE_1:
            self.state_foguete = 1          
        elif primeira_ocorrencia_True == NUM_SWITCH_STATE_2:
            self.state_foguete = 2         
        elif primeira_ocorrencia_True == NUM_SWITCH_STATE_3:
            self.state_foguete = 3          
        else:
            self.status = True    
            
    def update(self, *args):

        keys = pygame.key.get_pressed() #Array de Bool 

        # Movimento
        ioctl(fd, RD_PBUTTONS)
        press_botao = os.read(fd, 4);
        press_botao = int.from_bytes(press_botao, 'little')

        ioctl(fd, RD_SWITCHES)
        switch_value = os.read(fd, 4);
        switch_value = int.from_bytes(switch_value, 'little')

        if press_botao == BOTAO_ESQ: # move p/ esq. 
           self.rect.x -= 5
        elif press_botao == BOTAO_DIR: # move p/ dir. 
           self.rect.x += 5

        # limites de Tela 
        if self.rect.x < 0:
            self.rect.x = 0
        elif (self.rect.x + self.rect.width) > SIZE_WINDOW_X:
            self.rect.x = SIZE_WINDOW_X - self.rect.width

        # intera��o switch
        # somente para testes, na versao final deve usar o vetor vindo do driver
        if switch_value == EJETA_PROP_1:
            self.switchs[0] = False
        elif switch_value == EJETA_PROP_2:
            self.switchs[1] = False
        elif switch_value == EJETA_PROP_3 and press_botao == UPDATE_FOGAO:
            self.switchs[2] = False
            self.end = True

        if press_botao == UPDATE_FOGAO:
            self.set_foguete()
        
        
