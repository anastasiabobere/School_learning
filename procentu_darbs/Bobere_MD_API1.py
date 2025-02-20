import requests


def get_universities(country):
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
    
    return response.json()

def universities_in_latvia():
    data = get_universities("Latvia")
    print(f"Latvijā ir {len(data)} augstskolas.")
    for university in data:
        print(university.get("name"))

def universities_in_france():
    data = get_universities("France")
    print(f"Francijā ir {len(data)} augstskolas.")
    eu_domains = [domain for domain in data if any(website.endswith(".eu") for website in domain.get("domains", []))]
    print(f" Francijā {len(eu_domains) / len(data) * 100:.2f}% augstkolas ir  ar .eu domēnu.")
    paris_augstkolas = [uni for uni in data if "Paris" in uni.get("name", " ")]
    print(f"Francijā {len(paris_augstkolas)} augstkolas satur vārdu 'Paris'")
    http_adrese = [uni for uni in data if any(website.startswith("https") for website in uni.get("web_pages", []))]
    print(f"Francijā {len(http_adrese) / len(data) * 100:.2f}% adreses ir ar https adresi")




def main():
    universities_in_latvia()
    universities_in_france()
    

if __name__ == "__main__":
    main()
