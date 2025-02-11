def average(list):
    length = len(list)
    sum =0
    for n in list:
        sum += n
    return round(sum/length, 2)
print(average([1, 2, 3, 4, 5,5,5,10]))