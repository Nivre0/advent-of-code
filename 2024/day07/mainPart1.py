from itertools import product

file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

result = 0

for line in lines:
    testValue = int(line.split(":")[0])
    nums = list(map(int, line.split(":")[1].strip().split()))

    operatorCombinations = list(product(["+", "*"], repeat=len(nums) - 1))

    for operators in operatorCombinations:
        value = nums[0]
        for i in range(len(operators)):
            if operators[i] == "+":
                value += nums[i + 1]
            elif operators[i] == "*":
                value *= nums[i + 1]

    
        if value == testValue:
            result += testValue
            break 

print("Result:", result)
