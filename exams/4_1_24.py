import csv 
with open("agenti.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    dati =[row for row in reader]
def print_data(data):
    for row in data:
        print(row)
# print_data(dati)
tikai_izglitibas_valsts = [row for row in dati if row[0]=="Izglītības iestāde" or row[0]=="Valsts iestāde"]
# print_data(tikai_izglitibas_valsts)
tikai_riga = [row for row in tikai_izglitibas_valsts if "Rīga" in row[2].split(", ")]
# print_data(tikai_riga)
sorted = sorted(tikai_riga, key=lambda x:x[1])
print_data(sorted)