from mathutils import *
import variables

class Scene:
    def __init__(self):
        self.sprites = []

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

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
