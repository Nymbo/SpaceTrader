from mathutils import *
import variables
import pygame
import assets
import random

class Sprite:

    def __init__(self, image):
        self.image = image
        self.position = Vector2()


    def update(self):
        pass

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position
    
    def draw(self):
        loc = variables.viewport.project(self.position)
        loc.x = loc.x - self.image.get_width() / 2.0
        loc.y = loc.y - self.image.get_height() / 2.0
        
        variables.surface.blit(self.image, (loc.x,loc.y))



class AnimatedSprite(Sprite):
    def __init__(self, tick, images):
        self.tick = tick
        self.images = images
        self.frame = 0
        self.time = 0

    def update(self):
        
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
        variables.surface.blit(self.image, (0,0) )


class Asteroid(AnimatedSprite):
    def __init__(self):
        variation = random.randint(1,3)
        directory = "assets/asteroid" + str(variation)
        frames = assets.loadAnim(directory, 0, 99)
        AnimatedSprite.__init__(self, 4, frames)

        rand_x = random.randint(-100000, 100000)
        rand_y = random.randint(-100000, 100000)
        pos = Vector2(rand_x, rand_y)
        self.setPosition(pos)

        vec_x = random.randint(-4,4)
        vec_y = random.randint(-4,4)
        self.vector = Vector2(vec_x, vec_y)

        t = random.randint(120,180)
        self.timeout = t
        self.ticks = 0
        
    def update(self):
        AnimatedSprite.update(self)
        self.position = self.position + self.vector
        self.ticks += 1
        if self.ticks % 60 == 0:
            self.timeout -= 1

        if self.timeout == 0:
            variables.scene.removeSprite(self)
            variables.asteroids.remove(self)
            new_asteroid = Asteroid()
            variables.scene.addSprite(new_asteroid)
            varialbes.asteroids.append(new_asteroid)
            print "Respawning asteroid"
        
