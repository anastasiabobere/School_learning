# started 20:26
# finished 20:52
class Augi :
    nosaukums = "N/A"
    daudzums = 0
    def __init__(self, nosaukums, daudzums):
        self.nosaukums= nosaukums
        self.daudzums = daudzums
        if not isinstance(daudzums, int) or daudzums < 0:
            raise ValueError("Daudzumam jābut poztitv skaitlis")
    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami"
class Augļi(Augi):
    seklu_skaits= 0
    def __init__(self, nosaukums, daudzums, seklu_skaits):
        self.seklu_skaits = seklu_skaits
        if not isinstance(seklu_skaits, int):
            raise ValueError("Seklu skaitam jābut skaitlam")
        super().__init__(nosaukums, daudzums)
    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami, {self.seklu_skaits} uz 10 gramiem"
class Darzeņi(Augi):
    allergija = False
    def __init__(self, nosaukums, daudzums, allergija):
        self.allergija = allergija
        if not isinstance(allergija, bool):
            raise ValueError("Allergijai jabut true/ false")
        super().__init__(nosaukums, daudzums)
        
    def __str__(self):
        if self.allergija:
            status = "izraisa"
            
        else: 
            status = "neizraisa"
            
        return f"{self.nosaukums}, {self.daudzums} grami, allerģiju {status}"
class Puķes(Augi):
    ziedi= 0
    def __init__(self, nosaukums, daudzums, ziedi):
        self.ziedi = ziedi
        if not isinstance(ziedi, int):
            raise ValueError("Ziedu skaitam jābut skaitlam")
        super().__init__(nosaukums, daudzums)
    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami, {self.ziedi} ziedi"

class Recepte:
    nosaukums = "N/A"
    augi=[]
    
    vai_izraisa_allergiju = False
    vai_ir_derigs = True
    def __init__(self, nosaukums):
        self.augi=[]
        self.nosaukums= nosaukums
        self.vai_izraisa_allergiju = False
        self.vai_ir_derigs = True
    def add_augi(self,augs):
        self.augi.append(augs)
    def kopeja_masa(self):
        masa= 0
        for aug in self.augi:
            masa += aug.daudzums
        return masa
    def derigumu_parbaude(self):
        for aug in self.augi:
            if isinstance(aug, Puķes):
                self.vai_ir_derigs = False
    def alergiju_parbaude(self):
        for aug in self.augi:
            if isinstance(aug, Darzeņi) and aug.allergija:
                self.vai_izraisa_allergiju = True
    def izvade(self):
        print(f"Recepte: {self.nosaukums}")
        for aug in self.augi:
            print(aug)
        print("#######################")
        allergens = " alerģiju izraisa " if self.vai_izraisa_allergiju else " alerģiju neizraisa "
        derigums = "derīga" if self.vai_ir_derigs else "nederīga"
        print(f"Recepte {allergens}")
        print(f"Recepte {derigums}")
        print(f"Kopējā masa: {self.kopeja_masa()} grami")
        print("\n")
augļi=[
    Augļi("Āboli", 100, 5),
    Augļi("Bumbieri", 100, 7),
    Augļi("Apelsīni", 100, 9),
    Augļi("Banāni", 100, 6),
    Augļi("Mandarīni", 100, 8), 
    Augļi("Kivi", 100, 10),
    Augļi("Persiki", 100, 4),
    Augļi("Zemenes", 100, 3),
    Augļi("Mellenes", 100, 2)

]
dārzeņi=[  
    Darzeņi("Kartupelis", 100, False),
    Darzeņi("Bietes", 100, True),
    Darzeņi("Burkāni", 100, False),
    Darzeņi("Kāposti", 100, False),
    Darzeņi("ķirbji", 100, True),
    Darzeņi("Sīpoli", 100, False),
    Darzeņi("Čili", 100, True),
    Darzeņi("Paprika", 100, False),
    Darzeņi("Tomāti", 100, False)
]
puķes=[
    Puķes("Lilijas", 100, 5),
    Puķes("Tulpes", 100, 7),
    Puķes("Ziedi", 100, 9),
    Puķes("Krusteniski", 100, 6),
    Puķes("Kaktusi", 100, 8), 
    Puķes("Orhidejas", 100, 10),
    Puķes("Ābeles", 100, 4),
    Puķes("Bumbieri", 100, 3),
    Puķes("Kivi", 100, 2)
]

recepte1 = Recepte("Saldējums")
recepte1.add_augi(augļi[0])
recepte1.add_augi(dārzeņi[1])
recepte1.derigumu_parbaude()
recepte1.alergiju_parbaude()
recepte1.izvade()

recepte2 = Recepte("Zupa") 
recepte2.add_augi(dārzeņi[0])
recepte2.add_augi(dārzeņi[1])
recepte2.add_augi(dārzeņi[2])
recepte2.alergiju_parbaude()
recepte2.derigumu_parbaude()
recepte2.izvade()