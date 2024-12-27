#!/usr/bin/env python3

import sys

def turn_right(direction_index):
    return (direction_index + 1) % 4

def simulate(grid, start_row, start_col, start_dir_idx, rows, cols):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited_states = set()
    r, c = start_row, start_col
    d_idx = start_dir_idx
    
    while True:
        state = (r, c, d_idx)
        if state in visited_states:
            return True
        visited_states.add(state)

        dr, dc = directions[d_idx]
        front_r, front_c = r + dr, c + dc

        if not (0 <= front_r < rows and 0 <= front_c < cols):
            return False
        if grid[front_r][front_c] == '#':
            d_idx = turn_right(d_idx)
        else:
            r, c = front_r, front_c
            if not (0 <= r < rows and 0 <= c < cols):
                return False

def main():
    if len(sys.argv) < 2:
        print(f"no")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]

    grid = [list(row) for row in lines]
    rows = len(grid)
    cols = len(grid[0])

    guard_row, guard_col, guard_dir_idx = None, None, None
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                guard_row, guard_col = r, c
                guard_dir_idx = direction_map[grid[r][c]]
                break
        if guard_row is not None:
            break

    loop_count = 0

    for r in range(rows):
        for c in range(cols):
            if (r == guard_row and c == guard_col):
                continue
            if grid[r][c] == '#':
                continue

            original_char = grid[r][c]
            grid[r][c] = '#'

            if simulate(grid, guard_row, guard_col, guard_dir_idx, rows, cols):
                loop_count += 1

            grid[r][c] = original_char

    print(loop_count)

if __name__ == "__main__":
    main()

