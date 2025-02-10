def second_largest(list):
    sorted_numbers = sorted(list, reverse=True)
    
    return sorted_numbers[1]
print(second_largest([3, 7, 2, 1119,640, 455]))