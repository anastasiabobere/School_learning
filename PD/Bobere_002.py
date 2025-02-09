class Autovaditajs:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.automasinuZimju=[]
        self.sodaPunkti = 0
    def pievenot_zimju(self, numurZime):
        self.automasinuZimju.append(numurZime)
    def sods(self, punkti):
        self.sodaPunkti += punkti
    def izvade(self):
        print(f"Vārds : {self.name}, Vecums : {self.age} ")
        print(f"Automāšinas īpašuma ({len(self.automasinuZimju)}) : ")
        for masina in self.automasinuZimju:
            print(" "+ masina)
        print(f"Soda punkti {self.sodaPunkti}")
        print("---------------------")
driver1 = Autovaditajs("Anastasija", 18)
driver1.pievenot_zimju("NL-1919")
driver1.pievenot_zimju("LAK-8040")
driver1.pievenot_zimju("LAK-0000")
driver1.izvade()
driver2 = Autovaditajs("Mareks", 28)
driver2.pievenot_zimju("OB-2992")
driver2.pievenot_zimju("NAD-0000")
driver2.pievenot_zimju("LAK-0010")
driver2.pievenot_zimju("LAK-ii10")
driver2.sods(4.0)
driver2.sods(3.0)
driver2.izvade()