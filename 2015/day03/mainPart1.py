file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = list(file.read())

houses = set(["0,0"])
x = 0
y = 0

for c in content:
    if c == "<":
        x -= 1
    elif c == ">":
        x += 1
    elif c == "v":
        y -= 1
    else:
        y += 1
    houses.add(str(x) + "," + str(y))

print(len(houses))