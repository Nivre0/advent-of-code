file = "example.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read().splitlines()

table = []
antennas = set([])

for i in range(0, len(content)):
    listed = list(content[i])
    table.append(listed)
    for j in range(0, len(listed)):
        antennas.add(listed[j])
    antennas.remove(".")

print(antennas)

