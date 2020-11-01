from view.animated_sprite import *
from view.sprite import *
from cargo import *

class Dock(AnimatedSprite):
    def __init__(self):
        AnimatedSprite.__init__(self, 6, assets.loadAnim("assets/dock",1,9))
        self.producers = []
        self.consumers = []
        self.cargos     = {}
        self.initCargos()
        self.listeners = []
        self.time = 0 # Time since last consumers and producers updated.

    def update(self, clock):
        AnimatedSprite.update(self, clock)

        self.time += clock.get_time()
        if self.time > 2000:
            for producer in self.producers:
                produced = producer.update()
                if produced:
                    cargo = self.cargos[producer.cargo_name]
                    for listener in self.listeners:
                        listener.onDockCargoProduced(self, cargo)
            for consumer in self.consumers:
                consumed = consumer.update()
                if consumed:
                    cargo = self.cargos[consumer.cargo_name]
                    for listener in self.listeners:
                        listener.onDockCargoConsumed(self, cargo)
            self.time = 0

    def initCargos(self):
        def rand():
            return random.randint(100, 500)
        self.cargos[CARGO_1_NAME] = Cargo(CARGO_1_NAME, rand(), 30)
        self.cargos[CARGO_2_NAME] = Cargo(CARGO_2_NAME, rand(), 60)
        self.cargos[CARGO_3_NAME] = Cargo(CARGO_3_NAME, rand(), 80)
        self.cargos[CARGO_4_NAME] = Cargo(CARGO_4_NAME, rand(), 100)
        self.cargos[CARGO_5_NAME] = Cargo(CARGO_5_NAME, rand(), 120)
        self.cargos[CARGO_6_NAME] = Cargo(CARGO_6_NAME, rand(), 130)
        self.cargos[CARGO_7_NAME] = Cargo(CARGO_7_NAME, rand(), 140)
        self.cargos[CARGO_8_NAME] = Cargo(CARGO_8_NAME, rand(), 140)

    def setName(self, name):
        self.name = name

    def addProducer(self, producer):
        self.producers.append(producer)
        producer.dock = self

    def addConsumer(self, consumer):
        self.consumers.append(consumer)
        consumer.dock = self

    def setCargoPrice(self, cargo_name, price):
        self.cargos[cargo_name].price = price

    def getCargoPrice(self, cargo_name):
        return self.cargos[cargo_name].price

    def getCargoAmount(self, cargo_name):
        return self.cargos[cargo_name].amount

    def setCargoAmount(self, cargo_name, amount):
        self.cargos[cargo_name].amount = amount

    def addListener(self, listener):
        self.listeners.append(listener)

    def removeListener(self, listener):
        self.listeners.remove(listener)


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


class DockListener:
    def onDockCargoProduced(self, dock, cargo):
        pass


    def onDockCargoConsumed(self, dock, cargo):
        pass