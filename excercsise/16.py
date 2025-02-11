def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    print(longest)
longest_word("I loveornosomuchhonestlyidk programming in Py")