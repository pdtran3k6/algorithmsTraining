import math
import check

def all_Positions(current_position):
    Positions = []
    col_changes = (-1,-2,-2,-1,1,2,2,1)
    row_changes = (-2,-1,1,2,2,1,-1,-2)
    i = 0
    while(i < 8):
        Positions.append([
            current_position[0] + row_changes[i], 
            current_position[1] + col_changes[i]
            ])
        i += 1
    return Positions

check.expect("T1", all_Positions([2, 2]), [[0, 1], [1, 0], [3, 0], [4, 1], [4, 3], [3, 4], [1, 4], [0, 3]])

def is_Valid_Position(position, board_size):
    if (position[0] >= board_size or position[1] >= board_size):
        return False
    return True

check.expect("T1 - valid case", is_Valid_Position([4, 2], 5), True)
check.expect("T2 - invalid: row doesn't exist", is_Valid_Position([5, 0], 5), False)
check.expect("T3 - invalid: col doesn't exist", is_Valid_Position([0, 5], 5), False)
check.expect("T4 - invalid: row and col don't exist", is_Valid_Position([7, 6], 5), False)
