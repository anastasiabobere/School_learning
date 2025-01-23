class Kubs:
    def __init__(self, malas_garums, krasa):
        if malas_garums < 2:
            print("Malas garums nav derīgs, tiks iestatīts minimālais garums: 2 cm.")
            self.malas_garums = 2
        elif malas_garums > 10:
            print("Malas garums nav derīgs, tiks iestatīts maksimālais garums: 10 cm.")
            self.malas_garums = 10
        else:
            self.malas_garums = malas_garums
        self.krasa = krasa
    
    def aprekinat_tilpumu(self):
        return self.malas_garums ** 3

    def __del__(self):
        if hasattr(self, 'krasa'):
            print(f"Kubs ar krāsu {self.krasa} likvidēts.")

class Bloks(Kubs):
    def __init__(self, krasa, kubu_skaits, malas_garums, forma):
        super().__init__(malas_garums, krasa)
        
        if not (1 <= kubu_skaits <= 4):
            raise ValueError("Neatbilst nosacījumiem")
            # self.__kubu_skaits = 0

        else:
            print("Neatbilst nosacījumiem")
            
            self.__kubu_skaits = kubu_skaits
        
        self.nosaukums = f"{krasa}{kubu_skaits}"
        self._forma = forma 
        self.update_derīgums()  
        
    def update_derīgums(self):
        valid_formas = [11, 12, 13, 14, 22]
        self.derīgums = 1 if self._forma in valid_formas else 0
        if self.derīgums == 0:
            print("Kļūda: Forma neatbilst noteikumiem")

    @property
    def forma(self):
        return self._forma
    
    @forma.setter
    def forma(self, value):
        self._forma = value
        self.update_derīgums()  
    
    def tilpums(self):
        return self.__kubu_skaits * self.aprekinat_tilpumu()

# Piemēri
kubg = Kubs(10, "zaļa")
print(f"Krāsa: {kubg.krasa}, Tilpums: {kubg.aprekinat_tilpumu()}")

kubr = Kubs(1, "sarkana")
print(f"Kubr malas garums: {kubr.malas_garums}")

del kubr

try:
    kubr
except NameError:
    print("kubr objekts vairs nav pieejams")

print(f"Kubg malas garums: {kubg.malas_garums}")
print(f"Kubg malas garums: {kubg.malas_garums}")

# Manually delete kubg at the end to prevent unexpected messages
del kubg
bloks1 = Bloks("orange", 3, 5, 13)
print(f"Nosaukums: {bloks1.nosaukums}, Tilpums: {bloks1.tilpums()}")

bloks2 = Bloks("zils", 5, 7, 20)
print(f"Nosaukums: {bloks2.nosaukums}, Derīgums: {bloks2.derīgums}")

bloks2.forma = 12
print(f"Nosaukums: {bloks2.nosaukums}, Derīgums: {bloks2.derīgums}")
del kubg