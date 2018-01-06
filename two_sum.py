import check
def two_sum(array, num):
    if len(array) < 2:
        return False
    else:
        result = num - array[0]
        if result in array[1:]:
            return True
        else:
            return two_sum(array[1:], num)

s = [2, 5, 3, 1, 0, -6, -7, 9, 4]
p = [3]
check.expect("Test 1", two_sum(s, 5), True)
check.expect("Test 2", two_sum(p, 5), False)
check.expect("Test 3", two_sum(s, 0), False)
check.expect("Test 4", two_sum(s, 43), False)
check.expect("Test 5", two_sum(s, 13), True)