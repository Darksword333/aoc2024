with open("/workspaces/aoc2024/day2/input.txt", "r") as f:
    input = f.read().strip().split("\n")

def main(input):
    safe_count = 0
    
    for report in input:
        levels = list(map(int, report.split()))
        
        is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
        is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
        
        valid_diff = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
        
        if (is_increasing or is_decreasing) and valid_diff:
            safe_count += 1
    
    return safe_count

print(main(input))