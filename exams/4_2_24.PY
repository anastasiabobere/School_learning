import requests

# Task 1: Make a request to the API
response = requests.get("https://restcountries.com/v3.1/all")

# Task 2: Check if the response is successful
if response.status_code != 200:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

data = response.json()

# Task 3: Print all common country names
print("Visu valstu nosaukumi:")
for country in data:
    print(country["name"]["common"])

# Task 4: Print the total number of countries
print(f"\nKopējais valstu skaits: {len(data)}")

# Task 5: Calculate and print the average population
total_population = sum(country.get("population", 0) for country in data)
average_population = total_population / len(data)
print(f"\nVidējais iedzīvotāju skaits: {average_population:.2f}")

# Task 6: Find and print the country with the largest population
max_population = 0
country_with_max_population = ""

for country in data:
    population = country.get("population", 0)
    if population > max_population:
        max_population = population
        country_with_max_population = country["name"]["common"]

print(f"\nValsts ar vislielāko iedzīvotāju skaitu: {country_with_max_population} ({max_population} iedzīvotāji)")

# Task 7: Calculate and print the total area of all countries
total_area = sum(country.get("area", 0) for country in data)
print(f"\nKopējā platība: {total_area:.2f} km²")

# Task 8: Information about Latvia
for country in data:
    if country["name"]["common"] == "Latvia":
        # 8.1: Subregion
        print(f"\nLatvijas apakšreģions: {country.get('subregion', 'Nav datu')}")

        # 8.2: Border country codes
        borders = country.get("borders", [])
        print(f"Latvijas robežvalstu kodi: {', '.join(borders)}")
        break