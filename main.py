from modes.dock_mode import *
from modes.fly_mode import *
from modes.shipyard_mode import *
from gui.cargo_panel import *
from gui.gui import *
from gui.messenger import *
from gui.shipyard_menu import *
from view.screen import *
from carrier import *
from view.sky import *
from planets import *
from shipyard import *
from clock import *

def main():
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("Space Trader")

    globvars.surface    = pygame.display.set_mode((800, 800))
    pygame.display.set_icon(assets.loadImage("assets/icon.png"))
    globvars.gui        = Gui()
    globvars.scene      = Scene()
    globvars.viewport   = Viewport(800, 800);

    start_ship = SmallCarrier()
    start_ship.setPosition(Vector2(-3001, -3001))
    globvars.player     = start_ship
    globvars.spaceships.append(start_ship)

    globvars.shipyard = Shipyard()

    globvars.cargos = createCargoArray()

    sky = Sky()
    globvars.scene.addSprite(sky)
    createPlanetsWithDocks()
    createAsteroids()
    globvars.scene.addSprite(globvars.shipyard)
    globvars.scene.addSprite(globvars.player)

    globvars.fly_mode   = FlyMode()
    globvars.dock_mode  = DockMode()
    globvars.shipyard_mode = ShipyardMode()
    globvars.mode = globvars.fly_mode
    globvars.mode.enable()

    credits_gauge       = CreditsGauge()
    credits_gauge.setPosition(20, 770)
    globvars.gui.addWidget(credits_gauge)
    globvars.shipyard_menu = ShipyardMenu()
    globvars.cargo_panel = CargoPanel()
    globvars.messenger = Messenger()
    for dock in globvars.docks:
        dock.addListener(globvars.messenger)
    globvars.gui.addWidget(globvars.messenger)

    # Game loop:
    game_clock = Clock()
    pygame_clock = pygame.time.Clock()
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
        game_clock.update(pygame_clock)
        globvars.gui.update(game_clock)
        globvars.scene.update(game_clock)
        globvars.mode.update()

        # Draw:
        globvars.viewport.draw()
        globvars.mode.draw()
        globvars.gui.draw()

        # Delay and flip:
        pygame_clock.tick(60)
        pygame.display.update()




     
if __name__ == "__main__":
    main()
