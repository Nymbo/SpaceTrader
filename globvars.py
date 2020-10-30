surface   = None
gui       = None
scene     = None
viewport  = None

player    = None # The player Carrier instance
credits   = 50000
cargos    = {}  # Cargos being carried - dictionary: cargo name -> cargo

docks     = []
asteroids = []

mode      = None # The current mode the game is in.
fly_mode  = None
dock_mode = None

cargo_panel = None # The cargo panel displayed when player hit's TAB or docks onto station
messenger   = None # The messenger displaying information about certain events that occur.
