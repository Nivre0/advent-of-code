import re

# File input
file = "input.txt"
print("Using input:", file)

with open(file, 'r') as f:
    content = f.read()

enabled = True 
result = 0

instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", content)

for instr in instructions:
    if instr == "do()":
        enabled = True 
    elif instr == "don't()":
        enabled = False  
    elif "mul" in instr and enabled:
        numbers = re.findall(r"\d+", instr)
        if len(numbers) == 2:
            x, y = map(int, numbers)  
            result += x * y 

print("Result:", result)
