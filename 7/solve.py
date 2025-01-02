import sys

def solve_ops(equations):
    # just gonna solve it brute force first
    total = 0
    for eq in equations:
        truth = eq[0]
        args = eq[1:]

        solutions = [args[0]]
        for i in range(1, len(args)):
            new_solutions = []
            digits = len(str(args[i]))
            for j in range(len(solutions)):
                new_solutions.append(solutions[j] + args[i])
                new_solutions.append(solutions[j] * args[i])
                cc = int(str(solutions[j]) + str(args[i]))
                new_solutions.append(cc)

            solutions = new_solutions
        if truth in solutions:
            total += truth

    return total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("fuck you")
        sys.exit(1)

    input_filename = sys.argv[1]

    try:
        inputs = []
        with open(input_filename, 'r') as file:
            for line in file:
                split_line = line.split()
                inputs.append(list(map(int, [split_line[0][:-1]] + split_line[1:])))

        print(solve_ops(inputs))
    except FileNotFoundError:
        print(f"fuck you, file '{input_filename}' not found.")
        sys.exit(1)

