import pygame, pytmx
            

#Tile class with an image, x and y
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, type = None):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
