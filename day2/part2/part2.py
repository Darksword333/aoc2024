with open("/workspaces/aoc2024/day2/input.txt", "r") as f:
    input = f.read().strip().split("\n")

def is_safe(levels):
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    valid_diff = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    return (is_increasing or is_decreasing) and valid_diff

def main(input):
    safe_count = 0
    
    for report in input:
        levels = list(map(int, report.split()))
        
        if is_safe(levels):
            safe_count += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if is_safe(new_levels):
                    safe_count += 1
                    break
    
    return safe_count

print(main(input))