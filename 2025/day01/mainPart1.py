file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()
    position = 50
    count = 0

    for line in lines:
        direction = line[0]
        number = int(line[1:])
        
        while number > 99:
            number -= 100
        
        if direction == "R":
            position += number
        else:
            position -= number

        while position > 99:
            position -= 100
        
        while position < 0:
            position += 100

        if position == 0:
            count += 1

    print(count)
