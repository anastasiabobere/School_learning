vowels = ["a", "e", "i", 'o', "u"]
def count_vowels(string):
    vowels_in_str =0
    for char in string:
        if char in vowels:
            vowels_in_str +=1 
    print(vowels_in_str)
    return vowels_in_str
count_vowels("hello woaaaarld")