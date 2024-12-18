file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read().splitlines()

def checkBorder(table, x, y, orientation):
    if orientation == "^" and y == 0:
        return True
    elif orientation == "v" and y == len(table) - 1:
        return True
    if orientation == "<" and x == 0:
        return True
    elif orientation == ">" and x == len(table[0]) - 1:
        return True
    else:
        return False

def turn(orientation):
    if orientation == "^":
        return ">"
    elif orientation == "v":
        return "<"
    if orientation == "<":
        return "^"
    elif orientation == ">":
        return "v"

def simulate_guard(table, start_x, start_y, start_orientation):
    x, y, orientation = start_x, start_y, start_orientation
    visited_states = set()

    while True:
        state = (x, y, orientation)
        if state in visited_states:
            return True  
        visited_states.add(state)

        if checkBorder(table, x, y, orientation):
            return False  

        if orientation == "^" and not table[y - 1][x] == "#":
            y -= 1
        elif orientation == "v" and not table[y + 1][x] == "#":
            y += 1
        elif orientation == "<" and not table[y][x - 1] == "#":
            x -= 1
        elif orientation == ">" and not table[y][x + 1] == "#":
            x += 1
        else:
            orientation = turn(orientation)

table = []
start_x = start_y = 0
start_orientation = "^"

for i, line in enumerate(content):
    table.append(list(line))
    for j, char in enumerate(line):
        if char == "^":
            start_x = j
            start_y = i

possible_positions = set()
for i in range(len(table)):
    for j in range(len(table[0])):
        if table[i][j] == "." and (j != start_x or i != start_y):
            table[i][j] = "#" 
            if simulate_guard(table, start_x, start_y, start_orientation):
                possible_positions.add((j, i))
            table[i][j] = "."  

print("Result:", len(possible_positions))
