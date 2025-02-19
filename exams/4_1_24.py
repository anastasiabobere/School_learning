import csv

def read_csv(file_path, delimiter=";"):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        return [row for row in reader]

def print_data(data):
    for row in data:
        print(row)

def filter_education_and_state(data):
    return [row for row in data if row[0] == "Izglītības iestāde" or row[0] == "Valsts iestāde"]

def filter_riga(data):
    return [row for row in data if "Rīga" in row[2].split(", ")]

def sort_data(data):
    return sorted(data, key=lambda x: x[1])

data = read_csv("agenti.csv")
education_and_state_data = filter_education_and_state(data)
riga_data = filter_riga(education_and_state_data)
sorted_data = sort_data(riga_data)

print_data(sorted_data)
