file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()