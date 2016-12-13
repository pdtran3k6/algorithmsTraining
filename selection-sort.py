import math
import check

my_list = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
sorted_list = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]

def selection_sort(unsorted_list):
    smallest = 0
    for index in range(0, len(unsorted_list)):
        smallest = unsorted_list[index]
        for nextIndex in range(index + 1, len(unsorted_list)):
            if smallest > unsorted_list[nextIndex]:
                # Swap smallest with the first item
                temp = smallest
                smallest = unsorted_list[nextIndex]
                unsorted_list[nextIndex] = temp
        unsorted_list[index] = smallest
    return unsorted_list

selection_sort(my_list)
check.expect("TEST 1", selection_sort(my_list), sorted_list)
