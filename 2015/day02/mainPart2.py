file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

result = 0

for line in lines:
    nums = line.split("x")
    for i in range(0, 3):
        nums[i] = int(nums[i])
    nums.sort()
    result += nums[0] * 2 + nums[1] * 2 + nums[0] * nums[1] * nums[2]

print("Result:", result)
