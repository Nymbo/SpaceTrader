from pygame.mixer import Sound
from sprite import *

class Carrier(Sprite):

    def __init__(self):
        Sprite.__init__(self, None)
        self.setRotation(0)
        self.setSpeed(0)
        self.thrusters_sound = Sound("assets/sounds/thrusters.ogg")
        self.setAccelerating(False)
        self.setDecelerating(False)
        self.setRotatingLeft(False)
        self.setRotatingRight(False)


    def setRotation(self, rot):
        self.rotation = rot

        path = str(rot % 360)
        path = path.zfill(4)
        path = "assets/carrier/hull/" + path + ".png"
        
        self.image = assets.loadImage(path)

        thruster_path = str(self.rotation % 360)
        thruster_path = thruster_path.zfill(4)
        thruster_path = "assets/carrier/thrusters/" + thruster_path + ".png"
        thruster_image = assets.loadImage(thruster_path)

        self.rockets_image = thruster_image


    def draw(self):
        Sprite.draw(self)
        if self.accelerating:
            loc = globvars.viewport.project(self.position)
            loc.x = loc.x - self.image.get_width() / 2.0
            loc.y = loc.y - self.image.get_height() / 2.0
            globvars.surface.blit(self.rockets_image, (loc.x, loc.y))

    def getRotation(self):
        return self.rotation

    def setSpeed(self, speed):
        if speed >= 0:
            self.speed = speed
        else:
            self.speed = 0

    def getSpeed(self):
        return self.speed


    def setRockets(self, state):
        self.rockets_visible = state
        
    def setRotatingLeft(self, rotating):
        self.rotating_left = rotating

    def setRotatingRight(self, rotating):
        self.rotating_right = rotating

    def setAccelerating(self, acc):
        self.accelerating = acc
        if acc:
            self.thrusters_sound.play(-1)
        else:
            self.thrusters_sound.stop()

    def setDecelerating(self, dec):
        self.decelerating = dec
        if dec:
            self.thrusters_sound.play(-1)
        else:
            self.thrusters_sound.stop()

    def update(self, clock):
        if self.rotating_left:
            rot = self.getRotation()
            rot -= 1
            self.setRotation(rot)
        if self.rotating_right:
            rot = self.getRotation()
            rot += 1
            self.setRotation(rot)
        if self.accelerating:
            speed = self.getSpeed()
            speed += 0.2
            self.setSpeed(speed)
        if self.decelerating:
            speed = self.getSpeed()
            speed -= 0.2
            self.setSpeed(speed)



        rot = self.getRotation()
        fwd_vec = Vector2(0, -1)
        fwd_vec.rotate(rot)
        fwd_vec *= self.speed

        self.position += fwd_vec
