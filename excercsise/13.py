def remove_duplicates(lst):
    seen = set()  # To track elements we've already seen
    result = []   # To store the unique elements
    
    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)
    
    return result

# Example usage
print(remove_duplicates([1, 4, 2, 2, 3, 4, 4, 4, 4, 5]))