f = open("hasla.txt", "r")

lines = f.readlines()
i = 0
hasla = []
for haslo in lines:
    for j in range(len(haslo)):
        try:
            if ord(haslo[j]) + ord(haslo[j+1]) == 220:
                hasla.append(haslo)
                break
        except IndexError:
            continue

print(hasla)