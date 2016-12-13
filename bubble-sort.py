import math
import check

my_list = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
sorted_list = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]

def bubble_sort(unsorted_list):
    swapped = True
    while swapped:
        swapped = False
        for index in range(0, (len(unsorted_list)-1)):
            leftItem = unsorted_list[index]
            rightItem = unsorted_list[index + 1]
            
            if leftItem > rightItem:
                unsorted_list[index] = rightItem
                unsorted_list[index + 1] = leftItem
                swapped = True
    return unsorted_list

bubble_sort(my_list)
check.expect("TEST 1", bubble_sort(my_list), sorted_list)
