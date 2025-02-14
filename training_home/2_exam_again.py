import csv
import requests
# 1
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

# 2
response = requests.get("https://restcountries.com/v3.1/all")
if response.status_code != 200:
    raise Exception("Status code is not 200", response.status_code)
data = response.json()


for country in data:
    print(country["name"]["common"])

kopejais_valstu_sk = len(data)
print(f"Kopejais valstu skaits : {kopejais_valstu_sk}")

total_population = sum(country.get("population", 0) for country in data)
average_population= total_population/kopejais_valstu_sk
print(f"Videjajs population: {average_population:.2f}")
def max_pop():
    max_population = 0
    country_with_max=""
    for country in data:
        population= country.get("population", 0)
        if population > max_population:
            max_population= population
            country_with_max = country["name"]["common"]
    print(f"Valsts ar visslielako {country_with_max} tur dzivo {max_population}")    
max_pop()

total_area = sum(country.get("population", 0) for country in data)
print(f"Total area {total_area}")

def par_latviju():
    for country in data:
        if country["name"]["common"] =="Latvia":
            print(country["subregion"])
            borders = country.get("borders", [])
            print(f"Latvijas robežvalstu kodi: {', '.join(borders)}")
par_latviju()