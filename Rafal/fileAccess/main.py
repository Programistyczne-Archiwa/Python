
# Zadanie 2

fileread = open("file.txt", "r")

print(fileread.read())
fileread.close()

print()
print()
print()

# Zadanie 3
fileread = open("file.txt", "r")
for i in range(7):
    print(fileread.readlines(8))

fileread.close()
# Zadanie 4
print()
print()
print()
fileread = open("file.txt", "r")

files = fileread.readlines()
print(files[::-8])
fileread.close()
