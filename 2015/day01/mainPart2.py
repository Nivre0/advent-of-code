file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = list(file.read())
floor = 0
position = 0
for i in range(0, len(content) - 1):
    if content[i] == "(":
        floor += 1
    else: 
        floor -= 1
    
    if floor < 0:
        position = i + 1
        break


print("Result:", position)