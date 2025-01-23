class Kubs:
    def __init__(self, malas_garums, krasa):
        if malas_garums < 2 or malas_garums > 10:
            print("Malas garums nav derīgs, tiks iestatīts minimālais garums: 2 cm.")
            self.malas_garums = 2
        else:
            self.malas_garums = malas_garums
        self.krasa = krasa
        self.deleted = False
    
    def aprekinat_tilpumu(self):
        return self.malas_garums ** 3

    def __del__(self):
        if not self.deleted:
            print("Kubs likvidēts. bye")
            self.deleted = True
        self.malas_garums = None
        self.krasa = None
       
    
    def __str__(self):
        return f"Kuba malas garums: {self.malas_garums} krāsa: {self.krasa}, tilpums: {self.aprekinat_tilpumu()}"

class Bloks(Kubs):
    def __init__(self, krasa, kubu_skaits, malas_garums, forma):
        super().__init__(malas_garums, krasa)
        
        if 1 <= kubu_skaits <= 4:
            self.__kubu_skaits = kubu_skaits
        else:
            self.__kubu_skaits = 0
        
        self.krasa = krasa
        self.nosaukums = f"{krasa}{kubu_skaits}"
        self._forma = forma 
        self.update_derīgums()  
        
    def update_derīgums(self):
        valid_formas = [11, 12, 13, 14, 22]
        self.derīgums = 1 if self._forma in valid_formas else 0
        if self._forma not in valid_formas:
            print("Kļūda: Forma neatbilst noteikumiem")

    @property
    def forma(self):
        return self._forma
    
    @forma.setter
    def forma(self, value):
        self._forma = value
        self.update_derīgums()  
    
    def tilpums(self):
        return self.__kubu_skaits * (self.malas_garums ** 3)

# Piemēri :(
try:
    kubg = Kubs(10, "zaļa")
    print(kubg.aprekinat_tilpumu())
    print(kubg.krasa)

    kubr = Kubs(1, "sarkana")
    print(kubr.malas_garums)

    del(kubr)

    bloks1 = Bloks("orange", 3, 5, 13)
    print(bloks1.tilpums())
    print(bloks1.nosaukums)

    bloks2 = Bloks("zils", 5, 7, 20)
    print(bloks2.nosaukums)
    print(bloks2.derīgums)
    
  
    bloks2.forma = 12
    print(bloks2.nosaukums)
    print(bloks2.derīgums)

except Exception as e:
    print(f"Kļūda: {e}")
