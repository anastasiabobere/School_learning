import math
from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, krasa, koordinata_x, koordinata_y):
        self.krasa = krasa
        self.koordinata_x = koordinata_x
        self.koordinata_y = koordinata_y

    @abstractmethod
    def laukums(self):
        pass

    @abstractmethod
    def perimetrs(self):
        pass

class Aplis(Figure):
    def __init__(self, krasa, koordinata_x, koordinata_y, radiuss):
        super().__init__(krasa, koordinata_x, koordinata_y)
        self.radiuss = radiuss

    def laukums(self):
        return round(math.pi * self.radiuss ** 2, 2)

    def perimetrs(self):
        return round(2 * math.pi * self.radiuss, 2)

    def __str__(self):
        return f"{self.krasa} Aplis({self.koordinata_x}, {self.koordinata_y}) radiuss = {self.radiuss}, laukums = {self.laukums()}, perimetrs = {self.perimetrs()}"

class Kvadrats(Figure):
    def __init__(self, krasa, koordinata_x, koordinata_y, mala):
        super().__init__(krasa, koordinata_x, koordinata_y)
        self.mala = mala

    def laukums(self):
        return round(self.mala ** 2, 2)

    def perimetrs(self):
        return round(4 * self.mala, 2)

    def __str__(self):
        return f"{self.krasa} Kvadrats({self.koordinata_x}, {self.koordinata_y}) mala = {self.mala}, laukums = {self.laukums()}, perimetrs = {self.perimetrs()}"

figures = [
   Aplis("zelta", 9.0, 8.9, 8),
    Kvadrats("balts", 6.0, 7.0, 54),
    Kvadrats("melns", 0.7, 7.0, 1),
    Aplis("zils", 4.3, 8.9, 8),
    Kvadrats("sarkans", 98.0, 6.0, 8),
    Kvadrats("brūns", 12.0, 7.0, 32),
    Aplis("dzeltens", 9.0, 8.9, 6),
]
def izvadit_sarakstu(arr):

    for figure in arr:
        print(figure)
        print("---------------")
izvadit_sarakstu(figures)

# Bus kluda, jo klase Figure ir abstrakta, un nevar tikt izveidota instace
# test = Figure("zils", 9.0, 8.9)
# print(test)

# Papildas uzdevumi
# 1
def aprekinat_kopejo_laukumu(arr):
    kopejais_laukums = 0
    for figure in arr:
        kopejais_laukums += figure.laukums()
        
    return f"Kopējāis laukums ir {round(kopejais_laukums, 2)} " 
print(aprekinat_kopejo_laukumu(figures))

# 2
def aprekinat_centru(arr):
    summa_x = 0
    summa_y = 0
    skaits = len(arr)
   
    for figure in arr:
        summa_x += figure.koordinata_x
        summa_y += figure.koordinata_y
        

    centrs_x = round(summa_x / skaits, 2)
    centrs_y = round(summa_y / skaits, 2)
    
    return f"Visu figūru viduspunktu koordinātes: ({centrs_x}, {centrs_y})"
print(aprekinat_centru(figures))
