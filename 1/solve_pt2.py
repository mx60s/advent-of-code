import sys

def get_sim_score(list1, list2):
    list1_d, list2_d = {}, {}

    for l1, l2 in zip(list1, list2):
        list1_d[l1] = list1_d[l1] + 1 if l1 in list1_d else 1
        list2_d[l2] = list2_d[l2] + 1 if l2 in list2_d else 1

    total = 0

    for i, l1_count in list1_d.items():
        if i in list2_d:
            total += i * l1_count * list2_d[i]

    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("fuck you")
         sys.exit(1)

    input_filename = sys.argv[1]
    
    list1, list2 = [], []

    with open(input_filename, 'r') as file:
        for line in file:
            parts = line.split('   ')
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))
    
    print(get_sim_score(list1, list2))

       
