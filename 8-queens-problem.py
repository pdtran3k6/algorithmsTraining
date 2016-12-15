import math
import check

def is_Valid(new_queen, queens_list):
    my_row, my_col = new_queen
    my_diagonal1 = sum(new_queen)
    my_diagonal2 = my_row - my_col
    for queen in queens_list:
        row, col = queen
        diagonal1 = sum(queen)
        diagonal2 = row - col  
        if my_row == row:
            return False
        if my_col == col:
            return False
        if my_diagonal1 == diagonal1:
            return False
        if my_diagonal2 == diagonal2:
            return False
    return True

check.expect("T1 - valid case", is_Valid((4, 2), [(0, 0), (1, 3), (2, 1), (3, 4)]), True)
check.expect("T2 - invalid case: same row", is_Valid((0, 7), [(0, 3), (1, 2), (3, 5)]), False)
check.expect("T3 - invalid case: same column", is_Valid((1, 7), [(0, 3), (1, 2), (3, 5)]), False)
check.expect("T4 - invalid case: same diagonal1", is_Valid((0, 7), [(0, 3), (1, 2), (6, 1)]), False)
check.expect("T5 - invalid case: same diagonal2", is_Valid((4, 7), [(1, 2), (2, 5)]), False)

def solve(board_size):
    
