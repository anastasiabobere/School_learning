def sum_even(limit):
    a = 1
    b = 2
    even_sum = 0
    
    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b  
    
    return even_sum

result = sum_even(4000000)
print(result)
