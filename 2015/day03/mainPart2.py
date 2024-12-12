file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = list(file.read())

houses = set(["0,0"])

x1 = 0
y1 = 0

x2 = 0
y2 = 0

turn = 0

for c in content:
    if turn == 0:
        if c == "<":
            x1 -= 1
        elif c == ">":
            x1 += 1
        elif c == "v":
            y1 -= 1
        else:
            y1 += 1
        turn = 1
        houses.add(str(x1) + "," + str(y1))
    else:
        if c == "<":
            x2 -= 1
        elif c == ">":
            x2 += 1
        elif c == "v":
            y2 -= 1
        else:
            y2 += 1
        turn = 0
        houses.add(str(x2) + "," + str(y2))

print(len(houses))