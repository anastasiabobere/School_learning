def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number**0.5) + 1):  # Check divisors up to the square root
        if number % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

# Example usage
print(is_prime(10))  # Output: False
print(is_prime(7))   # Output: True