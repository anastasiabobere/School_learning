class Dzivnieks:
    def __init__(self, name, kajas):
        self.name = name
        self.kajas = kajas

    def skanja(self):
        return self.sound
    def __str__(self):
        return f"{self.name} un vinam ir {self.kajas} kajas"

class Suns(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name ="Komisars "+ self.name
        self.sound = "woof"

class Kakis(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.sound = "meow"

s1 = Suns("Arnold", 4)
d1 = Dzivnieks("Gauja", 6)
print(d1)
