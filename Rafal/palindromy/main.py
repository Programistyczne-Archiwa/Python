f = open("C:/Users/uczeń/Desktop/hasla.txt", "r")

files = f.read().splitlines()

licznik = 0
np = 0
p = 0
for haslo in files:
    if len(haslo) % 2 != 0:
        np += 1
    else:
        p += 1

    if haslo[::-1] == haslo:
        licznik += 1
        print(f"Palindrom nr {licznik}: {haslo}")

print(f"Liczba parzystych: {p}")
print(f"Liczba nieparzystych: {np}")

