class Turnirs :
    nosaukums = "N/A"
    cilveku_skaits =0
    grupu_skaits = 0
    sporta_veids= "N/A"
    
    def __init__(self,nosaukums,  cilveku_skaits,grupu_skaits,sporta_veids):
        self.nosaukums= nosaukums
        self.cilveku_skaits=cilveku_skaits
        self.grupu_skaits=grupu_skaits
        self.sporta_veids=sporta_veids
        self.sponsori = []
    def pievenot_sponsoru(self,sponsor):
        self.sponsori.append(sponsor)
    def izvade(self):
        print(f"Šis ir {self.sporta_veids} turnīrs '{self.nosaukums}', kurā piedalās {self.cilveku_skaits} cilvēki, {self.grupu_skaits} grupās.")
        print("Sponsori:")
        for sponsor in self.sponsori:
            print("  ", sponsor)
turnīrs1 = Turnirs("Last Dab 2023",18, 5, "Fortnite")
# turnīrs1.nosaukums = "Last Dab 2025"
turnīrs1.pievenot_sponsoru("Adidaš")
turnīrs1.pievenot_sponsoru("Mike")
turnīrs1.pievenot_sponsoru("DolčeNKabana")

turnīrs2 = Turnirs("Urban Basket Challenge",24, 6, "Basketbols")
# turnīrs2.nosaukums = "Urban Basket Challenge"
turnīrs2.pievenot_sponsoru("Nike")
turnīrs2.pievenot_sponsoru("V6VSK")
turnīrs2.pievenot_sponsoru("Red Bull")

turnīrs1.izvade()
print("\n")
turnīrs2.izvade()