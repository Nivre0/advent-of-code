file = "input.txt"
print("Using input:", file)

with open(file, 'r') as file:
    grid = file.read().splitlines()

ROWS, COLS = len(grid), len(grid[0])

def isXMAS(grid, r, c):
    if r - 1 < 0 or r + 1 >= ROWS or c - 1 < 0 or c + 1 >= COLS:
        return False
    
    d1 = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
    d2 = grid[r + 1][c - 1] + grid[r][c] + grid[r - 1][c + 1]
    
    valid_diagonal = {"MAS", "SAM"}
    return d1 in valid_diagonal and d2 in valid_diagonal

def countXMAS(grid):
    count = 0
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if isXMAS(grid, r, c):
                count += 1
    return count

result = countXMAS(grid)

print("Result:", result)
