import csv
file_name = "pokemon_data.csv"

pokemons = []

with open(file_name, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["HP"] = int(row["HP"])
        row["Attack"] = int(row["Attack"])
        row["Defense"] = int(row["Defense"])
        row["Speed"] = int(row["Speed"])
        pokemons.append(row)

lielakais_uzbrukums = max(pokemons, key=lambda pokemon: pokemon["Attack"])
print(f"Visaugstakais uzbrukumā: {lielakais_uzbrukums['Name']}, viņa uzbrukuma speja ir {lielakais_uzbrukums['Attack']}")

videjajs_HP = sum(pokemon["HP"] for pokemon in pokemons) / len(pokemons)
print(f"Vidējais HP: {videjajs_HP:.2f}")

udens_pokemon = [pokemon for pokemon in pokemons if "Water" in pokemon["Type"]]
print(f"Ūdens tipa pokemoni: {len(udens_pokemon)}")

atrakais_pokemon = max(pokemons, key=lambda pokemon: pokemon["Speed"])
print(f"Ātrākais pokemons: {atrakais_pokemon['Name']}, viņa atrums ir {atrakais_pokemon['Speed']}")

def most_common_type(pokemons):
    types = {}
    for pokemon in pokemons:
        if "," in pokemon["Type"]:
            for type in pokemon["Type"].split(","):
                if type in types:
                    types[type] += 1
                else:
                    types[type] = 1
    common_type = max(types, key=types.get)
    return common_type
print(f"Visbiežāk sastopamais tips: {most_common_type(pokemons)}")

labakais_aizsardziba = max(pokemons, key=lambda pokemon: pokemon["Defense"])
print(f"Labākais aizsardzībā: {labakais_aizsardziba['Name']}, viņa aizsardzībā ir {labakais_aizsardziba['Defense']}")

pokemoni_ar_multi_tipiem = [pokemon for pokemon in pokemons if "," in pokemon["Type"]]
print(f"Pokemoni ar vairākiem tipiem: {len(pokemoni_ar_multi_tipiem)}")
