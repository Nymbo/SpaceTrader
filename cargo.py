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

        if name == CARGO_1_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_2_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_3_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_4_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_5_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_6_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_7_NAME: img_path = "assets/cargos/litium.png"
        if name == CARGO_8_NAME: img_path = "assets/cargos/litium.png"
        self.icon = assets.loadImage(img_path)



class CargoProducer:

    def __init__(self, cargo_name, rate):
        self.cargo_name = cargo_name
        self.rate = rate

    # Update the producer - return true if cargo was produced.
    def update(self):
        dock_cargo = self.dock.cargos[self.cargo_name]
        if dock_cargo.amount <= dock_cargo.capacity - self.rate:
            self.dock.cargos[self.cargo_name].amount += self.rate
            return True
        else:
            return False


class CargoConsumer:

    def __init__(self, cargo_name, rate):
        self.cargo_name = cargo_name
        self.rate = rate

    # Update the consumer - return true if cargo was consumed
    def update(self):
        if self.dock.cargos[self.cargo_name].amount >= 0 + self.rate:
            self.dock.cargos[self.cargo_name].amount -= self.rate
            return True
        else:
            return False

