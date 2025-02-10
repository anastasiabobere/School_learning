def common_elements(listA, listB):
    common =[]
    for element in listA:
        if element in listB:
            common.append(element)
    return(common)   
        
print(common_elements([1, 2, 3, 4,7], [1,3, 4, 5, 6,7]))