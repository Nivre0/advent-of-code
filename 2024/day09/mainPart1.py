file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read()

newFormat = []

counter = 0

for i, char in enumerate(content):
    if i % 2 == 0: 
        newFormat.append(str(counter) * int(char))
        counter += 1
    else:  
        newFormat.append("." * int(char))

newFormat = list(''.join(newFormat))

optimized = []

while len(newFormat) > 0:
    value = newFormat.pop(0)
    if not value == ".":
        optimized.append(value)
    else:
        while newFormat:
            last = newFormat.pop()
            if not last == ".":
                optimized.append(last)
                break
        
checksum = sum(i * int(block) for i, block in enumerate(optimized) if block != ".")

print(checksum)
    