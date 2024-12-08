import sys
import re

def solve_crossword(crossword):
    word = 'XMAS'

    def check_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= x < rows and 0 <= y < cols) or crossword[nx][ny] != word[i]:
                return False
        return True

    rows, cols = len(crossword), len(crossword[0])
    directions = [
        (0, 1), 
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1
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

       
