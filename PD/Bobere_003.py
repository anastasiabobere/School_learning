from abc import ABC, abstractmethod
import random
class Telpa(ABC):
    def __init__(self, numurs, platiba):
        self.numurs = numurs
        self.platiba = platiba
        self.cilveku_skaits = 0

    def pievienot_cilvekus(self, skaits):
        self.cilveku_skaits += skaits
    @abstractmethod
    def parbaudit_kapaciteti(self):
        pass

class Datorklase(Telpa):
    def __init__(self, numurs, platiba, datoru_skaits):
        super().__init__(numurs, platiba)
        self.datoru_skaits = datoru_skaits

    def pietiek_inventaru(self):
        return self.datoru_skaits >= self.cilveku_skaits

    def parbaudit_kapaciteti(self):
        return self.cilveku_skaits > (self.platiba / 0.8)

    def __str__(self):
        informacija = f'Datorklase "{self.numurs}", {self.platiba}kvm, {self.datoru_skaits} datori, {self.cilveku_skaits} cilveki;'
        if not self.pietiek_inventaru():
            informacija += 'nepieciešami papildus datori; '
        if self.parbaudit_kapaciteti():
            informacija += 'pārāk daudz cilvēku'
        return informacija.strip()
class Kabinets(Telpa):
    def __init__(self, numurs, platiba, galdu_skaits):
        super().__init__(numurs, platiba)
        self.galdu_skaits = galdu_skaits

    def pietiek_inventaru(self):
        return self.galdu_skaits >= self.cilveku_skaits

    def parbaudit_kapaciteti(self):
        return self.cilveku_skaits > (self.platiba / 1.0)

    def __str__(self):
        informacija = f'Kabinets "{self.numurs}", {self.platiba}kvm, {self.galdu_skaits} galdi, {self.cilveku_skaits} cilveki;'
        if not self.pietiek_inventaru():
            informacija += 'nepieciešami papildus  galdi; '
        if self.parbaudit_kapaciteti():
            informacija += 'pārāk daudz cilvēku'
        return informacija.strip()
kabineti =[
    Datorklase("1", 14, 10),
    Datorklase("2", 25, 40),
    Datorklase("3", 81, 15),
    Datorklase("4", 22, 20),
    Kabinets("5", 10, 90),
    Kabinets("6", 53, 11),
    Kabinets("7", 32, 22),
    Kabinets("8", 38, 24)
]
for kabinet in kabineti:
    kabinet.pievienot_cilvekus(random.randrange(1, 40))
    print(kabinet)


# kluda
# test = Telpa("88", 90)
# print(test)

# Papilduzdevumi
def kabineti_nav_inventaru(arr):
    print("-------------------------")
    print("Šim kabinetam un klasem nav inventaru !!")
    for kabinet in arr:
        if not kabinet.pietiek_inventaru():
            print(kabinet)

def parak_daudz_cilveku(arr):
    print("-------------------------")
    print("Šim kabinetam ir parak daudz cilveku !!")
    for kabinet in arr:
        if kabinet.parbaudit_kapaciteti():
            print(kabinet)
kabineti_nav_inventaru(kabineti)
parak_daudz_cilveku(kabineti)
