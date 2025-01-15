class Dzivnieks:
    def __init__(self, name, kajas, sound):
        self.name = name
        self.kajas = kajas
        self.sound = sound

    def skanja(self):
        return self.sound

tigeris = Dzivnieks("tigeris", 4, "meow in caps")
print(tigeris.skanja())
