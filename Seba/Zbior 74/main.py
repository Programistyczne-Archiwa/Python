# 74.1.
# Podaj liczbę haseł złożonych jedynie ze znaków numerycznych, tzn. cyfr od 0 do 9. 

file = open("hasla.txt", "r")
lines = file.read().splitlines()

counter = 0
for line in lines:
    if line.isdigit():
        counter += 1

print(counter)

# 74.2.
# Wypisz hasła, które zostały użyte przez co najmniej dwóch różnych użytkowników, tzn. występujące w dwóch różnych wierszach. Hasła wypisz (bez powtórzeń) w kolejności leksykograficznej. 

passwords = []
for line in lines:
    if lines.count(line) > 1:
        passwords.append(line)

passwords = list(set(passwords))
passwords.sort()
print(passwords)

# 74.3.
# Podaj liczbę użytkowników posiadających hasła, w których występuje fragment złożony
# z czterech kolejnych znaków ASCII (w dowolnej kolejności). 

def check(string):
    string = list(set(string))
    string.sort()
    print(string)
    if ord(string[0]) == ord(string[1]) - 1 == ord(string[2]) - 2 == ord(string[3]) - 3:
        return True
    return False

counter = 0
for line in lines:
    if len(line) >= 4:
        break
    for i in range(len(line) - 3):
        if check(line[i:i+4]):
            counter += 1
            break
print(counter)