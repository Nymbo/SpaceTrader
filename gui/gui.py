import pygame
from pygame.locals import *
from pygame.mixer import *

import globvars
from mathutils import *


class Gui:
    def __init__(self):
        self.widgets = []
        self.hover_widget = None

    def addWidget(self, widget):
        if not widget in self.widgets:
            self.widgets.append(widget)

    def removeWidget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)

    def onEvent(self, event):
        if event.type == MOUSEMOTION:
            hover_widget = None
            for widget in self.widgets:
                if widget.containsCursor(event.pos[0], event.pos[1]):
                    hover_widget = widget
            if(hover_widget != self.hover_widget):
                if hover_widget != None:
                    hover_widget.onMouseOver()                    
                if self.hover_widget != None:
                    self.hover_widget.onMouseOut()
                self.hover_widget = hover_widget

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and self.hover_widget != None:
                self.hover_widget.onMouseDown()
                
        if event.type == MOUSEBUTTONUP :
            if event.button == 1 and self.hover_widget != None:
                self.hover_widget.onMouseUp()
            

    def update(self, clock):
        for widget in self.widgets:
            widget.update(clock)

    def draw(self):
        for widget in self.widgets:
            widget.draw()

class Widget:

    def __init__(self):
        self.name = None
        self.position = Vector2(0,0)
        self.size     = Vector2(0,0)
        self.listeners = []
        self.data = None  # User data to be used elsewhere.
        self.visible = True
        
    def draw(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addListener(self, listener):
        self.listeners.append(listener)

    def removeListener(self, listener):
        self.listeners.remove(listener)
    
    def setPosition(self, x, y):
        self.position.x = x
        self.position.y = y

    def setSize(self, w, h):
        self.size.x = w
        self.size.y = h

    def containsCursor(self, x, y):
        result_x = x >= self.position.x and x <= self.position.x + self.size.x
        result_y = y >= self.position.y and y <= self.position.y + self.size.y
        return result_x and result_y

    def onMouseOver(self):
        for listener in self.listeners:
            consumed = listener.onMouseOver(self)
            if consumed: return True
        return False

    def onMouseOut(self):
        
        for listener in self.listeners:
            consumed = listener.onMouseOut(self)
            if consumed: return True
        return False

    def onMouseDown(self):
        for listener in self.listeners:
            consumed = listener.onMouseDown(self)
            if consumed: return True
        return False

    def onMouseUp(self):
        for listener in self.listeners:
            consumed = listener.onMouseUp(self)
            if consumed: return True
        return False

    def update(self, clock):
        pass


class MouseListener:
    def onMouseOver(self, widget):
        pass

    def onMouseOut(self,widget):
        pass

    def onMouseDown(self, widget):
        pass

    def onMouseUp(self, widget):
        pass

class Text(Widget):

    def __init__(self, font, text=""):
        Widget.__init__(self)
        self.font = font
        self.txt_surf = None
        self.color = (255,255,255)
        self.setText(text)

    def setColor(self, color):
        self.color = color
        
    def setText(self, text):
        self.text = text
        self.surf = self.font.render(text, 1, self.color)
        self.size.x = self.surf.get_width()
        self.size.y = self.surf.get_height()

    def draw(self):
        if not self.visible: return
        globvars.surface.blit(self.surf, (self.position.x, self.position.y))


class Panel(Widget):
    def __init__(self):
        Widget.__init__(self)

    def draw(self):
        if not self.visible: return
        rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        pygame.draw.rect(globvars.surface, (0, 0, 0), rect)

        r, g, b = 70,70,70

        frame_top = pygame.Rect(self.position.x, self.position.y, self.size.x, 2)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_top)

        frame_bottom = pygame.Rect(self.position.x, self.position.y + self.size.y - 2, self.size.x, 2)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_bottom)

        frame_left = pygame.Rect(self.position.x, self.position.y, 2, self.size.y)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_left)

        frame_right = pygame.Rect(self.position.x + self.size.x - 2, self.position.y, 2, self.size.y)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_right)

        
class Button(Widget):

    def __init__(self, image):
        Widget.__init__(self)
        self.image = image
        self.size.x = image.get_width()
        self.size.y = image.get_height()
    
    def draw(self):
        if not self.visible: return
        globvars.surface.blit(self.image, (self.position.x, self.position.y))

        r, g, b = 70,70,70

        frame_top = pygame.Rect(self.position.x, self.position.y, self.size.x, 1)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_top)

        frame_bottom = pygame.Rect(self.position.x, self.position.y + self.size.y - 1, self.size.x, 1)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_bottom)

        frame_left = pygame.Rect(self.position.x, self.position.y, 1, self.size.y)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_left)

        frame_right = pygame.Rect(self.position.x + self.size.x - 1, self.position.y, 1, self.size.y)
        pygame.draw.rect(globvars.surface, (r, g, b), frame_right)

    def onMouseUp(self):
        Widget.onMouseUp(self)
        click = Sound("assets/sounds/click.ogg")
        click.play()

class CreditsGauge(Text):

    def __init__(self):
        Text.__init__(self, pygame.font.Font("assets/gui/LCD14.ttf", 15))

    def update(self, clock):
        self.setText("Credits: " + str(globvars.credits))


