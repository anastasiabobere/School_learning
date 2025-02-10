def is_palindrome(string):
    if string == string[::-1]:
        print("pal")
        return True
    else:
        print("n")
        return False
is_palindrome("racecar")
is_palindrome("hell")