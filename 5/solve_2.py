import sys


def make_rule_graph(rules):
    rule_graph = {}

    for leader, follower in rules:
        if leader in rule_graph:
            rule_graph[leader].append(follower)

    return rule_graph

def print_queue(rules, updates):
    total_count = 0

    for update in updates:
        valid_rules = []
        for leader, follower in rules:
            if leader in update and follower in update:
                valid_rules.append((leader, follower))

        update_idxs = {page: i for i, page in enumerate(update)}
        made_change = True
        invalid_update = False
        while made_change:
            made_change = False
            for leader, follower in valid_rules:
                if update_idxs[leader] > update_idxs[follower]:
                    invalid_update = True
                    made_change = True
                    l_idx = update_idxs[leader]
                    f_idx = update_idxs[follower]
                    update_idxs[leader], update_idxs[follower] = f_idx, l_idx
                    update[l_idx], update[f_idx] = update[f_idx], update[l_idx]
                    
        if invalid_update:
            total_count += update[len(update) // 2]
                
    return total_count

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

