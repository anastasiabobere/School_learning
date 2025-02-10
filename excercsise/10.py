def multiplication_table(number, limit):
    for i in range(1, limit+1):
        print(f"{number} x {i} = {number * i}")
multiplication_table(5, 10)