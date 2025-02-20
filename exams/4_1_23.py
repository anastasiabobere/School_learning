import requests
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS location (
    _id INTEGER PRIMARY KEY,
    pilsetanovads TEXT,
    adrese TEXT,
    map TEXT,
    papirs TEXT,
    plastmasa TEXT,
    stikls TEXT,
    metals TEXT,
    bio TEXT,
    tekstils TEXT,
    elektro TEXT,
    apgaismes TEXT,
    baterijas TEXT,
    sadzives TEXT,
    riepas TEXT
)
''')

response = requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=3800")

if response.status_code != 200:
    raise Exception(f"Rādas kļūda pieprasījumā: {response.status_code}")

data = response.json()

needed_data = data["result"]["records"]

for record in needed_data:
    _id = record.get('_id')
    
    cursor.execute('''SELECT _id FROM location WHERE _id = ?''', (_id,))
    existing_record = cursor.fetchone()
    
    if existing_record:
        print(f"Record with _id {_id} already exists. Skip.")
        continue

    cursor.execute('''
    INSERT INTO location (
        _id, pilsetanovads, adrese, map, papirs, plastmasa, stikls, metals, bio, tekstils, elektro, apgaismes, baterijas, sadzives, riepas
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        _id,
        record.get('pilsetanovads'),
        record.get('adrese'),
        record.get('map'),
        record.get('0 : Papīrs'),
        record.get('1 : Plastmasa'),
        record.get('2 : Stikls'),
        record.get('3 : Metāls'),
        record.get('4 : Bioloģiski noārdāmie atkritumi'),
        record.get('5 : Tekstilmateriāli'),
        record.get('6 : Elektriskās un elektroniskās iekārtas'),
        record.get('7 : Apgaismes iekārtas un spuldzes'),
        record.get('8 : Baterijas un akumulatori'),
        record.get('9 : Sadzīvē radušies bīstamie atkritumi'),
        record.get('10 : Nolietotās riepas')
    ))

def print_locations_db(cursor, material_key, material_name):
    print(f"Šeit var nodot {material_name}:")
    statement = f"SELECT adrese, pilsetanovads FROM location WHERE {material_key} = 'x'"
    cursor.execute(statement)
    output = cursor.fetchall()
    if output:
        for row in output:
            print(f"{row[0]} - {row[1]}")
    else:
        print("Nav atrastas atbilstošas vietas.")
    print("----------------")

print_locations_db(cursor, 'stikls', 'stiklu')
# print_locations_db(cursor, '3 : Metāls', 'metālu')
print_locations_db(cursor, 'riepas', 'riepas')
print_locations_db(cursor, 'baterijas', 'baterijas')


conn.commit()
conn.close()

def print_locations(data, material_key, material_name):
    print(f"Šeit var nodot {material_name}:")
    for row in data:
        if row.get(material_key) == 'x':
            print(f"{row.get('adrese', ' ')} - {row.get('pilsetanovads', ' ')}")
    print("----------------")

# print_locations(needed_data, '2 : Stikls', 'stiklu')
# print_locations(needed_data, '3 : Metāls', 'metālu')
# print_locations(needed_data, '10 : Nolietotās riepas', 'riepas')
# print_locations(needed_data, '8 : Baterijas un akumulatori', 'baterijas')
