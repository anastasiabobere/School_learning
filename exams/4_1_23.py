import requests
response = requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d")
data = response.json()

if response.status_code !=200:
    raise Exception("Rādas kļuda pieprsijuma:", response.status_code)
print(len(data))
for main in data:
    print(main)
needed_data = data["result"]["records"]
for row in needed_data:
    # print(row)
    # print("------------------------")
    print(row.get('8 : Baterijas un akumulatori'))
    # if row.get('8 : Baterijas un akumulatori') == 'x':
    #     print(row)