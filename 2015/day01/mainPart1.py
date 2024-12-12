file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read()

floor = 0
for b in content:
    if b == "(":
        floor += 1
    else:
        floor -= 1

print("Result:", floor)