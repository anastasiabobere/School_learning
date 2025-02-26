import requests
import json

response = requests.get("https://restcountries.com/v3.1/all")

if response.status_code != 200:
    raise Exception(f"Kļūda API pieprasijumā: {response.status_code}")

data = response.json()  

def eiropas_valstis(dict):
    eirope=[]
    for valsts in dict:
        if valsts["region"] == "Europe":
            print(valsts["name"]["common"])
            eirope.append(valsts)
    print("-----------------------------------")
    return len(eirope)
# print(f"Eiropa ir {eiropas_valstis(data)}")
def francu_runa(dict):
    french_speaking_countries = []  
    african_french =[]
    for valsts in dict:
       
        if "languages" in valsts and 'fra' in valsts["languages"]:
            french_speaking_countries.append(valsts["name"]["common"])
            if valsts["region"] == "Africa":
                african_french.append(valsts["name"]["common"])
    
    for country in french_speaking_countries:
        print(country)
    print("-----------------------------------")
    for country in african_french:
        print(country)
    percent = len(african_french) / len(french_speaking_countries) * 100
    print(f"Afrikā ir {percent:.2f}% no franciski runājošajām valstīm.")
    return len(french_speaking_countries)

# print(francu_runa(data))

def land_valstits(dict):
    land_valstits = []
    for valsts in dict:
        if "land" in valsts["name"]["common"].lower():
            land_valstits.append(valsts["name"]["common"])
            print(valsts["name"]["common"])
    
# print(land_valstits(data))

def euro(dict):
    euro_countries =[]
    for valsts in dict:
        if "currencies" in valsts and  "EUR" in valsts["currencies"] :
            euro_countries.append(valsts["name"]["common"])
            print(valsts["name"]["common"])
    return len(euro_countries)
# print(euro(data))
def more_than_50_mil(dict):
    for valsts in dict:
        if "population" in valsts and valsts["population"] > 50000000:
            print(valsts["name"]["common"])
# more_than_50_mil(data)
def starts_with_B(dict):
    countriws_with_B = []
    for valsts in dict:
        if valsts["name"]["common"][0] == "B":
            print(valsts["name"]["common"])
            countriws_with_B.append(valsts["name"]["common"])
    return len(countriws_with_B)
# print(starts_with_B(data))
def continent_with_most_countries():
    continents = {}
    for valsts in data:
        if valsts["region"] in continents:
            continents[valsts["region"]] += 1
        else:
            continents[valsts["region"]] = 1
    print(continents)
    max_countries = max(continents, key=continents.get)
    print(max_countries)
continent_with_most_countries()