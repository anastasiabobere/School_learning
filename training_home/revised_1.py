# started 20:10
# finished 20:19
class Turnirs :
    nosaukums = "N/A"
    sporta_veids = "N/A"
    cilveku_skaits = 0
    grupu_skaits = 0
    def __init__(self, nosaukums, cilveku_skaits, grupu_skaits, sporta_veids):
        self.nosaukums= nosaukums
        self.cilveku_skaits = cilveku_skaits
        self.grupu_skaits= grupu_skaits
        self.sporta_veids = sporta_veids
        self.sponsori = []
    def add_sponsori(self, sponsor):
        self.sponsori.append(sponsor)

    def izvade(self):
        print(f"Šis ir {self.sporta_veids} turnīrs '{self.nosaukums}', kurā piedalās {self.cilveku_skaits} cilvēki, {self.grupu_skaits} grupās.")
        print("Sponsori: ")
        for sponsor in self.sponsori:
            print("- " + sponsor)
        # print("\n")
fortnte = Turnirs("Last Dab 2025", 89, 9, "Tortnite")
fortnte.add_sponsori("6VSK")
fortnte.add_sponsori("Red Bull")
fortnte.add_sponsori("Super monkey")
fortnte.izvade()


dance = Turnirs("KPD", 19, 90, "Dance")
dance.add_sponsori("VV1G")
dance.add_sponsori("Monster")
dance.add_sponsori("8a")
dance.izvade()

