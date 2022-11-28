file = open("hasla.txt", "r")

passwords = file.read().splitlines()

for password in passwords:
    for idx in range(1, len(password)):
        if ord(password[idx]) + ord(password[idx - 1]) == 220:
            print(password)
            break
        