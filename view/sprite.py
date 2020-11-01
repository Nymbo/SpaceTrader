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






