import sys

def safety_check(reports):
    safe = 0

    for report in reports:
        diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        
        dec = all(-3 <= diff <= -1 for diff in diffs)
        inc = all(1 <= diff <= 3 for diff in diffs)

        safe += 1 if dec or inc else 0

    return safe


if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("fuck you")
         sys.exit(1)

    input_filename = sys.argv[1]
    
    reports = []

    with open(input_filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split(' ')))
            reports.append(report)

    print(safety_check(reports))

       
