import sys
import re

def solve_crossword(crossword):
    rows, cols = len(crossword), len(crossword[0])

    horizontal = ["".join(row) for row in crossword]
    vertical = ["".join(crossword[row][col] for row in range(rows)) for col in range(cols)]
    
    diag_down_right = []
    diag_up_right = []
    diag_down_left = []
    diag_up_right = []

    for d in range(-rows + 1, cols):
        diag_down_right.append("".join(crossword[r][r - d] for r in range(rows) if 0 <= r - d < cols))
        diag_up_right.append("".join(crossword[r][d + r] for r in range(rows) if 0 <= d + r < cols))

    diag_down_left = []
    diag_up_left = []

    for d in range(-rows + 1, cols):
        diag_down_left.append("".join(crossword[r][cols - 1 - r - d] for r in range(rows) if 0 <= cols - 1 - r - d < cols))
        diag_up_left.append("".join(crossword[rows - 1 - r][d + r] for r in range(rows) if 0 <= d + r < cols))

    all_lines = horizontal + vertical + diag_down_right + diag_up_right + diag_down_left + diag_up_left

    all_lines += [line[::-1] for line in all_lines]

    count = sum(line.count('XMAS') for line in all_lines)
    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("fuck you")
         sys.exit(1)

    input_filename = sys.argv[1] 

    crossword = []

    with open(input_filename, 'r') as file:
        for line in file: 
            crossword.append(line) 

    print(solve_crossword(crossword))

       
