from gui.Messenger import Messenger
from screen import *
from carrier import *
from modes.dock_mode import *
from modes.fly_mode import *
from gui.cargo_panel import *
from gui.gui import *

from planets import *

def main():
    pygame.init()
    pygame.mixer.init()

    globvars.surface    = pygame.display.set_mode((800, 800))
    globvars.gui        = Gui()
    globvars.scene      = Scene()
    globvars.viewport   = Viewport(800, 800);

    globvars.player     = Carrier()
    globvars.player.setPosition(Vector2(-3001, -3001))

    initCargo()

    sky = Sky()
    globvars.scene.addSprite(sky)
    createPlanetsWithDocks()
    createAsteroids()
    globvars.scene.addSprite(globvars.player)

    globvars.fly_mode   = FlyMode()
    globvars.dock_mode  = DockMode()
    globvars.mode = globvars.fly_mode
    globvars.mode.enable()

    credits_gauge       = CreditsGauge()
    credits_gauge.setPosition(20, 770)
    globvars.gui.addWidget(credits_gauge)

    globvars.cargo_panel = CargoPanel()
    globvars.messenger = Messenger()
    for dock in globvars.docks:
        dock.addListener(globvars.messenger)
    globvars.gui.addWidget(globvars.messenger)

    # Game loop:
    clock = pygame.time.Clock()
    done = False
    while not done:
        # Event dispatching:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            else:
                consumed = globvars.gui.onEvent(event)
                if not consumed:
                    globvars.mode.onEvent(event)

        # Update:
        globvars.gui.update(clock)
        globvars.scene.update(clock)
        globvars.mode.update()

        # Draw:
        globvars.viewport.draw()
        globvars.mode.draw()
        globvars.gui.draw()

        # Delay and flip:
        clock.tick(60)
        pygame.display.update()


def initCargo():
    globvars.cargos[CARGO_1_NAME] = Cargo(CARGO_1_NAME, 0, 0)
    globvars.cargos[CARGO_2_NAME] = Cargo(CARGO_2_NAME, 0, 0)
    globvars.cargos[CARGO_3_NAME] = Cargo(CARGO_3_NAME, 0, 0)
    globvars.cargos[CARGO_4_NAME] = Cargo(CARGO_5_NAME, 0, 0)
    globvars.cargos[CARGO_5_NAME] = Cargo(CARGO_4_NAME, 0, 0)
    globvars.cargos[CARGO_6_NAME] = Cargo(CARGO_6_NAME, 0, 0)
    globvars.cargos[CARGO_7_NAME] = Cargo(CARGO_7_NAME, 0, 0)
    globvars.cargos[CARGO_8_NAME] = Cargo(CARGO_8_NAME, 0, 0)



     
if __name__ == "__main__":
    main()
