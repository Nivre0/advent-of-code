file = "exa.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

def check(line):
    split = line.split(" ")
    for i in range(0, len(split)):
        split[i] = int(split[i])
    isSafe = True
    direction = False
    if split[0] - split[1] > 0:
        direction = True

    for i in range(1, len(split)):
        value = (split[i - 1] - split[i])
        if value < 0:
            value = value * -1

        if direction and split[i - 1] < split[i]:
            isSafe = False
        elif not direction and split[i - 1] > split[i]:
            isSafe = False
        if value < 4 and value > 0:
            continue
        else:
            isSafe = False
        
    return isSafe

count = 0

for line in lines:
    if check(line):
        count += 1

print("Result:", count)
            

