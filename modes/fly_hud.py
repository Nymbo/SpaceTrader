import pygame
from pygame.locals import *
import globvars
from main      import *


class FlyHud:

    def __init__(self):
        self.dock_guides = []


    def update(self):
        docks = globvars.docks
        self.dock_guides = []
        for dock in docks:
            dock_guide = DockGuide(dock)
            self.dock_guides.append(dock_guide)

        globvars.cargo_panel.update()


    def draw(self, nearby_dock):
        # Draw the navigation circle around the screen:
        pygame.draw.circle(globvars.surface, (200, 200, 200), (400, 400), 350, 2)

        for dock_guide in self.dock_guides:
            dock_guide.draw()

        font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
        if nearby_dock != None:
            txt = font.render("Press \"D\" to enter " + nearby_dock.name + " spacedock.", 1, (255, 255, 255))
            globvars.surface.blit(txt, (220, 0))

        asteroids = globvars.asteroids
        for ast in asteroids:
            to_vec = ast.position - globvars.player.position
            to_vec.normalize()
            to_vec *= 300
            guide_pos = Vector2(400, 400)
            guide_pos += to_vec

            # Draw the guide to a asteroid:
            pygame.draw.circle(globvars.surface, (255, 0, 0), (int(guide_pos.x), int(guide_pos.y)), 4)


    def onEvent(self, event):
        if event.type == MOUSEMOTION:
            globvars.cargo_panel.setDrawButtons(True)
            globvars.cargo_panel.hide()
            globvars.cargo_panel.setDock(None)

            x = event.pos[0]
            y = event.pos[1]
            mouse = Vector2(x, y)
            hover_guide = None
            for guide in self.dock_guides:
                guide_pos = guide.calcPosition()
                if mouse.distance(guide_pos) < 6:
                    hover_guide = guide
            if hover_guide != None:
                globvars.cargo_panel.setDock(hover_guide.dock)
                globvars.cargo_panel.setDrawButtons(False)
                globvars.cargo_panel.show()



# Dock guide is a mark within the navigation circle
# signifiying a space dock.
class DockGuide:
    def __init__(self, dock):
        self.dock = dock

    def draw(self):
        position = self.calcPosition()

        # Draw the guiding circle to a planet:
        pygame.draw.circle(globvars.surface, (255, 255, 255), (int(position.x), int(position.y)), 4)

        font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
        dist = int(globvars.player.position.distance(self.dock.position))
        txt = font.render(self.dock.name + " " + str(dist), 1, (255, 255, 255))

        # Draw the distance to a planet:
        globvars.surface.blit(txt, (position.x - 60, position.y))


    def calcPosition(self):
        to_vec = self.dock.position - globvars.player.position
        to_vec.normalize()
        to_vec *= 350
        center_pos = Vector2(400, 400)
        center_pos += to_vec
        guide_pos = center_pos
        return guide_pos