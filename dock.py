from sprite import *
from cargo import *

class Dock(AnimatedSprite):
    def __init__(self):
        AnimatedSprite.__init__(self, 10, assets.loadAnim("assets/dock",1,9))
        self.ticks = 0
        self.producers = []
        self.consumers = []
        self.cargos     = {}
        self.cargos[CARGO_1_NAME] = Cargo(CARGO_1_NAME, 6, 30)
        self.cargos[CARGO_2_NAME] = Cargo(CARGO_2_NAME, 250, 60)
        self.cargos[CARGO_3_NAME] = Cargo(CARGO_3_NAME, 250, 80)
        self.cargos[CARGO_4_NAME] = Cargo(CARGO_4_NAME, 250, 100)
        self.cargos[CARGO_5_NAME] = Cargo(CARGO_5_NAME, 250, 120)
        self.cargos[CARGO_6_NAME] = Cargo(CARGO_6_NAME, 250, 130)
        self.cargos[CARGO_7_NAME] = Cargo(CARGO_7_NAME, 250, 140)
        self.cargos[CARGO_8_NAME] = Cargo(CARGO_8_NAME, 250, 140)
        self.listeners = []

    def update(self, clock):
        AnimatedSprite.update(self, clock)
        self.ticks +=1

        produced = consumed = False
        if self.ticks % 60 == 0:
            for producer in self.producers:
                produced = producer.update()
                if produced:
                    for listener in self.listeners:
                        listener.onDockCargoProduced(self, producer.cargo_name)
            for consumer in self.consumers:
                consumed = consumer.update()
                if consumed:
                    for listener in self.listeners:
                        listener.onDockCargoConsumed(self, consumer.cargo_name)


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


class DockListener:
    def onDockCargoProduced(self, dock, cargo_name):
        pass


    def onDockCargoConsumed(self, dock, cargo_name):
        pass