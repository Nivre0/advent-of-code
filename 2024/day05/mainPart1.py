file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read().splitlines()

lists = [list(map(int, line.split(','))) for line in [line for line in content if ',' in line]]
pairs = [list(map(int, line.split('|'))) for line in [line for line in content if '|' in line]]

rules = {}

for pair in pairs:
    if pair[0] in rules:
        rules[pair[0]].append(pair[1])
    else:
        rules[pair[0]] = [pair[1]]

def is_valid_update(update):
    update_set = set(update)
    for x in update:
        if x in rules:
            for y in rules[x]:
                if y in update_set and update.index(x) > update.index(y):
                    return False  
    return True

result = 0

for update in lists:
    if is_valid_update(update):
        middle_page = update[len(update) // 2]
        result += middle_page

print("Result:", result)
