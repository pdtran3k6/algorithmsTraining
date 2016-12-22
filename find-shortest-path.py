import check

def all_moves(starting_point):
    Positions = []
    col_changes = (-1,1,0,0)
    row_changes = (0,0,-1,1)
    i = 0
    while(i < 4):
        Positions.append([
            starting_point[0] + row_changes[i], 
            starting_point[1] + col_changes[i]
            ])
        i += 1
    return Positions

def is_valid(position, row_size, col_size):
    if (0 <= position[0] < row_size 
    and 0 <= position[1] < col_size):
        return True
    return False

def find_shortest_path(my_map, starting_point, end_point):
    row_size = len(my_map)
    col_size = len(my_map[0])

    queue = []
    visited = [["" for x in range(col_size)] for y in range(row_size)]
    step_num = 0

    queue.append(starting_point)
    while queue != []:
        current_position = queue.pop(0)
        visited[current_position[0]][current_position[1]] = "a"
        if (current_position == end_point):
            print("Found shortest path")
            return

        for surrounding_position in all_moves(current_position):
            if (not (is_valid(surrounding_position, row_size, col_size)) 
            or (my_map[surrounding_position[0]][surrounding_position[1]] == 'X')
            or (visited[surrounding_position[0]][surrounding_position[1]] == 'a')
            or (surrounding_position in queue)):
                continue
            queue.append(surrounding_position)
    print("Can't find path")
    return
        
example_map = [
    ['', '', ''],
    ['', 'X', 'X'],
    ['', '', 'X'],
    ['', '', 'X'],
    ['', '', '']]

find_shortest_path(example_map, [3,0], [0,2])

    