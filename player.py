import pygame
from pygame import *

#player class
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.img = pygame.image.load("assets/player.png")
        self.rect = self.img.get_rect()
        self.rect.center = self.x, self.y
        self.left_pressed = False
        self.right_pressed = False
        
        
    
    def draw(self, win):
        win.blit(self.img, self.rect)
    
    def update(self):
        if self.left_pressed and not self.right_pressed:
            self.rect.move_ip(-13, 0)
        if self.right_pressed and not self.left_pressed:
            self.rect.move_ip(13, 0)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800

        

