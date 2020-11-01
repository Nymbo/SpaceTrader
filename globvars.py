surface   = None
gui       = None
scene     = None
viewport  = None

player     = None # The player Carrier instance
credits    = 10000
spaceships = []  # The list of ships owned by player

shipyard  = None
docks     = []
asteroids = []

cargos    = {}  # Cargos list used for iterations

mode            = None # The current mode the game is in.
fly_mode        = None
dock_mode       = None
shipyard_mode   = None

shipyard_menu = None
cargo_panel = None # The cargo panel displayed when player hit's TAB or docks onto station
messenger   = None # The messenger displaying information about certain events that occur.
