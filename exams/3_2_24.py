class Skolotajs:
    stunduSkaitsNedela = 0
    uzvards = "N/A"
    skolotajaTips = 0

    def __init__(self, uzvards="N/A", stunduSkaitsNedela=0, skolotajaTips=0):
        self.uzvards = uzvards
        self.skolotajaTips = skolotajaTips
        self.stunduSkaitsNedela = stunduSkaitsNedela


class SakumsskolasSkolotajs(Skolotajs):
    klase = "x.i"  

    def __init__(self, uzvards="N/A", stunduSkaitsNedela=0, skolotajaTips=1, klase="x.i"):
        super().__init__(uzvards, stunduSkaitsNedela, skolotajaTips)
        self.klase = klase

    def ievads(self):
        self.uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
        self.klase = input("Ievadiet skolotāja klasi: ")
        self.stunduSkaitsNedela = int(input("Ievadiet skolotāja stundu skaitu: ")) 

    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} "
              f"māca {self.stunduSkaitsNedela} stundas {self.klase} klasē.")


class VidusskolasSkolotajs(Skolotajs):
    primaisPrieksmets = "x prieksmets"
    otraisPrieksmets = "prieksmets"
    pirmaisPrieksmetsStunduSkaits = 0
    otraisPrieksmetsStunduSkaits = 0

    def __init__(self, uzvards="N/A", skolotajaTips=3,
                 primaisPrieksmets="prieksmets", otraisPrieksmets="prieksmets",
                 pirmaisPrieksmetsStunduSkaits=0, otraisPrieksmetsStunduSkaits=0):
        super().__init__(uzvards, 0, skolotajaTips)  
        self.primaisPrieksmets = primaisPrieksmets
        self.otraisPrieksmets = otraisPrieksmets
        self.pirmaisPrieksmetsStunduSkaits = pirmaisPrieksmetsStunduSkaits
        self.otraisPrieksmetsStunduSkaits = otraisPrieksmetsStunduSkaits

    def ievads(self):
        self.uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
        self.primaisPrieksmets = input("Ievadiet pirmo pasniegto priekšmetu: ")
        self.pirmaisPrieksmetsStunduSkaits = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))  
        self.otraisPrieksmets = input("Ievadiet otro pasniegto priekšmetu: ")
        self.otraisPrieksmetsStunduSkaits = int(input("Ievadiet otrā priekšmeta stundu skaitu: ")) 
        self.stunduSkaitsNedela = self.pirmaisPrieksmetsStunduSkaits + self.otraisPrieksmetsStunduSkaits

    def izvade(self):
        print(f"Vidusskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} "
              f"māca šādus priekšmetus: {self.primaisPrieksmets} un {self.otraisPrieksmets}, kopā {self.stunduSkaitsNedela} stundas. ")



d2 = VidusskolasSkolotajs()
d2.ievads()
d2.izvade()
d1 = SakumsskolasSkolotajs()
d1.ievads()
d1.izvade()