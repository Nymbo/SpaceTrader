import assets

CARGO_1_NAME = "litium"     # Produced on Mercury
CARGO_2_NAME = "sulfur"     # Produced on Venus
CARGO_3_NAME = "carbon"     # Produced on Earth
CARGO_4_NAME = "silicon"    # Produced on Mars
CARGO_5_NAME = "hydrogen"   # Produced on Jupiter
CARGO_6_NAME = "helium"     # Produced on Saturn
CARGO_7_NAME = "water"      # Produced on Uranus
CARGO_8_NAME = "calcium"    # Produced on Neptune

class Cargo:
    def __init__(self, name, amount, price, capacity = 500):
        self.name   = name
        self.amount = amount
        self.price  = price
        self.capacity = capacity

        icon_path = "assets/cargos/" + name + ".png"
        self.icon = assets.loadImage(icon_path)

def createCargoArray():
    cargos = {}
    cargos[CARGO_1_NAME] = Cargo(CARGO_1_NAME, 0, 0)
    cargos[CARGO_2_NAME] = Cargo(CARGO_2_NAME, 0, 0)
    cargos[CARGO_3_NAME] = Cargo(CARGO_3_NAME, 0, 0)
    cargos[CARGO_4_NAME] = Cargo(CARGO_4_NAME, 0, 0)
    cargos[CARGO_5_NAME] = Cargo(CARGO_5_NAME, 0, 0)
    cargos[CARGO_6_NAME] = Cargo(CARGO_6_NAME, 0, 0)
    cargos[CARGO_7_NAME] = Cargo(CARGO_7_NAME, 0, 0)
    cargos[CARGO_8_NAME] = Cargo(CARGO_8_NAME, 0, 0)
    return cargos