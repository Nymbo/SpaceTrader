from mathutils import *
import variables

class Scene:
    def __init__(self):
        self.sprites = []
        self.iterating = False
        self.marked_for_removal = []

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        if self.iterating:
            self.marked_for_removal.append(sprite)
        else:
            self.sprites.remove(sprite)

    def update(self):
        self.iterating = True
        for sprite in self.sprites:
            sprite.update()
        self.iterating = False

        for marked in self.marked_for_removal:
            self.sprites.remove(marked)

        del self.marked_for_removal[:]
            

class Viewport:

    def __init__(self, width, height):
        self.center = Vector2()
        self.width  = width
        self.height = height
    
    def project(self, vec2):
       
        result = vec2 - self.center

        result.x += self.width  / 2
        result.y += self.height / 2
            
        return result    


    def draw(self):
        for sprite in variables.scene.sprites:
            sprite.draw()
