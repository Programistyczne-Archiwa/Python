file = open("passwords.txt", "r")
passwords = file.read().splitlines()

def check(string):
    string = sorted([*string])
    for i in range(1, len(string)):
        if ord(string[i - 1]) != ord(string[i]) - 1:
            return False
    return True

count = 0
for password in passwords:
    for i in range(0, len(password) - 3):
        if check(password[i:i + 4]):
            count += 1
            break
print(count)