file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

def get_joltage(input):
    input_list = list(input)

    first = 0
    first_index = -1

    last = 0

    for i in range(0, len(input_list)):
        item = int(input_list[i])
        if item > first and i < len(input_list) - 1:
            first = item
            input_list[i] = 0
            first_index = i

    for i in range(first_index, len(input_list)):
        item = int(input_list[i])
        if item > last :
            last = item
            input_list[i] = 0

    return int(str(first) + str(last))

total = 0

for line in lines:
    total += get_joltage(line)

print(total)