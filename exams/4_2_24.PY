import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
    return response.json()

def print_country_names(data):
    print("Visu valstu nosaukumi:")
    for country in data:
        print(country["name"]["common"])

def calculate_population_statistics(data):
    total_population = sum(country.get("population", 0) for country in data)
    average_population = total_population / len(data) if len(data) > 0 else 0
    return total_population, average_population

def find_country_with_max_population(data):
    max_population = 0
    country_with_max_population = ""
    for country in data:
        population = country.get("population", 0)
        if population > max_population:
            max_population = population
            country_with_max_population = country["name"]["common"]
    return country_with_max_population, max_population

def calculate_total_area(data):
    total_area = sum(country.get("area", 0) for country in data)
    return total_area

def print_latvia_details(data):
    for country in data:
        if country["name"]["common"] == "Latvia":
            print(f"\nLatvijas apakšreģions: {country.get('subregion', 'Nav datu')}")
            borders = country.get("borders", [])
            print(f"Latvijas robežvalstu kodi: {', '.join(borders)}")
            break

def main():
    url = "https://restcountries.com/v3.1/all"
    
    data = fetch_data(url)
    
    print_country_names(data)
    
    total_population, average_population = calculate_population_statistics(data)
    print(f"\nKopējais valstu skaits: {len(data)}")
    print(f"\nVidējais iedzīvotāju skaits: {average_population:.2f}")
    
    country_with_max_population, max_population = find_country_with_max_population(data)
    print(f"\nValsts ar vislielāko iedzīvotāju skaitu: {country_with_max_population} ({max_population} iedzīvotāji)")

    total_area = calculate_total_area(data)
    print(f"\nKopējā platība: {total_area:.2f} km²")
    
    
    print_latvia_details(data)


if __name__ == "__main__":
    main()
