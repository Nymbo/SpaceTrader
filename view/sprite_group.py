from .sprite import *

class SpriteGroup(Sprite):

    def __init__(self):
        Sprite.__init__(self, None)
        self.children = []


    def setPosition(self, position):
        old_pos = self.getPosition()
        delta = position - old_pos
        for child in self.children:
            child_old_pos = child.getPosition()
            child_new_pos = child_old_pos + delta
            child.setPosition(child_new_pos)
        Sprite.setPosition(self, position)


    def addSprite(self, sprite):
        self.children.append(sprite)

    def draw(self):
        for child in self.children:
            child.draw()

    def update(self, clock):
        for child in self.children:
            child.update(clock)