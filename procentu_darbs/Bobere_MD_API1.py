import requests
visas_augstkolas = "http://universities.hipolabs.com/search?"
def augstskolas_pec_valsti(country):
    response = requests.get(f"{visas_augstkolas}country={country}")
    
    if response.status_code != 200:
        raise Exception(f"Kļuda API pieprasijumā: {response.status_code}")
    
    return response.json()

def augstskolas_latvija():
    data = augstskolas_pec_valsti("Latvia")
    print(f"Latvijā ir {len(data)} augstskolas.")
    for augstskola in data:
        print(" ",augstskola.get("name"))
    print("-----------------------------------")
    return data


def augstskolas_francija():
    data = augstskolas_pec_valsti("France")
    print(f"Francijā ir {len(data)} augstskolas.")
   
    eu_domains = [uni for uni in data if any(website.endswith(".eu") for website in uni.get("domains", []))]
    print(f"Francijā {len(eu_domains) / len(data) * 100:.2f}% augstkolas ir  ar .eu domēnu.")

    paris_augstkolas = [uni for uni in data if "Paris" in uni.get("name", " ")]
    print(f"Francijā {len(paris_augstkolas)} augstkolas satur vārdu 'Paris'")

    http_adrese = [uni for uni in data if any(website.startswith("https") for website in uni.get("web_pages", []))]
    print(f"Francijā {len(http_adrese) / len(data) * 100:.2f}% adreses ir ar https adresi")
    print("-----------------------------------")
    return {
        "data": data,
        "eu_domains": eu_domains,
        "paris_augstkolas": paris_augstkolas,
        "http_adrese": http_adrese
    }

def augstkolas_ar_vardu_school():
    response= requests.get(f"{visas_augstkolas}name=school")
    data = response.json()
    # print("Augstskolas ar vārdu 'school':")
    # for augstskola in data:
    #     print(" ",augstskola.get("name"))
    print(f"Kopā ir {len(data)} augstskolas ar vārdu 'school'")
    print("-----------------------------------")
    return data


def valsts_ar_visvairak_augstkolam():
    eiropas_valstis = [
        "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland",
        "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands",
        "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia",
        "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom"
    ]
    max_skaits = 0
    valsts_ar_visvairak = ""
    print("Ielāde datus par Eiropas valstīm...")
    for valsts in eiropas_valstis:
        data = augstskolas_pec_valsti(valsts)
        if len(data) > max_skaits:
            max_skaits = len(data)
            valsts_ar_visvairak = valsts
    
    print(f"Valsts ar visvairāk augstskolām Eiropā ir {valsts_ar_visvairak} ar {max_skaits} augstskolām")
    print("-----------------------------------")
    return valsts_ar_visvairak, max_skaits  

def main():
    augstskolas_latvija()
    augstskolas_francija()
    augstkolas_ar_vardu_school()
    valsts_ar_visvairak_augstkolam()
    
if __name__ == "__main__":
    main()
