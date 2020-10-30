import globvars

def setMode(new_mode):
    globvars.mode.disable()
    new_mode.enable()
    globvars.mode = new_mode

class Mode:

    def enable(self):
        pass

    def disable(self):
        pass

    def update(self):
        pass

    def onEvent(self, event):
        pass

    def draw(self):
        pass