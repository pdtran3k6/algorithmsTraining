import math
import check

list_1 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
sorted_list1 = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
def selection_sort(unsorted_list):
    smallest = 0
    sorted_list = []
    for index in range(0, len(unsorted_list)):
        smallest = unsorted_list[index]
        for nextIndex in range(index + 1, len(unsorted_list)):
            if smallest > unsorted_list[nextIndex]:
                # Swap smallest with the first item
                tempSmallest = smallest
                smallest = unsorted_list[nextIndex]
                unsorted_list[nextIndex] = tempSmallest

        sorted_list.append(smallest)
    return sorted_list

check.expect("TEST 1", selection_sort(list_1), sorted_list1)
