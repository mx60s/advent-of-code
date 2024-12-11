import sys

# make adjacency graph of the rules
# just need to make sure that after you find the first node in the graph, any
# next one which is in the rules graph needs to directly follow

def print_queue(rules, updates):
    pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("fuck you")
        sys.exit(1)

    input_filename = sys.argv[1]

    rules = []
    updates = []

    with open(input_filename, 'r') as file:
       for line in file:
            if '|' not in line:
                parsed = [int(n) for n in line.split(',')]
                updates.append(parsed)
            else:
                parsed = tuple(map(int, line.split('|')))
                rules.append(parsed)

    print(print_queue(rules, updates))

