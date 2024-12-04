import sys

def get_dist(list1, list2):
    total = 0

    list1.sort()
    list2.sort()

    for entry1, entry2 in zip(list1, list2):
        total += abs(entry1 - entry2)
        
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
    
    print(get_dist(list1, list2))

       
