import requests

response = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()

print("Common names of all countries:")
for country in countries:
    # if 'name' in country and 'common' in country['name']:
    #     print(country['name']['common'])
    if "population" in country  and "name" in country:
        print(country["name"]["common"])
        print(country["population"])
print(len(countries))

