file = "input.txt"
print("using input:", file)

with open(file, 'r') as f:
    lines = f.read().splitlines()
    position = 50
    count = 0

    for line in lines:
        direction = line[0]
        number = int(line[1:])

        if direction == "R":
            hit_i = (100 - position) % 100
        else:
            hit_i = position % 100

        if 1 <= hit_i <= number:
            count += 1

        if direction == "R":
            position = (position + number) % 100
        else:
            position = (position - number) % 100

    print(count)
