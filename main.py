from abc import ABC, abstractmethod

class Dzivnieks(ABC):
    def __init__(self, name, kajas):
        self.name = name
        self.kajas = kajas

    @abstractmethod
    def skanja(self):
        pass

    def __str__(self):
        return f"Tas ir {self.name} un vinam ir {self.kajas} kajas"

class Suns(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name = "Komisars " + self.name

    def skanja(self):
        return "woof"

class Kakis(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name = "Minkāns " + self.name

    def skanja(self):
        return "meow"
class Govs(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name = "Mister " + self.name

    def skanja(self):
        return "moooo"
class Papagailis(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name = "Papagailis " + self.name

    def skanja(self):
        return "Hello how are you doing?"
# List of animals
dzivnieki = [
    Kakis("Cat1", 4),
    Kakis("Cat2", 7),
    Suns("Suns1", 3),
    Govs("Gauja", 4), 
    Papagailis("Chika", 2)
]

# Loop through animals and print info
for animal in dzivnieki:
    print(animal)
    print(f"{animal.skanja()} - pateica {animal.name}")
    print("###########")
