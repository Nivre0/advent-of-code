# This is way too slow

import hashlib

file = "example.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read()

print(content)

number = 1

while True:
    content = content + str(number)
    md5_hash = hashlib.md5()
    md5_hash.update(content.encode('utf-8'))
    result = md5_hash.hexdigest()
    if result[:5] == "00000":  
        print(number)
        break
    number += 1

print("no result")

