class Skolotajs:
    stunduSkaitsNedela = 0
    uzvards = "N/A"
    skolotajaTips = 0

    def __init__(self, uzvards="N/A", stunduSkaitsNedela=0, skolotajaTips=0):
        self.uzvards = uzvards
        self.skolotajaTips = skolotajaTips
        self.stunduSkaitsNedela = stunduSkaitsNedela


class SakumsskolasSkolotajs(Skolotajs):
    klase = "x.i"  # default class if not provided

    def __init__(self, uzvards="N/A", stunduSkaitsNedela=0, skolotajaTips=1, klase="x.i"):
        super().__init__(uzvards, stunduSkaitsNedela, skolotajaTips)
        self.klase = klase
    def ievads(self):
        self.uzvards= input("Ievadiet sākumskolas skolotāja uzvārdu: ")
        self.klase= input("Ievadiet skolotāja klasi: ")
        self.stunduSkaitsNedela= input("Ievadiet skolotāja stundu skaitu: ")
    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} "
              f"māca {self.stunduSkaitsNedela} stundas {self.klase} klasē.")


class VidusskolasSkolotajs(Skolotajs):
    primaisPrieksmets = "x prieksmets"  # default subject
    otraisPrieksmets = "prieksmets"  # default subject
    pirmaisPrieksmetsStunduSkaits = 0  # default hours for the first subject
    otraisPrieksmetsStunduSkaits = 0  # default hours for the second subject

    def __init__(self, uzvards="N/A", stunduSkaitsNedela=0, skolotajaTips=0,
                 primaisPrieksmets="x prieksmets", otraisPrieksmets="prieksmets",
                 pirmaisPrieksmetsStunduSkaits=0, otraisPrieksmetsStunduSkaits=0):
        super().__init__(uzvards, stunduSkaitsNedela, skolotajaTips)
        self.primaisPrieksmets = primaisPrieksmets
        self.otraisPrieksmets = otraisPrieksmets
        self.pirmaisPrieksmetsStunduSkaits = pirmaisPrieksmetsStunduSkaits
        self.otraisPrieksmetsStunduSkaits = otraisPrieksmetsStunduSkaits
        # Total hours is the sum of both subjects
        self.stunduSkaitsNedela = self.pirmaisPrieksmetsStunduSkaits + self.otraisPrieksmetsStunduSkaits
    def ievads(self):
        self.uzvards= input("Ievadiet vidusskolas skolotāja uzvārdu: ")
        self.primaisPrieksmets= input("Ievadiet pirmo pasniegto priekšmetu: ")
        self.stunduSkaitsNedela= input("Ievadiet skolotāja stundu skaitu: ")
    def izvade(self):
        print(f"Vidusskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} "
              f"māca {self.stunduSkaitsNedela} stundas ({self.primaisPrieksmets}, {self.otraisPrieksmets}) "
              "priekšmetos.")


d1 = SakumsskolasSkolotajs()
d1.ievads()
d1.izvade()