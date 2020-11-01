from .sprite import *

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