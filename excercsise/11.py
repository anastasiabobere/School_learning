def count_words(sentence):
    # Split the sentence into words, handling multiple spaces
    words = [word for word in sentence.split(" ") if word]
   
    return len(words)


print(count_words("Hello world!"))  
print(count_words("Hello   world!"))  
print(count_words("  Hello world!  "))  