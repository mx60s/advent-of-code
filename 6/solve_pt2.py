import sys
from collections import defaultdict

def turn(move):
    directions = {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}
    return directions.get(move, move)

def debug(map_data, obs_locs):
    for i, row in enumerate(map_data):
        print(''.join('O' if (i, j) in obs_locs else cell for j, cell in enumerate(row)))

def sneaky(map_data):
    h, w = len(map_data), len(map_data[0])

    def in_bounds(i, j):
        return 0 <= i < h and 0 <= j < w

    move = None
    start = None

    for i in range(h):
        for j in range(w):
            if map_data[i][j] in {'^', 'v', '<', '>'}:
                start = (i, j)
                move = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[map_data[i][j]]
                break
        if start:
            break

    if not start or not move:
        return 0 

    curr = start
    obstacles = 0

    char_dict = {(-1, 0): '^', (1,0): 'v', (0, -1): '<', (0, 1): '>'}

    visited = defaultdict(set)

    def fill(mapp, pos, move):
        # when you hit an obstacle, walk backwards and fill in the path leading
        # up to it (like placing arrows directing you to obstacle)
        
        move_back = (-move[0], -move[1])
        i, j = pos[0] + move_back[0], pos[1] + move_back[1]

        while in_bounds(i, j):
            if mapp[i][j] == '#':
                break
            
            visited[(i, j)].add(move)
            
            i += move_back[0]
            j += move_back[1]
        
        return mapp 

    while True:
        next_pos = (curr[0] + move[0], curr[1] + move[1])
        if not in_bounds(*next_pos):
            break

        if map_data[next_pos[0]][next_pos[1]] == '#':
            map_data = fill(map_data, next_pos, move)
            move = turn(move)
        else:
            turned = turn(move)

            visited[next_pos].add(move)
            curr = next_pos

    # now check for overlapping visits
    for visits in visited.values():
        if len(visits) > 1:
            obstacles += 1

    return obstacles

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("fuck you")
        sys.exit(1)

    input_filename = sys.argv[1]

    try:
        with open(input_filename, 'r') as file:
            rows = [list(line.strip()) for line in file]

        print(sneaky(rows))
    except FileNotFoundError:
        print(f"fuck you, file '{input_filename}' not found.")
        sys.exit(1)

