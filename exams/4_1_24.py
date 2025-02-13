import csv

def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        return [row for row in reader]

def filter_by_type(data, types):
    return [row for row in data if row[0] in types]

def filter_by_city(data, city):
    return [row for row in data if city in row[2].split(' , ')]

def sort_data(data, key):
    return sorted(data, key=lambda x: x[key])

def print_data(data, format_str=None):
    for line in data:
        if format_str:
            print(format_str.format(*line))
        else:
            print(line)

def main():
    file_path = "agenti.csv"
    data = read_csv(file_path)

    print("All data:")
    print_data(data)

    types = ["Izglītības iestāde", "Valsts iestāde"]
    filtered_by_type = filter_by_type(data, types)
    print("\nFiltered by type:")
    print_data(filtered_by_type)

    city = "Rīga"
    rigas_iestades = filter_by_city(filtered_by_type, city)
    print(f"\nFiltered by city ({city}):")
    print_data(rigas_iestades)

    sorted_data = sort_data(rigas_iestades, 1)
    print("\nSorted data:")
    print_data(sorted_data, "{1} - {0} - {2}")

if __name__ == "__main__":
    main()