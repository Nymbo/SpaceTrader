

class Clock:

    def __init__(self):
        self.delta = 0

    def update(self, pygame_clock):
        self.delta = pygame_clock.get_time()

    def get_time(self):
        return self.delta