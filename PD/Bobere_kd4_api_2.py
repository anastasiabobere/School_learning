import requests
import json
response = requests.get("https://restcountries.com/v3.1/all")

if response.status_code != 200:
    raise Exception(f"Kļūda API pieprasijumā: {response.status_code}")

data = response.json()
print(f"Kopumā valstu skaits: {len(data)}")

def ANO(data):
    ANO = [valsts for valsts in data if valsts["unMember"]]

    un_members = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
        "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
        "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
        "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia",
        "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad",
        "Chile", "China", "Colombia", "Comoros", "Republic of the Congo",
        "Costa Rica", "Ivory Coast", "Croatia", "Cuba", "Cyprus", "Czechia",
        "North Korea", "Democratic Republic of the Congo",
        "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
        "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji",
        "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
        "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
        "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
        "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan",
        "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan",
        "Laos", "Latvia", "Lebanon", "Lesotho",
        "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
        "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
        "Mauritania", "Mauritius", "Mexico", "Federated States of Micronesia",
        "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar",
        "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
        "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama",
        "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
        "Qatar", "Republic of Korea", "Republic of Moldova", "Romania",
        "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Samoa", "San Marino",
        "São Tomé and Príncipe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
        "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
        "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan",
        "Suriname", "Eswatini", "Switzerland", "Sweden", "Syria", "Tajikistan",
        "Thailand", "North Macedonia", "Timor-Leste",
        "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
        "United Republic of Tanzania", "United States", "Uruguay", "Uzbekistan",
        "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]

    country_names_in_data = {v["name"]["common"] for v in ANO} | {v["name"]["official"] for v in ANO}
    country_in_ANO_not_in_data = [valsts for valsts in un_members if valsts not in country_names_in_data]

    print(f"Vasts kas ir ANo, bet nav API uzradits ka ANO dalībvalsts: {country_in_ANO_not_in_data[0]}")
    return len(ANO)

print(f"Valstis, kas ir ANO dalībvalstis: {ANO(data)}")

valstis_ar_pirmdienu = [valsts for valsts in data if valsts["startOfWeek"] == "monday"]
procentuali = len(valstis_ar_pirmdienu) / len(data) * 100
print(f"Pirmdienas sākuma valstu procents: {procentuali:.2f}%")

valstis_ar_republic = [valsts for valsts in data if "republic" in valsts["name"]["official"].lower()]
print(f"Valstis, kuru nosaukumā ir 'republic': {len(valstis_ar_republic)}")

def tuvakajs_koordinata(coordinates):
    closest_lat = 0
    closest_lon = 0
    closest_valsts_vards = ""

    for valsts in data :
        if closest_lat == 0 and closest_lon == 0:
            closest_lat = valsts["latlng"][0]
            closest_lon = valsts["latlng"][1]
        else:
            if abs(valsts["latlng"][0] - coordinates[0]) < abs(closest_lat - coordinates[0]) and abs(valsts["latlng"][1] - coordinates[1]) < abs(closest_lon - coordinates[1]):
                closest_lat = valsts["latlng"][0]
                closest_lon = valsts["latlng"][1]
                closest_valsts_vards = valsts["name"]["common"]
    print(f"Tuvākā valsts ar  koordinātam: {closest_lat}, {closest_lon} ir {closest_valsts_vards}")
tuvakajs_koordinata([57.801558744803096, 23.240355694350477] )

def valsts_eiropa_landlocked(data):
    landlocked = []
    for valsts in data:
        if valsts["region"] == "Europe" and valsts["landlocked"]:
            landlocked.append(valsts)
    total_population = 0
    for valsts in landlocked:
        total_population += valsts["population"]
    return total_population
print(valsts_eiropa_landlocked(data))