def sum_even(list):
    suma = 0
    for number in list:
        if number % 2 == 0:
            suma += number
    print(suma)
sum_even([1, 2, 3, 4, 5, 5])