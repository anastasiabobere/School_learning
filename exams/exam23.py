class Doctorate:
    name="N/A"
    pacientuSkaits=0
    def __init__(self, name="N/A", pacientuSkaits=0):
        self.name= name
        self.pacientuSkaits = pacientuSkaits
    def ievads(self):
        self.name= input("Ievadiet doktorāta nosaukumu: ")
        try:
            self.pacientuSkaits=int( input("Ievadiet pacientu skaitu: "))
        except:
            self.pacientuSkaits =0
            print("Ievadiet veselus skaitlus")
        # finally:
        #     print("ievade veiksmiga", self.pacientuSkaits)    
    def izvade(self):
        addition =""

        if(self.pacientuSkaits%10 !=1):
            addition ="s"
        print( f"Doktorāts {self.name} apkalpo {self.pacientuSkaits} pacientu{addition}.")
d1 = Doctorate()
d1.ievads()
d1.izvade()