import sys

def turn(move):
    directions = {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}
    return directions.get(move, move)

def debug(map_data, visited):
    for i, row in enumerate(map_data):
        print(''.join('X' if (i, j) in visited else cell for j, cell in enumerate(row)))

def sneaky(map_data):
    h, w = len(map_data), len(map_data[0])

    def in_bounds(i, j):
        return 0 <= i < h and 0 <= j < w

    visited = set()
    move = None
    start = None

    for i in range(h):
        for j in range(w):
            if map_data[i][j] in {'^', 'v', '<', '>'}:
                start = (i, j)
                move = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[map_data[i][j]]
                visited.add(start)
                break
        if start:
            break

    if not start or not move:
        return 0 

    curr = start

    while True:
        next_pos = (curr[0] + move[0], curr[1] + move[1])
        if not in_bounds(*next_pos):
            break

        if map_data[next_pos[0]][next_pos[1]] == '#':
            move = turn(move)
        else:
            visited.add(next_pos)
            curr = next_pos

    return len(visited)

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

