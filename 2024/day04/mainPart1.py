file = "input.txt"
print("Using input:", file)

with open(file, 'r') as file:
    content = file.read().splitlines()

def flipVertical(content):
    new = []
    for col in range(len(content[0])):
        new.append("".join(row[col] for row in content))
    return new

def getDiagonalsBLTR(content):
    rows, cols = len(content), len(content[0])
    diagonals = []
    for k in range(-(rows - 1), cols):  
        diagonal = [content[i][i - k] for i in range(rows) if 0 <= i - k < cols]
        diagonals.append("".join(diagonal))
    return diagonals

def getDiagonalsTLBR(content):
    rows, cols = len(content), len(content[0])
    diagonals = []
    for k in range(rows + cols - 1): 
        diagonal = [content[i][k - i] for i in range(rows) if 0 <= k - i < cols]
        diagonals.append("".join(diagonal))
    return diagonals

def countOccurrences(line):
    return line.count("XMAS") + line.count("SAMX")

def horizontal(content):
    return sum(countOccurrences(line) for line in content)

def vertical(content):
    return sum(countOccurrences(line) for line in flipVertical(content))

def diagonal1(content):
    return sum(countOccurrences(line) for line in getDiagonalsBLTR(content))

def diagonal2(content):
    return sum(countOccurrences(line) for line in getDiagonalsTLBR(content))

result = horizontal(content) + vertical(content) + diagonal1(content) + diagonal2(content)

print("Result:", result)
