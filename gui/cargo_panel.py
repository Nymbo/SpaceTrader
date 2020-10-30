import assets
from gui.gui import *

class CargoPanel(MouseListener):

    def __init__(self):

        self.draw_buttons = True

        self.background_panel = Panel()
        self.background_panel.setPosition(30,100)
        self.background_panel.setSize(740, 600)

        self.dock = None

        # Create the planet header:
        planet_name_font = pygame.font.Font("assets/gui/LCD14.ttf", 30)
        self.planet_header = Text(planet_name_font)

        # Create headers for the panel:
        font = pygame.font.Font("assets/gui/LCD14.ttf", 16)
        self.cargo_name_header = Text(font, "Name:")
        self.cargo_carried_header = Text(font, "Carried:")
        # Only in dock mode:
        self.cargo_available_header = Text(font, "Avail:")
        self.cargo_price_header = Text(font, "Price:")
        self.cargo_buy_header = Text(font, "Buy:")
        self.cargo_sell_header = Text(font, "Sell:")

        # Create rows for the panel:
        self.rows = []
        for cargo_name in globvars.cargos:
            cargo = globvars.cargos[cargo_name]
            row = CargoRow(cargo)
            row.buy_button.addListener(self)
            row.sell_button.addListener(self)
            self.rows.append(row)


    def setDock(self, dock):
        self.dock = dock

    def setDrawButtons(self, draw_buttons):
        self.draw_buttons = draw_buttons

    def show(self):
        gui = globvars.gui
        gui.addWidget(self.background_panel)

        if self.dock != None:
            self.planet_header.setPosition(350, 100)
            self.planet_header.setText(self.dock.name)
            gui.addWidget(self.planet_header)

        # Add the headers to the gui:
        x = 100 if self.dock != None else 300
        y = 160

        self.cargo_name_header.setPosition(x, y)
        gui.addWidget(self.cargo_name_header)
        x += 200
        self.cargo_carried_header.setPosition(x,y)
        gui.addWidget(self.cargo_carried_header)
        x += 100

        if self.dock != None:
            self.cargo_available_header.setPosition(x, y)
            gui.addWidget(self.cargo_available_header)
            x += 100
            self.cargo_price_header.setPosition(x, y)
            gui.addWidget(self.cargo_price_header)

            if self.draw_buttons:
                x += 100
                self.cargo_buy_header.setPosition(x, y)
                gui.addWidget(self.cargo_buy_header)
                x += 100
                self.cargo_sell_header.setPosition(x, y)
                gui.addWidget(self.cargo_sell_header)


        # Add the rows for each cargo to the gui:
        y = 220

        for row in self.rows:
            x = 40 if self.dock != None else 240

            row.icon.setPosition(x, y)
            gui.addWidget(row.icon)

            x += 60

            row.name_text.setPosition(x, y)
            gui.addWidget(row.name_text)
            x += 200
            row.carried_text.setPosition(x, y)
            gui.addWidget(row.carried_text)
            x += 100

            if self.dock != None:
                row.available_text.setPosition(x, y)
                gui.addWidget(row.available_text)
                x += 100
                dock_cargo = self.dock.cargos[row.cargo.name]
                row.price_text.setPosition(x,y)
                row.price_text.setText(str(dock_cargo.price))
                gui.addWidget(row.price_text)
                if self.draw_buttons:
                    x += 100
                    row.buy_button.setPosition(x, y)
                    gui.addWidget(row.buy_button)
                    x += 100
                    row.sell_button.setPosition(x, y)
                    gui.addWidget(row.sell_button)

            y += 60



    def hide(self):
        gui = globvars.gui
        gui.removeWidget(self.background_panel)

        gui.removeWidget(self.planet_header)

        gui.removeWidget(self.cargo_name_header)
        gui.removeWidget(self.cargo_carried_header)
        gui.removeWidget(self.cargo_price_header)
        gui.removeWidget(self.cargo_available_header)
        gui.removeWidget(self.cargo_buy_header)
        gui.removeWidget(self.cargo_sell_header)

        for row in self.rows:
            gui.removeWidget(row.icon)
            gui.removeWidget(row.name_text)
            gui.removeWidget(row.carried_text)
            gui.removeWidget(row.available_text)
            gui.removeWidget(row.price_text)
            gui.removeWidget(row.buy_button)
            gui.removeWidget(row.sell_button)


    def update(self):
        dock = self.dock
        if dock == None: return

        for row in self.rows:
            dock_cargo = dock.cargos[row.cargo.name]
            row.available_text.setText(str(dock_cargo.amount))

            player_cargo = globvars.cargos[row.cargo.name]
            row.carried_text.setText(str(player_cargo.amount))


    def onMouseDown(self, widget):
        for row in self.rows:
            dock_cargo = self.dock.cargos[row.cargo.name]
            player_cargo = globvars.cargos[row.cargo.name]

            if widget == row.buy_button:
                target_player_cargo_amount = player_cargo.amount + 50
                total_price = 50 * dock_cargo.price
                credits = globvars.credits
                if dock_cargo.amount > 50 and target_player_cargo_amount <= player_cargo.capacity and total_price <= credits:
                    dock_cargo.amount -= 50
                    player_cargo.amount += 50
                    globvars.credits -= total_price

            elif widget == row.sell_button:
                target_dock_cargo_amount = dock_cargo.amount + 50
                if target_dock_cargo_amount <= dock_cargo.capacity and player_cargo.amount >= 50:
                    total_price = 50 * dock_cargo.price
                    player_cargo.amount -= 50
                    dock_cargo.amount += 50
                    globvars.credits += total_price


class CargoRow:

    def __init__(self, cargo):
        self.cargo = cargo

        font = pygame.font.Font("assets/gui/LCD14.ttf", 25)
        self.icon = Button(cargo.icon)
        self.name_text = Text(font, cargo.name)
        self.carried_text = Text(font , str(cargo.amount))
        self.available_text = Text(font)
        self.price_text = Text(font, str(cargo.price))
        buy_icon  = assets.loadImage("assets/gui/buy.png")
        sell_icon = assets.loadImage("assets/gui/sell.png")
        self.buy_button = Button(buy_icon)
        self.sell_button = Button(sell_icon)