f = open("hasla.txt","r")
lines = f.read().splitlines()

# ZADANIE 1
count = 0
for line in lines:
    numberOnly = False
    try:
        line = int(line)
        count+=1
    except:
        count = count

print(count)

# Zadanie 2


for line in lines:
    r = lines.count(line)
    if r>=2:
        print(line)
        del lines[lines.index(line)]
print("********************************************************")
# Zadanie 3

for line in lines:
    conditions = False
    if any(letter.isdigit() for letter in line) and any(letter.isupper() for letter in line) and any(letter.islower() for letter in line):
        conditions = True
    else:
        conditions = False
    if conditions:
        print(line)