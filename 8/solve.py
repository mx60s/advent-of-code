import sys
from math import gcd

def find_antinodes(map):
    r, c = len(map), len(map[0])
    towers = {}

    for i in range(r):
        for j in range(c):
            t = map[i][j]
            if t != '.':
                if t in towers:
                    towers[t].append((i, j))
                else:
                    towers[t] = [(i, j)]

    def in_bounds(i, j):
        return 0 <= i < r and 0 <= j < c 

    antinodes = set()
    for tower, locs in towers.items():
        l = len(locs)
        if l < 2:
            continue

        for i in range(l):
            for j in range(i + 1, l):
                dx, dy = locs[j][0] - locs[i][0], locs[j][1] - locs[i][1]
                g = gcd(dx, dy)
                dx, dy = dx // g, dy // g
                x, y = locs[i]
                while True:
                    possible = x + dx, y + dy
                    if in_bounds(*possible):
                        x, y = possible
                        antinodes.add(possible)
                    else:
                        break

                # extend out the other dir in the same way
                x, y = locs[j]
                while True:
                    possible = x - dx, y - dy
                    if in_bounds(*possible):
                        x, y = possible
                        antinodes.add(possible)
                    else:
                        break
                    
    return len(antinodes)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("fuck you")
        sys.exit(1)

    input_filename = sys.argv[1]

    try:
        with open(input_filename, 'r') as file:
            map = [list(line.strip()) for line in file]

        print(find_antinodes(map))
    except FileNotFoundError:
        print(f"fuck you, file '{input_filename}' not found.")
        sys.exit(1)

