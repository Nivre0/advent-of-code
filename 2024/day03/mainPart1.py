import re

file = "input.txt"
print("Using input:", file)

with open(file, 'r') as f:
    content = f.read()

result = 0

pattern = r"mul\(\d{1,3},\d{1,3}\)"

valid_mul = re.findall(pattern, content)

for instr in valid_mul:
    numbers = re.findall(r"\d+", instr)
    if len(numbers) == 2:
        x, y = map(int, numbers)
        result += x * y 

print("Result:", result)
