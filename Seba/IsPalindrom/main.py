file = open("hasla.txt", "r")
passwords = file.read().splitlines()
count = 0

for password in passwords:
    if password == password[::-1]:
        count += 1
        print(f"{count}: {password}")

odd_count = 0
even_count = 0
for password in passwords:
    if len(password) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even: {even_count}, Odd: {odd_count}")