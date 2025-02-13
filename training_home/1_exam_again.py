import csv
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    # for row in spamreader:
    #     print(', '.join(row))import csv

    dati = [row for row in spamreader]
def print_data(data):
    for row in data:
        print(row)
iestades = [row for row in dati if row[0] == "Izglītības iestāde" or row[0]=="Valsts iestāde"] 
print_data(iestades)

adrese = [row for row in iestades if 'Rīga' in row [2].split(", ")]
# print(adrese)
print_data(adrese)

sorted = sorted(adrese, key=lambda x:x[1])
print_data(sorted)