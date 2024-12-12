file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

left = []
right = []

for line in lines:
    split = line.split(" ")
    left.append(int(split[0]))
    right.append(int(split[len(split) - 1]))

left.sort()
right.sort()

count = 0

for i in range(0, len(lines)):
    if left[i] > right[i]:
        count += left[i] - right[i]
    else:
        count += right[i] - left[i]

print("result:", count)