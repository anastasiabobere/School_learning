def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest_palindrome = 0
factors = (0, 0)

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product
            factors = (i, j)

print(f"Largest palindrome product: {largest_palindrome}")
print(f"Factors: {factors[0]} and {factors[1]}")
