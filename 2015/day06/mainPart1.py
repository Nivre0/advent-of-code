file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

# Parse commands
commands = []
for s in lines:
    # turn off = 1
    # turn on  = 2
    # toggle   = 3

    command = []
    split = s.split(' ')
    if len(split) == 5:
        if split[1] == "off":
            command.append(1)
        else:
            command.append(2)
        cords1 = split[2].split(',')
        cords2 = split[4].split(',')
        command.append(cords1)
        command.append(cords2)

    if len(split) == 4:
        command.append(3)
        cords1 = split[1].split(',')
        cords2 = split[3].split(',')
        command.append(cords1)
        command.append(cords2)

    commands.append(command)




# Creating grid
grid = [['x' for _ in range(1000)] for _ in range(1000)]

