from mathutils import *
import globvars
import pygame
import assets
import random

class Sprite:

    def __init__(self, image):
        self.image = image
        self.position = Vector2()


    def update(self, clock):
        pass

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position
    
    def draw(self):
        loc = globvars.viewport.project(self.position)
        loc.x = loc.x - self.image.get_width() / 2.0
        loc.y = loc.y - self.image.get_height() / 2.0
        
        globvars.surface.blit(self.image, (loc.x, loc.y))



class AnimatedSprite(Sprite):
    def __init__(self, tick, images):
        Sprite.__init__(self, images[0])
        self.tick = tick
        self.images = images
        self.frame = 0
        self.time = 0

    def update(self, clock):
        self.time += 1
        if self.time % self.tick == 0:
            self.frame += 1
            if self.frame >= len(self.images):
                self.frame = 0
        self.image = self.images[self.frame]

class Sky(Sprite):

    def __init__(self):
        Sprite.__init__(self, None)
        w = 1000
        h = 1000
        self.image = pygame.Surface((w, h))
        img = self.image

        for i in range(0,2000):
            x = random.randint(10,w - 10)
            y = random.randint(10,h - 10)
            r = random.randint(1,2)
            bright = random.randint(0,255)
            pygame.draw.rect(img, (bright, bright, bright), (x, y,r,r))

    def draw(self):
        globvars.surface.blit(self.image, (0, 0))

