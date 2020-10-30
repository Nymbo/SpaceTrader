from modes.mode import Mode
from pygame.locals import *
import globvars
import pygame
from mathutils import *
from main      import *


class DockMode(Mode, MouseListener):

    def __init__(self):
        self.panel = Panel()
        self.panel.setPosition(100,100)
        self.panel.setSize(600, 600)

    def enable(self):
        dock = globvars.dock
        globvars.cargo_panel.setDock(dock)
        globvars.cargo_panel.show()

    def disable(self):
        globvars.cargo_panel.setDock(None)
        globvars.cargo_panel.hide()
        pass


    def onEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == 100:
                setMode(globvars.fly_mode)

    def update(self):
        globvars.cargo_panel.update()

            
    def draw(self):
        font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
        txt = font.render("Press \"D\" again to leave this spacedock.", 1, (255,255,255))
        globvars.surface.blit(txt, (220, 0))

    
