from sprite import *


class Dock(Sprite):
    def __init__(self):
        Sprite.__init__(self, assets.loadImage("assets/dock.png"))
        self.ticks = 0
        self.producers = []
        self.consumers = []
        self.cargo     = {}
        self.cargo["carbon"]   = Cargo(250, 30)
        self.cargo["selenium"] = Cargo(250, 60)
        self.cargo["uranium"]  = Cargo(250, 80)
        self.cargo["nitrogen"] = Cargo(250, 100)
        self.cargo["oxygen"]   = Cargo(250, 120)
        self.cargo["hydrogen"] = Cargo(250, 130)
        self.cargo["titanium"] = Cargo(250, 140)
        
    def setName(self, name):
        self.name = name

    def addProducer(self, producer):
        self.producers.append(producer)
        producer.dock = self

    def addConsumer(self, consumer):
        self.consumers.append(consumer)
        consumer.dock = self

    def setCargoPrice(self, cargo_name, price):
        self.cargo[cargo_name].price = price

    def getCargoPrice(self, cargo_name):
        return self.cargo[cargo_name].price

    def getCargoAmount(self, cargo_name):
        return self.cargo[cargo_name].amount

    def setCargoAmount(self, cargo_name, amount):
        self.cargo[cargo_name].amount = amount

    def update(self):
        self.ticks +=1
        
        if self.ticks % 60 == 0:
            for producer in self.producers:
                producer.update()
            for consumer in self.consumers:
                consumer.update()

                

class Cargo:
    def __init__(self, amount, price):
        self.amount = amount
        self.price  = price

class CargoProducer:

    def __init__(self, cargo_name, rate):
        self.cargo_name = cargo_name
        self.rate = rate
    
    def update(self):
        if self.dock.cargo[self.cargo_name].amount < 500 - self.rate:
            self.dock.cargo[self.cargo_name].amount += self.rate
        

class CargoConsumer:

    def __init__(self, cargo_name, rate):
        self.cargo_name = cargo_name
        self.rate = rate

    def update(self):
        if self.dock.cargo[self.cargo_name].amount > 0 + self.rate:
            self.dock.cargo[self.cargo_name].amount -= self.rate


def createDocks():
    scene = variables.scene
    docks = variables.docks

    planet = Sprite(assets.loadImage("assets/earth.png"))
    planet.setPosition(Vector2(-3000,-3000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Earth")
    dock.setPosition(Vector2(-3000,-3000))
    dock.setCargoPrice("carbon", 20)
    dock.setCargoAmount("carbon", 500)
    dock.addProducer(CargoProducer("carbon", 7))
    dock.addConsumer(CargoConsumer("selenium", 1))
    dock.addConsumer(CargoConsumer("uranium", 1))
    dock.addConsumer(CargoConsumer("nitrogen", 1))
    dock.addConsumer(CargoConsumer("oxygen", 1))
    dock.addConsumer(CargoConsumer("hydrogen", 1))
    dock.addConsumer(CargoConsumer("titanium", 1))
    
    scene.addSprite(dock)
    docks.append(dock)

    planet = Sprite(assets.loadImage("assets/mars.png"))
    planet.setPosition(Vector2(3000,-45000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Mars")
    dock.setPosition(Vector2(3000,-45000))
    dock.setCargoPrice("selenium", 45)
    dock.setCargoAmount("selenium", 500)
    dock.addProducer(CargoConsumer("carbon", 1))
    dock.addConsumer(CargoProducer("selenium", 7))
    dock.addConsumer(CargoConsumer("uranium", 1))
    dock.addConsumer(CargoConsumer("nitrogen", 1))
    dock.addConsumer(CargoConsumer("oxygen", 1))
    dock.addConsumer(CargoConsumer("hydrogen", 1))
    dock.addConsumer(CargoConsumer("titanium", 1))
    scene.addSprite(dock)
    docks.append(dock)

    planet = Sprite(assets.loadImage("assets/jupiter.png"))
    planet.setPosition(Vector2(-83000,-30000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Jupiter")
    dock.setPosition(Vector2(-83000,-30000))
    dock.setCargoPrice("uranium", 65)
    dock.setCargoAmount("uranium", 500)
    dock.addProducer(CargoConsumer("carbon", 1))
    dock.addConsumer(CargoConsumer("selenium", 1))
    dock.addConsumer(CargoProducer("uranium", 7))
    dock.addConsumer(CargoConsumer("nitrogen", 1))
    dock.addConsumer(CargoConsumer("oxygen", 1))
    dock.addConsumer(CargoConsumer("hydrogen", 1))
    dock.addConsumer(CargoConsumer("titanium", 1))
    scene.addSprite(dock)
    docks.append(dock)

    planet = Sprite(assets.loadImage("assets/neptune.png"))
    planet.setPosition(Vector2(-53000,-63000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Neptune")
    dock.setPosition(Vector2(-53000,-63000))
    dock.setCargoPrice("nitrogen", 65)
    dock.setCargoAmount("nitrogen", 500)
    dock.addProducer(CargoConsumer("carbon", 1))
    dock.addConsumer(CargoConsumer("selenium", 1))
    dock.addConsumer(CargoConsumer("uranium", 1))
    dock.addConsumer(CargoProducer("nitrogen", 7))
    dock.addConsumer(CargoConsumer("oxygen", 1))
    dock.addConsumer(CargoConsumer("hydrogen", 1))
    dock.addConsumer(CargoConsumer("titanium", 1))
    scene.addSprite(dock)
    docks.append(dock)

    planet = Sprite(assets.loadImage("assets/venus.png"))
    planet.setPosition(Vector2(30000,-43000))
    scene.addSprite(planet)   
    dock = Dock()
    dock.setName("Venus")
    dock.setPosition(Vector2(30000,-43000))
    dock.setCargoPrice("oxygen", 100)
    dock.setCargoAmount("oxygen", 500)
    dock.addProducer(CargoConsumer("carbon", 1))
    dock.addConsumer(CargoConsumer("selenium", 1))
    dock.addConsumer(CargoConsumer("uranium", 1))
    dock.addConsumer(CargoConsumer("nitrogen", 1))
    dock.addConsumer(CargoProducer("oxygen", 7))
    dock.addConsumer(CargoConsumer("hydrogen", 1))
    dock.addConsumer(CargoConsumer("titanium", 1))
    scene.addSprite(dock)
    docks.append(dock)

    planet = Sprite(assets.loadImage("assets/mercury.png"))
    planet.setPosition(Vector2(80000,40000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Mercury")
    dock.setPosition(Vector2(80000,40000))
    dock.setCargoPrice("hydrogen", 110)
    dock.setCargoAmount("hydrogen", 500)
    dock.addProducer(CargoConsumer("carbon", 1))
    dock.addConsumer(CargoConsumer("selenium", 1))
    dock.addConsumer(CargoConsumer("uranium", 1))
    dock.addConsumer(CargoConsumer("nitrogen", 1))
    dock.addConsumer(CargoConsumer("oxygen", 1))
    dock.addConsumer(CargoProducer("hydrogen", 7))
    dock.addConsumer(CargoConsumer("titanium", 1))
    scene.addSprite(dock)
    docks.append(dock)

    planet = Sprite(assets.loadImage("assets/saturn.png"))
    planet.setPosition(Vector2(30000,80000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Saturn")
    dock.setPosition(Vector2(30000,80000))
    dock.setCargoPrice("titanium", 120)
    dock.setCargoAmount("titanium", 500)
    dock.addProducer(CargoConsumer("carbon", 1))
    dock.addConsumer(CargoConsumer("selenium", 1))
    dock.addConsumer(CargoConsumer("uranium", 1))
    dock.addConsumer(CargoConsumer("nitrogen", 1))
    dock.addConsumer(CargoConsumer("oxygen", 1))
    dock.addConsumer(CargoConsumer("hydrogen", 1))
    dock.addConsumer(CargoProducer("titanium", 7))
    scene.addSprite(dock)
    docks.append(dock)


    planet = Sprite(assets.loadImage("assets/uranus.png"))
    planet.setPosition(Vector2(-130000,43000))
    scene.addSprite(planet)
    dock = Dock()
    dock.setName("Uranus")
    dock.setPosition(Vector2(-130000,43000))
    scene.addSprite(dock)
    docks.append(dock)
