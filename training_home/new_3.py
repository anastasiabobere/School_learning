# started 20.40
# finished 20.58
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name, species,age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
    @abstractmethod
    def sound(self):
        pass 
    @abstractmethod
    def food_consumption(self):
        pass
class Mammal(Animal):
    def __init__(self,name, species,age, weight, fur_color):
        super().__init__(name,species,age, weight )
        self.fur_color = fur_color
    def sound(self):
        match self.species:
                case "big_cat":
                    return "Roar"
                case "dog":
                    return "Bark"
                case "cow":
                    return "Moo"
                case "cat":
                    return "Meow"
                case _:
                    return "Unknown sound"
    def food_consumption(self):
        return self.weight * 0.05
class Bird(Animal):
    def __init__(self,name, species,age, weight, wingspan):
        super().__init__(name,species,age, weight )
        self.wingspan = wingspan
    def sound(self):
        match self.species:
                case "eagle":
                    return "Screech"
                case "parrot":
                    return "Squawk"
                case "penguin":
                    return "Honk"
                case "owl":
                    return "Hoot"
                case _:
                    return "Unknown sound"
    def food_consumption(self):
        return self.weight * 0.02
class Reptile(Animal):
    def __init__(self, name, species, age, weight, is_venomous):
        super().__init__(name, species, age, weight)
        self.is_venomous = is_venomous  # Keep as boolean

    def sound(self):
        match self.species:
            case "snake":
                return "Hiss"
            case "turtle":
                return "Grunt"
            case "lizard":
                return "Squeak"
            case "crocodile":
                return "Roar"
            case _:
                return "Unknown sound"

    def food_consumption(self):
        return self.weight * 0.03

    def display_info(self):
        venom_status = "ir indīgs" if self.is_venomous else "nav indīgs"
        return f"{self.name} ({self.species}), Vecums: {self.age}, Svars: {self.weight}, Indīgums: {venom_status}"
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def all(self):
        return len(self.animals)

    def total_food_needed(self):
        return sum(animal.food_consumption() for animal in self.animals)

    def list_animals(self):
        for animal in self.animals:
            if hasattr(animal, 'display_info'):
                print(animal.display_info())
            else:
                print(f"{animal.name} ({animal.species})")
            print("---------------")

    def izvade(self):
        print(f"Zoodārzs {self.name}")
        print("Dzīvnieki:", ", ".join(animal.name for animal in self.animals))
        print(f"Kopējais dzīvnieku skaits: {self.all()}")


def find_heaviest_animal(arr):
    return max(arr, key=lambda animal: animal.weight).name

def find_oldest_animal(arr):
    return max(arr, key=lambda animal: animal.age).name
        
def count_animals_by_class(arr):
    counts = {"Zīdītāji": 0, "Putni": 0, "Rāpuļi": 0}
    for animal in arr:
        if isinstance(animal, Mammal):
            counts["Zīdītāji"] += 1
        elif isinstance(animal, Bird):
            counts["Putni"] += 1
        elif isinstance(animal, Reptile):
            counts["Rāpuļi"] += 1

    visvairak = max(counts, key=counts.get)
    return f"Zīdītāji: {counts['Zīdītāji']}, Putni: {counts['Putni']}, Rāpuļi: {counts['Rāpuļi']}. Visvairāk dzīvnieku ir {visvairak} klasei."
dzivnieki = [
    Mammal("Māra", "big_cat", 5, 120, "orange"),
    Bird("Pēteris", "parrot", 3, 2, 0.5),
    Reptile("Guntis", "snake", 1, 5, True),
    Mammal("Līga", "dog", 7, 25, "brown"),
    Bird("Jānis", "eagle", 4, 10, 1),
    Reptile("Liene", "lizard", 2, 1, False),
    Mammal("Jānis", "cow", 9, 250, "white"),
    Bird("Liene", "owl", 5, 3, 0.7),
    Reptile("Līga", "crocodile", 3, 50, True),
    Mammal("Guntis", "cat", 6, 5, "grey"),
]

zooparks = Zoo("Riga")
for dzivnieks in dzivnieki:
    zooparks.add_animal(dzivnieks)

zooparks.list_animals()
print(f"Kopējais pārtikas patēriņš: {zooparks.total_food_needed()} kg")
print(f"Smagākais dzīvnieks: {find_heaviest_animal(zooparks.animals)}")
print(f"Vecākais dzīvnieks: {find_oldest_animal(zooparks.animals)}")
print(count_animals_by_class(zooparks.animals))