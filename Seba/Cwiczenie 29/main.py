# Zadanie 2
print("Zadanie 2")
file = open("test.txt", "r")
file_content = file.read()
print(file_content)
file.close()

# Zadanie 3
print("\nZadanie 3")
file = open("test.txt", "r")
file_content_lines = file.readlines()
print(file_content_lines[0:8])
file.close()

# Zadanie 4
print("\nZadanie 4")  
file = open("test.txt", "r")
file_content_lines = file.readlines()
print(file_content_lines[0:-8])
file.close()

# Zadanie 5
print("\nZadanie 5")
file = open("test.txt", "a")
file.write("\nAutor: Jan Kowalski")
file.close()

# Zadanie 6
print("\nZadanie 6")
file = open("test.txt", "r")
file_content_lines = file.readlines()
print(file_content)
file.close()

# Zadanie 7
print("\nZadanie 7")
file = open("test.txt", "r")
file_content = "".join(file.readlines())
print(file_content)
file.close()

# Zadanie 8
print("\nZadanie 8")
file = open("test.txt", "r")
words = file.read().split()
print(max(words))
file.close()

# Zadanie 9
print("\nZadanie 9")
file = open("test.txt", "r")
file_lines = file.readlines()
print(len(file_lines))

# Zadanie 10
print("\nZadanie 10")
file = open("test.txt", "r")
words = file.read().split()
print(len(words))

# Zadanie 11
print("\nZadanie 11")
file = open("test.txt", "r")
chars = list(file.read())
print(chars)

# Zadanie 12
print("\nZadanie 12")
file = open("test.txt", "r")
new_file = open("test_copy.txt", "w")
new_file.write(file.read())

# Zadanie 13
print("\nZadanie 13")
file = open("test.txt", "r")
file_content_lines = file.readlines()
for idx, file_content_line in enumerate(file_content_lines):
    if idx % 2 == 0:
        print(file_content_line)
file.close()