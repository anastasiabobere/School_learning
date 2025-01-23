class Vehicle :
    def __init__(self,zīmols, modelis,reg_datums,pilna_masa,degvielas_veids ):
        self.zīmols = zīmols
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids
    def __str__(self):
       return f"Auto zīmols: {self.zīmols}\n" \
               f"Modelis: {self.modelis}\n" \
               f"Reģistrācijas datums: {self.reg_datums}\n" \
               f"Pilna masa: {self.pilna_masa}\n" \
               f"Degvielas veids: {self.degvielas_veids}"
      
d1 = Vehicle("Audi","A4","22.10.2019",2000,"BG")
print(d1)