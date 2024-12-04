import sys


def safety_check(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)

def check_reports(reports):
    safe = 0

    for report in reports:
        if safety_check(report):
            safe += 1
        else:
            for i in range(len(report)):
                fixed = report[:i] + report[i+1:]
                if safety_check(fixed):
                    safe += 1
                    break
    
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

    print(check_reports(reports))

       
