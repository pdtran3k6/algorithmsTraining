from time import process_time

a1 = [1, 3, 5, 15, 25, 27, 35]
a2 = [2, 3, 4, 5, 35]



def num_common_elements(array1, array2, num_common):
    if len(array1) == max(len(array1), len(array2)):
        large_array = array1
        small_array = array2
    else:
        large_array = array2
        small_array = array1
    
    # check if the number is in the large array
    for number in small_array:
        if large_array.count(number) == 1:
            num_common += 1
    
    return num_common


def num_common_elements2(array1, array2, num_common):
    if len(array1) == max(len(array1), len(array2)):
        large_array = array1
        small_array = array2
    else:
        large_array = array2
        small_array = array1
    
    # check if the number is in the large array
    for number in small_array:
        if number in large_array:
            num_common += 1
    
    return num_common
