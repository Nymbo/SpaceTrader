import pygame
import globvars
from .gui import Widget


class AnimatedIcon(Widget):

    def __init__(self, framerate, images):
        Widget.__init__(self)
        self.images = images
        self.image = images[0]
        self.size.x = self.image.get_width()
        self.size.y = self.image.get_height()
        self.duration = 1000 / framerate # Duration of a single frame in milliseconds.
        self.frame = 0
        self.frame_time = 0


    def update(self, clock):
        delta_time = clock.get_time()
        self.frame_time += delta_time
        if self.frame_time > self.duration:
            self.frame_time = 0
            framecount = len(self.images)
            self.frame += 1
            if self.frame >= framecount:
                self.frame = 0
            self.image = self.images[self.frame]


    def draw(self):
        globvars.surface.blit(self.image, (self.position.x, self.position.y))