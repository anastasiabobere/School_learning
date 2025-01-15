class Dzivnieks:
    def __init__(self, name, kajas, species):
        self.name = name
        self.kajas = kajas
        self.species = species
        if species == "dog":
            self.sound = "WOOF"
        elif species == "cat":
            self.sound = "MEOW!"
        elif species == "bird":
            self.sound = "CAWW!"
        else:
            self.sound = "Animal Noise"

    def skanja(self):
        return self.sound


tigeris = Dzivnieks("tigeris", 4, "big cat")
print(tigeris.skanja())
