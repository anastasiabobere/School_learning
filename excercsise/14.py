def anagram(stringA, stringB):
    stringA = stringA.replace(" ", "").lower()
    stringB = stringB.replace(" ", "").lower()
    
    # Check if the sorted characters are the same
    return sorted(stringA) == sorted(stringB)
print(anagram("listen", "silent"))
print(anagram("hello", "world") )