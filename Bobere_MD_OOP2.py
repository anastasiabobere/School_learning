class Augi:
    nosaukums = "N/A"
    dauzums = 0
    def __init__(self, nosaukums, dauzums):
        self.nosaukums = nosaukums
        self.dauzums = dauzums

    def __str__(self):
        return f"{self.nosaukums}, {self.dauzums} grami"

class Augļi(Augi):
    seklu_skaits = 0
    def __init__(self, nosaukums, dauzums, seklu_skaits):
        super().__init__(nosaukums, dauzums)
        self.seklu_skaits = seklu_skaits

    def __str__(self):
        return f"{self.nosaukums}, {self.dauzums} grami, {self.seklu_skaits} sēklas uz 10 gramiem"

class Dārzeņi(Augi):
    allergija= "N/A"
    def __init__(self, allergija, nosaukums, dauzums):
        super().__init__(nosaukums, dauzums)
        self.allergija = allergija

    def __str__(self):
        if self.allergija:
            status = "alerģiju izraisa"
        else:
            status = "alerģiju neizraisa"
        return f"{self.nosaukums}, {self.dauzums} grami, {status}"

class Puķes(Augi):
    ziedu_skaits= 0 
    def __init__(self, ziedu_skaits, nosaukums, dauzums):
        super().__init__(nosaukums, dauzums)
        self.ziedu_skaits = ziedu_skaits

    def __str__(self):
        return f"{self.nosaukums}, {self.dauzums} grami, {self.ziedu_skaits} ziedi"

class Recepte:
    nosaukums = "N/A "
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.augi = []
        self.allergija = False
        self.derigums = True

    def pievienot_augu(self, aug):
        self.augi.append(aug)

    def deriguma_parbaude(self):
        for aug in self.augi:
            if isinstance(aug, Augi):
                self.derigums = False
    def allergijas_parbaude(self):
        for aug in self.augi:
            if isinstance(aug, Dārzeņi) and aug.allergija:
                self.allergija = True

    def izvade(self):
        print(f"Recepte: {self.nosaukums}")
        for aug in self.augi:
            print(f"* {aug}")
        print("###########")
        if self.allergija:
            status = "alerģiju izraisa"
        else:
            status = "alerģiju neizraisa"
        print("Recepte " + status)
        if self.derigums:
            derigums="derīga"
        else:
            derigums="nederīga"
        print("Recepte " + derigums)

augļi = [Augļi("Ābols", 100, 10), Augļi("Bumbieris", 200, 5), Augļi("Banāns", 50, 20), Augļi("Apelsīns", 150, 15)]
dārzeņi = [Dārzeņi(True, "Tomāts", 150), Dārzeņi(False, "Kartupelis", 300), Dārzeņi(True, "Sīpoli", 50), Dārzeņi(False, "Ķirbis", 200)]
puķes = [Puķes(5, "Lilijas", 10), Puķes(7, "Rozes", 25)]

recepte1 = Recepte("Banānu sufle")
recepte1.pievienot_augu(augļi[1])
recepte1.pievienot_augu(dārzeņi[1])
recepte1.pievienot_augu(augļi[2])
recepte1.deriguma_parbaude()
recepte1.allergijas_parbaude()
recepte1.izvade()

recepte2= Recepte("Ratatuille")
recepte2.pievienot_augu(dārzeņi[0])
recepte2.pievienot_augu(dārzeņi[3])
recepte2.pievienot_augu(puķes[0])
recepte2.deriguma_parbaude()
recepte2.allergijas_parbaude()
recepte2.izvade()