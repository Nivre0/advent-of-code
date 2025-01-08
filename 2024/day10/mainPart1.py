file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read()

def is_valid_step(current_height, next_height):
    return next_height == current_height + 1

def find_score(map_data, start):
    queue = [start]
    visited = set()
    reached_nines = set()

    while queue:
        y, x = queue.pop(0)
        if (y, x) in visited:
            continue
        visited.add((y, x))

        current_height = map_data[y][x]
        if current_height == 9:
            reached_nines.add((y, x))

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(map_data) and 0 <= nx < len(map_data[0]):
                next_height = map_data[ny][nx]
                if is_valid_step(current_height, next_height):
                    queue.append((ny, nx))

    return len(reached_nines)

def sum_trailhead_scores(map_data):
    trailheads = find_trailheads(map_data)
    total_score = 0
    for trailhead in trailheads:
        total_score += find_score(map_data, trailhead)
    return total_score

def find_trailheads(map_data):
    trailheads = []
    for y, row in enumerate(map_data):
        for x, height in enumerate(row):
            if height == 0:
                trailheads.append((y, x))
    return trailheads

table = [list(map(int, line)) for line in content.splitlines()]

total_score = 0

trailheads = []

for y, row in enumerate(table):
    for x, height in enumerate(row):
        if height == 0:
            trailheads.append((y, x))


for trailhead in trailheads:
    total_score += find_score(table, trailhead)

result = sum_trailhead_scores(table)

print(f"Result: {result}")
