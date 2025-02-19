LATVIAN_ALPHABET = {
    'A': 1, 'Ā': 2, 'B': 3, 'C': 4, 'Č': 5, 'D': 6, 'E': 7, 'Ē': 8,
    'F': 9, 'G': 10, 'Ģ': 11, 'H': 12, 'I': 13, 'Ī': 14, 'J': 15,
    'K': 16, 'Ķ': 17, 'L': 18, 'Ļ': 19, 'M': 20, 'N': 21, 'Ņ': 22,
    'O': 23, 'P': 24, 'R': 25, 'S': 26, 'Š': 27, 'T': 28, 'U': 29,
    'Ū': 30, 'V': 31, 'Z': 32, 'Ž': 33
}

word_list = [None] * 33

def is_valid_word(word):
    return word.isalpha() and word.istitle()

def get_position(word):
    first_letter = word[0]
    return LATVIAN_ALPHABET.get(first_letter, None)

def add_word(word):
    position = get_position(word)
    if position is None:
        print(f"Kļūda: Vārds '{word}' nesākas ar derīgu latviešu burtu.")
        return False

    if word_list[position - 1] is None:
        print(f"Pievienoju vārdu '{word}' {position}. vietā.")
    else:
        print(f"Aizvietoju vārdu '{word_list[position - 1]}' ar '{word}' {position}. vietā.")
    word_list[position - 1] = word
    return True

def main():
    print("Programma sāk darbu. Ievadiet latviešu vārdus, kas sākas ar lielo burtu.")
    while None in word_list:
        user_input = input("Ievadiet vārdu: ").strip()
        if not is_valid_word(user_input):
            print("Kļūda: Ievadītā vērtība nav derīgs vārds. Lūdzu, ievadiet vēlreiz.")
            continue
        add_word(user_input)

    print("\nAlfabēta saraksts ir pilnībā aizpildīts:")
    for i, word in enumerate(word_list, start=1):
        print(f"{i}. {word}")

if __name__ == "__main__":
    main()