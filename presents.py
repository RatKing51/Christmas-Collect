import pygame
from pygame import *
import random

class Present(pygame.sprite.Sprite):

    def __init__(self):
        self.x = random.randint(32, 568)
        self.y = 32
        self.img = pygame.image.load("assets/giftbox.png")
        self.rect = self.img.get_rect()
        self.rect.center = self.x, self.y
    
    def draw(self, win):
        win.blit(self.img, self.rect)

    def update(self):
        self.rect.move_ip(0, 15)
        if self.rect.top >= 600:
            self.rect.left = random.randint(32, 568)
            self.rect.top = 32
        
