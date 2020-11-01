from pygame.mixer import Sound
from modes.mode import *
from pygame.locals import *
import globvars
import pygame
from mathutils import *
from main      import *
from modes.fly_hud import *

class FlyMode(Mode):

    def __init__(self):
        self.fly_hud = FlyHud()
        self.tab_pressed = False

    def onEvent(self, event):
        player = globvars.player
        if event.type == KEYDOWN:
            if event.key == 275:
                player.setRotatingLeft(True)
            if event.key == 276:
                player.setRotatingRight(True)
            if event.key == 273:
                player.setAccelerating(True)
            if event.key == 274:
                player.setDecelerating(True)
            if event.key == 100:
                if self.nearby_dock != None:
                    globvars.player.setSpeed(0)
                    globvars.player.rotating_left = False
                    globvars.player.rotating_right = False
                    globvars.dock = self.nearby_dock
                    setMode(globvars.dock_mode)
            if event.key == 9:  # Tab key to view the carried cargos.
                self.tab_pressed = True
                self.displayCargo()
            if event.key == 13: # Enter for entering the shipyard.
                if self.nearby_shipyard != None:
                    setMode(globvars.shipyard_mode)

        elif event.type == KEYUP:
            if event.key == 275:
                player.setRotatingLeft(False)
            if event.key == 276:
                player.setRotatingRight(False)
            if event.key == 273:
                player.setAccelerating(False)
            if event.key == 274:
                player.setDecelerating(False)

            if event.key == 9:
                self.tab_pressed = False
                self.hideCargo()
        else:
            if not self.tab_pressed:
                self.fly_hud.onEvent(event)

    def displayCargo(self):
        globvars.cargo_panel.show()

    def hideCargo(self):
        globvars.cargo_panel.hide()

    def update(self):
        globvars.viewport.center.x = globvars.player.position.x
        globvars.viewport.center.y = globvars.player.position.y

        # Nearby dock contact detection:
        self.nearby_dock = None
        for dock in globvars.docks:
            if dock.position.distance(globvars.player.position) < 20:
                self.nearby_dock = dock
                break

        # Nearby shipyard contact detection:
        self.nearby_shipyard = None
        if globvars.shipyard.position.distance(globvars.player.position) < 20:
            self.nearby_shipyard = globvars.shipyard

        # Asteroid collision detection:
        for asteroid in globvars.asteroids:
            if asteroid.position.distance(globvars.player.position) < 50:
                collision_sound = Sound("assets/sounds/collision.ogg")
                collision_sound.play()
                globvars.player.setSpeed(2)

        if self.tab_pressed:
            globvars.cargo_panel.update()

        self.fly_hud.update()

    def draw(self):
        self.fly_hud.draw(self.nearby_dock, self.nearby_shipyard)
