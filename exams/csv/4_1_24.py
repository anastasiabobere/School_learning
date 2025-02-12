import csv


with open("1.csv", newline="", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";", quotechar="|")
        print("1. Dati lejupielādēti un atvērti:")
        dati = [row for row in reader]
        print(dati)

        filtered_data_iestades = [row for row in dati if row['TIPS'] in ['Izglītības iestāde', 'Valsts iestāde']]

        print("\n2. Filtrēti dati (tikai Izglītības iestāde un Valsts iestāde):")
        for row in filtered_data_iestades:
            print(row)
        print("\n2. Filtrēti dati (Riga):")
        filtered_data_riga= [row for row in filtered_data_iestades if 'Rīga' in row['ADRESE']]
        for row in filtered_data_riga:
                  print(f"{row['NOSAUKUMS']} - {row['ADRESE']}")
        sorted_data = sorted(filtered_data_riga, key=lambda x: x['NOSAUKUMS'])
        for row in sorted_data:
                  print(f"{row['NOSAUKUMS']} - {row['ADRESE']}")




