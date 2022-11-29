# Zadanie 1

f = open("cyfry.txt", "r")
lines = f.read().splitlines()
print(lines)
licznik = 0
for i in lines:
    if int(i) % 2 == 0:
        licznik += 1
print(f"W pliku znajduje sie {licznik} cyfr parzystych")

# Zadanie 2

najw = 0
najm = 999999999
def sum_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

for i in lines:
    if sum_digits(int(i)) > sum_digits(int(najw)):
        najw = i
    if sum_digits(int(i)) < sum_digits(int(najm)):
        najm = i
print(najw)
print(najm)

print()
print()

for a in lines:
    isAsc = True
    for index in range(0, len(a) -1 ):
        if a[index] > a[index+1]:
            isAsc = False
    if isAsc == True:
        print(a)


