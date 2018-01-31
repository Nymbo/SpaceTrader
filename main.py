import pygame
from   pygame.locals import *
import assets
import variables
from screen    import *
from modes     import *
from sprite    import *
from dock      import *
from mathutils import *
from dock      import *
from carrier   import *
from gui       import *

def main():
    pygame.init()

    width  = 800
    height = 800

    variables.surface = pygame.display.set_mode((width, height))

    variables.gui = Gui()
    frame = Panel()
    frame.setPosition(100,100)
    frame.setSize(100,100)
    #variables.gui.addWidget(frame)

    btn = Button(assets.loadImage("assets/asteroid.png"))
    #variables.gui.addWidget(btn)

    credits_gauge = CreditsGauge()
    credits_gauge.setPosition(20, 770)
    variables.gui.addWidget(credits_gauge)
    
    variables.scene = Scene()
    
    variables.viewport = Viewport(width, height);

    clock = pygame.time.Clock()

    variables.fly_mode = FlyMode()
    variables.mode = variables.fly_mode
    variables.mode.enable()

    variables.dock_mode = DockMode()

    bg = pygame.Surface(variables.surface.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))

    sky = Sky()
    variables.scene.addSprite(sky)

    createDocks()

    initCargo()
    
    variables.scene.addSprite(Sprite(assets.loadImage("assets/dock.png")))

    variables.player = PlayerCarrier()
    variables.player.setPosition(Vector2(-3001,-3001))
    variables.scene.addSprite(variables.player)

    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                done = True
            else:
                consumed = variables.gui.onEvent(event)
                if not consumed:
                    variables.mode.onEvent(event)

        variables.gui.update()
        variables.scene.update()
        variables.mode.update()

        variables.surface.blit(bg, (0,0))
        variables.viewport.draw()
        variables.mode.draw()

        variables.gui.draw()
        
        clock.tick(60)
        
        pygame.display.update()



def initCargo():
    variables.cargo["carbon"]   = Cargo(0, 0)
    variables.cargo["selenium"] = Cargo(0, 0)
    variables.cargo["uranium"]  = Cargo(0, 0)
    variables.cargo["nitrogen"] = Cargo(0, 0)
    variables.cargo["oxygen"]   = Cargo(0, 0)
    variables.cargo["hydrogen"] = Cargo(0, 0)
    variables.cargo["titanium"] = Cargo(0, 0)

def setMode(new_mode):
    variables.mode.disable()
    new_mode.enable()
    variables.mode = new_mode


     
if __name__ == "__main__":
    main()
