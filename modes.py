from pygame.locals import *
import variables
import pygame
from mathutils import *
from main      import *

class Mode:

    def enable(self):
        pass

    def disable(self):
        pass

    def update(self):
        pass

    def onEvent(self, event):
        pass

    def draw(self):
        pass


class ViewMode(Mode):

    def __init__(self):
        self.nearby_dock = None

    def enable(self):
        print "ViewMode enabled"    

    def onEvent(self, event):
        print event


class FlyMode(Mode):

    def __init__(self):
        self.panel = Panel()
        self.panel.setPosition(100,100)
        self.panel.setSize(600, 600)

    def onEvent(self, event):

        player = variables.player

        print event
        
        if event.type == KEYDOWN:
            print event
            
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
                    variables.player.setSpeed(0)
                    variables.player.rotating_left  = False
                    variables.player.rotating_right = False
                    variables.dock = self.nearby_dock
                    setMode(variables.dock_mode)
            if event.key == 9:
                self.displayCargo()
                
        if event.type == KEYUP:
            if event.key == 275:
                player.setRotatingLeft(False)
            if event.key == 276:
                player.setRotatingRight(False)
            if event.key == 273:
                player.setAccelerating(False)
            if event.key == 274:
                player.setDecelerating(False)

            if event.key == 9:
                self.hideCargo()


    def displayCargo(self):
        gui = variables.gui
        
        gui.addWidget(self.panel)

        self.cargos = {}

        font = pygame.font.Font("assets/LCD14.ttf",25)

        buy_icon  = assets.loadImage("assets/buy.png")
        sell_icon = assets.loadImage("assets/sell.png")

        x = 210
        y = 200

        l1 = 150     # buy button
        l2 = l1 + 40 # sell button
        l3 = l2 + 40 # price
        l4 = l3 + 60 # amount available
        l5 = l4 + 70 # amount has

        dy = 50
        
        for cargo_name, cargo_obj in variables.cargo.iteritems():
            self.cargos[cargo_name] = {}
            
            caption = Text(font)
            self.cargos[cargo_name]['caption'] = caption
            caption.setText(cargo_name)
            caption.setPosition(x, y)
        
            has_amount_txt = Text(font)
            self.cargos[cargo_name]["has_amount_txt"] = has_amount_txt
            has_amount_txt.setText(str(cargo_obj.amount))
            has_amount_txt.setPosition(x + l5, y)

            y += dy
        
        for cargo_name, cargo_obj in variables.cargo.iteritems():
            gui.addWidget(self.cargos[cargo_name]["caption"])
            gui.addWidget(self.cargos[cargo_name]["has_amount_txt"])

    def hideCargo(self):

        gui = variables.gui

        gui.removeWidget(self.panel)
        
        for cargo_name, cargo_obj in variables.cargo.iteritems():
            
            gui.removeWidget(self.cargos[cargo_name]["caption"])
            gui.removeWidget(self.cargos[cargo_name]["has_amount_txt"])
            
    def update(self):
        variables.viewport.center.x = variables.player.position.x
        variables.viewport.center.y = variables.player.position.y

        self.nearby_dock = None
        for dock in variables.docks:
            if dock.position.distance(variables.player.position) < 10:
                self.nearby_dock = dock
                break

    def draw(self):
        #Draw the navigation circle around the screen:
        pygame.draw.circle(variables.surface, (200,200,200), (400,400), 350, 2)
        docks = variables.docks

        font = pygame.font.Font("assets/LCD14.ttf", 15)
        
        for dock in docks:
            to_vec = dock.position - variables.player.position
            to_vec.normalize()
            to_vec *= 350
            center_pos = Vector2(400, 400)
            center_pos += to_vec
            guide_pos = center_pos

            #Draw the guide to a planet:
            pygame.draw.circle(variables.surface, (255,255,255), (int(guide_pos.x),int(guide_pos.y)), 4)

            dist = int( variables.player.position.distance(dock.position))
            txt = font.render(dock.name + " " + str(dist), 1, (255,255,255))

            #Draw the distance to a planet:
            variables.surface.blit(txt, (guide_pos.x - 60, guide_pos.y))
            
        if self.nearby_dock != None:
            txt = font.render("Press \"D\" to enter " + self.nearby_dock.name + " spacedock.", 1, (255,255,255))
            variables.surface.blit(txt, (400, 770))

        asteroids = variables.asteroids
        for ast in asteroids:
            to_vec = ast.position - variables.player.position
            to_vec.normalize()
            to_vec *= 300
            center_pos = Vector2(400, 400)
            center_pos += to_vec
            guide_pos = center_pos

            #Draw the guide to a asteroid:
            pygame.draw.circle(variables.surface, (255,0,0), (int(guide_pos.x),int(guide_pos.y)), 4)

            
class DockMode(Mode, MouseListener):

    def __init__(self):
        self.panel = Panel()
        self.panel.setPosition(100,100)
        self.panel.setSize(600, 600)


        
        
    def enable(self):
        gui = variables.gui
        dock = variables.dock
        
        gui.addWidget(self.panel)

        self.cargos = {}

        font = pygame.font.Font("assets/LCD14.ttf",25)

        buy_icon  = assets.loadImage("assets/buy.png")
        sell_icon = assets.loadImage("assets/sell.png")

        x = 210
        y = 200

        l1 = 150     # buy button
        l2 = l1 + 40 # sell button
        l3 = l2 + 40 # price
        l4 = l3 + 60 # amount available
        l5 = l4 + 70 # amount has

        dy = 50
        
        for cargo_name, cargo_obj in dock.cargo.iteritems():
            self.cargos[cargo_name] = {}
            
            caption = Text(font)
            self.cargos[cargo_name]['caption'] = caption
            caption.setText(cargo_name)
            caption.setPosition(x, y)
        
            buy_button = Button(buy_icon)
            self.cargos[cargo_name]["buy_button"] = buy_button
            buy_button.setPosition(x + l1, y)

            sell_button = Button(sell_icon)
            self.cargos[cargo_name]["sell_button"] = sell_button
            sell_button.setPosition(x + l2,y)

            price_txt = Text(font)
            self.cargos[cargo_name]["price_txt"] = price_txt
            price_txt.setText("0")
            price_txt.setPosition(x + l3, y)

            av_amount_txt = Text(font)
            self.cargos[cargo_name]["av_amount_txt"] = av_amount_txt
            av_amount_txt.setText("0")
            av_amount_txt.setPosition(x + l4, y)

            has_amount_txt = Text(font)
            self.cargos[cargo_name]["has_amount_txt"] = has_amount_txt
            has_amount_txt.setText("0")
            has_amount_txt.setPosition(x + l5, y)

            y += dy

        for cargo_name, cargo_obj in dock.cargo.iteritems():
            
            gui.addWidget(self.cargos[cargo_name]["caption"])
            gui.addWidget(self.cargos[cargo_name]["buy_button"])
            self.cargos[cargo_name]["buy_button"].addListener(self)
            gui.addWidget(self.cargos[cargo_name]["sell_button"])
            self.cargos[cargo_name]["sell_button"].addListener(self)
            gui.addWidget(self.cargos[cargo_name]["price_txt"])
            self.cargos[cargo_name]["price_txt"].setText(str(dock.getCargoPrice("carbon")))
            gui.addWidget(self.cargos[cargo_name]["av_amount_txt"])
            gui.addWidget(self.cargos[cargo_name]["has_amount_txt"])
        
    def disable(self):
        gui = variables.gui
        gui.removeWidget(self.panel)

        dock = variables.dock

        for cargo_name, cargo_obj in dock.cargo.iteritems():
            
            gui.removeWidget(self.cargos[cargo_name]["caption"])
            gui.removeWidget(self.cargos[cargo_name]["buy_button"])
            self.cargos[cargo_name]["buy_button"].removeListener(self)
            gui.removeWidget(self.cargos[cargo_name]["sell_button"])
            self.cargos[cargo_name]["sell_button"].removeListener(self)
            gui.removeWidget(self.cargos[cargo_name]["price_txt"])
            gui.removeWidget(self.cargos[cargo_name]["av_amount_txt"])
            gui.removeWidget(self.cargos[cargo_name]["has_amount_txt"])


    def onEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == 100:
                setMode(variables.fly_mode)


    def onMouseDown(self, widget):

        dock = variables.dock

        is_buy_button  = False
        is_sell_button = False
        cargo_name = None
        for cargo_name_i, cargo in dock.cargo.iteritems():
            target_button_buy  = self.cargos[cargo_name_i]["buy_button"]
            target_button_sell = self.cargos[cargo_name_i]["sell_button"]
            if target_button_buy == widget:
                cargo_name = cargo_name_i
                is_buy_button = True
                break
            if target_button_sell == widget:
                cargo_name = cargo_name_i
                is_sell_button = True
                break

        if cargo_name == None: return False

        dock_cargo = dock.cargo[cargo_name]

        if is_buy_button:
            cost = 50 * dock_cargo.price
            if variables.credits >= cost:
                if dock_cargo.amount >= 50:
                    variables.credits -= cost
                    dock_cargo.amount -= 50
                    variables.cargo[cargo_name].amount += 50
            return True

        if is_sell_button:
            if dock_cargo.amount <=450:
                if variables.cargo[cargo_name].amount >= 50:
                    cost = 50 * dock_cargo.price
                    variables.credits += cost
                    dock_cargo.amount += 50
                    variables.cargo[cargo_name].amount -= 50
                
            return True


    def update(self):

        dock = variables.dock
        
        for cargo_name, cargo in dock.cargo.iteritems():
            self.cargos[cargo_name]["av_amount_txt"].setText(str(dock.cargo[cargo_name].amount))
            self.cargos[cargo_name]["has_amount_txt"].setText(str(variables.cargo[cargo_name].amount))
            self.cargos[cargo_name]["price_txt"].setText(str(dock.cargo[cargo_name].price))
            
    def draw(self):
        font = pygame.font.Font("assets/LCD14.ttf", 15)
        txt = font.render("Press \"D\" again to leave this spacedock.", 1, (255,255,255))
        variables.surface.blit(txt, (400, 770))

    
