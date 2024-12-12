def is_safe(report):
    deltas = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    return all(1 <= delta <= 3 for delta in deltas) and (
        all(report[i] < report[i + 1] for i in range(len(report) - 1)) or
        all(report[i] > report[i + 1] for i in range(len(report) - 1))
    )

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def analyze_reports(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')

    reports = [list(map(int, line.split())) for line in data]

    # Count reports that are safe with the dampener
    safe_reports_with_dampener = sum(is_safe_with_dampener(report) for report in reports)
    return safe_reports_with_dampener

result = analyze_reports("input.txt")
print(f"Result: {result}")