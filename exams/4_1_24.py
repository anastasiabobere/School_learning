import csv 
with open("agenti.csv", "r", encoding="utf-8") as file:
    reader= csv.reader(file, delimiter=";")
    dati = [ row for row in reader] 
    def atvert(datus):
        for line in datus:
            print(line)
    iestades_valsts = [ row for row in dati if row[0] in ["Izglītības iestāde", "Valsts iestāde"]]
    def tikai_iestades_un_valsts(datus):
        for row in datus:
            print(row)
    rigas_iestades= [row for row in iestades_valsts if "Rīga" in row[2] ]
    def tikai_riga(datus):

        for line in datus:
            print(line)
    sorted= sorted(rigas_iestades, key=lambda x:x[1])
    def izvadit_sorted(datus):
        for line in datus:
            print(f"{line[1]} -{line[0]}- {line[2]}")
atvert(dati)
tikai_iestades_un_valsts(iestades_valsts)
tikai_riga(rigas_iestades)
izvadit_sorted(sorted)
