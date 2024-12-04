import sys
import re

def unjumble_regex(instructs):
    total = 0
    
    pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    matches = [match.start() for match in re.finditer(pattern, instructs)] 

    do_pattern = r'do\(\)'
    do_matches = [match.end() for match in re.finditer(do_pattern, instructs)]
    dont_pattern = r'don\'t\(\)'
    dont_matches = [match.end() for match in re.finditer(dont_pattern, instructs)]

    cmds = []
    cmds += [(match, 'mul') for match in matches]
    cmds += [(do, 'do') for do in do_matches]
    cmds += [(dont, 'dont') for dont in dont_matches]
    cmds.sort()

    do = True

    for idx, cmd in cmds:
        if cmd == 'do':
            do = True
        elif cmd == 'dont':
            do = False
        elif cmd == 'mul':
            if do:
                match = re.findall(pattern, instructs[idx:idx+13])[0]
                total += int(match[0]) * int(match[1])
        
    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("fuck you")
         sys.exit(1)

    input_filename = sys.argv[1] 

    instructs = ''

    with open(input_filename, 'r') as file:
        for line in file: 
            instructs = instructs + line 

    print(unjumble_regex(instructs))

       
