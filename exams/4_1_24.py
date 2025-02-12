import csv
with open("agenti.csv", "r", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";",quotechar="|")
    # for line in csv_reader:
    #     print(line)
    dati = [row for row in csv_reader]

    iestades =[row for row in dati if row[0] in ['Izglītības iestāde', 'Valsts iestāde']]
    for row in iestades:
        print(iestades)
    riga = [row for row in iestades if 'Rīga' in row[2]]
    for row in riga:
        print(row)
    sorted = sorted(riga, key=lambda x:x[1])
    for row in sorted:
        print(f"{row[1]} - {row[2]}")