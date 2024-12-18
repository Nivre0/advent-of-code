file = "example.txt"
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
    
table = []

for line in content:
    table.append(list(line))

x = 0
y = 0
orientation = "^"

for i in range(0, len(table)):
    for j in range(0, len(table[0])):
        test = table[i][j]
        if aable[i][j] == '^':
            x = j
            y = i

positions = set([])

while True:
    positions.add(str(x) + "," + str(y))

    if checkBorder(table, x, y, orientation):
        break
    if orientation == "^" and not table[y - 1][x] == "#":
        y -= 1
    elif orientation == "v" and not table[y + 1][x] == "#":
        y += 1
    elif orientation == "<" and not table[y ][x - 1] == "#":
        x -= 1
    elif orientation == ">" and not table[y][x + 1] == "#":
        x += 1
    else:
        orientation = turn(orientation)
    

print(len(positions))
    