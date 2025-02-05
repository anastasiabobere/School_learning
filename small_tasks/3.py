import math

def prime_factorization(number):
    # Print the number of 2s that divide number
    while number % 2 == 0:
        print(2)
        number //= 2

    # number must be odd at this point
    # so a skip of 2 (i.e., i = i + 2) can be used
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        # while i divides number, print i and divide number
        while number % i == 0:
            print(i)
            number //= i

    # Condition if number is a prime
    # number greater than 2
    if number > 2:
        print(number)

# Example usage
prime_factorization(600851475143)