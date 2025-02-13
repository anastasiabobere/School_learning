import requests
response = requests.get("https://restcountries.com/v3.1/all")
if response.status_code != 200:
    raise Exception(f"Failed {response.status_code}")
data = response.json()
for country in data:
    print(country["name"]["common"])
print("Kopa ", len(data))
total_population = sum(country.get("population", 0) for country in data)
average_population= total_population/ len(data)
print(average_population)

max_population = 0
country_with_max_population = ""
for country in data:
    population = country.get("population",0)
    if population > max_population:
        max_population = population
        country_with_max_population = country["name"]["common"]
print(f"\nValsts ar vislielāko iedzīvotāju skaitu: {country_with_max_population} ({max_population} iedzīvotāji)")
total_area = sum(country.get("area", 0) for country in data)
print(f"\nValstsus kopeja laukums {total_area}")
for country in data:
    if country["name"]["common"] =="Latvia":
        print(f"\n Apakšregio {country.get('subregion', 'Nav datu')}")
        robezas= country.get("borders", [])
        print(f"Latvijas robežvalstu kodi: {', '.join(robezas)}")
        break