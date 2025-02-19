import requests
response = requests.get("https://data.gov.lv/dati/lv//api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=3800")
data = response.json()

if response.status_code !=200:
    raise Exception("Rādas kļuda pieprsijuma:", response.status_code)

# print(len(data))

needed_data = data["result"]["records"]
def print_locations(data, material_key, material_name):
    print(f"Šeit var nodot {material_name}:")
    for row in data:
        if row.get(material_key) == 'x':
            print(f"{row.get('adrese', ' ')} - {row.get('pilsetanovads', ' ')}")
    print("----------------")
# print_locations(needed_data, '2 : Stikls', 'stiklu')
print_locations(needed_data, '3 : Metāls', 'metālu')
print_locations(needed_data, '10 : Nolietotās riepas', 'riepas')
print_locations(needed_data, '8 : Baterijas un akumulatori', 'baterijas')

# # empty strings ???????
# for row in needed_data:
#     print(row.get("10 : Nolietotās riepas"))
#     print(row.get('8 : Baterijas un akumulatori'))
#     print(row.get('2 : Stikls'))
      
