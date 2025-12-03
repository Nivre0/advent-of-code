file = "input.txt"
print("using input:", file)

with open(file, 'r') as file:
    lines = file.read().splitlines()

def checkIfNice(s):
    double = False
    notContains = True

    vowelCount = 0
    lastChar = ''

    for c in list(s):
        # Could use Regex
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowelCount += 1
        
        if c == lastChar:
            double = True
        
        x = lastChar + c
        if x == "ab" or x == "cd" or x == "pq" or x == "xy":
            notContains = False
            
        lastChar = c

    print(s)
    print("Double: " + str(double) + ", notContains: " + str(notContains) + ", vowels: " + str(vowelCount)) 

    if double and notContains and vowelCount >= 3:
        return True
    return False

count = 0

for line in lines:
    if checkIfNice(line):
        count += 1

print(count)