from .sprite import  *

class AnimatedSprite(Sprite):
    def __init__(self, framerate, frames):
        Sprite.__init__(self, frames[0])
        self.frames = frames
        self.duration = 1000 / framerate # Duration of a single frame in milliseconds.
        self.frame = 0
        self.frame_time = 0

    def update(self, clock):
        delta_time = clock.get_time()
        self.frame_time += delta_time
        if self.frame_time > self.duration:
            self.frame_time = 0
            framecount = len(self.frames)
            self.frame += 1
            if self.frame >= framecount:
                self.frame = 0
            self.image = self.frames[self.frame]