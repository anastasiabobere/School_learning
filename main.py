class Dzivnieks:
    def __init__(self, name, kajas):
        self.name =name
        self.kajas = kajas
        self.sound= "random animal noise"

    def skanja(self):
        return self.sound
    def __str__(self):
        return f" Tas ir {self.name} un vinam ir {self.kajas} kajas"

class Suns(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name ="Komisars "+ self.name
        self.sound = "woof"

class Kakis(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name = "Minkāns "+ self.name
        self.sound = "meow"

s1 = Suns("Arnold", 4)

d1 = Dzivnieks("Gauja", 6)
# print(d1)
# d1.skanja()
dzivnieki =[Kakis("Cat1", 4),Kakis("Cat2", 7), Suns("Suns1", 3), Dzivnieks("Arnolds", 9)]
for animal in dzivnieki:
    print(animal)
    print(f"{animal.skanja()} - pateica {animal.name}")
    print("###########")