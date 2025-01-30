class Skolens:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
        self.atzimes = []

    def pievenot_atzimes(self, atzime):
        if not isinstance(atzime, int) :
            raise ValueError("Atzimam jābūt skaitļam.")
        else:
            if atzime > 10 or atzime <1 :
                print(f"Jūs mēģināt pievenot {atzime } Tam jābut intervāla 1-10")
                atzime= 0
                self.atzimes.append(atzime)
            else:
                self.atzimes.append(atzime)
            

    def izvade(self):
        print(f"Vārds: {self.vards}, Vecums: {self.vecums} gadi;")
        print("Atzīmes: ")
        kopeja_atzime = 0
        for atzime in self.atzimes:
            kopeja_atzime += atzime
            print(atzime)
        print("-----------")
        videja_atzime = kopeja_atzime / len(self.atzimes)
        print(videja_atzime)
        print("#######################")

skolens1 = Skolens("Jānis", 18)
skolens1.pievenot_atzimes(5)
skolens1.pievenot_atzimes(4)
skolens1.pievenot_atzimes(9)
skolens1.izvade()

skolens1 = Skolens("Anastasija", 18)
skolens1.pievenot_atzimes(10)
skolens1.pievenot_atzimes(9)
skolens1.pievenot_atzimes(9)
skolens1.pievenot_atzimes(8)
skolens1.pievenot_atzimes(10)
skolens1.izvade()