import math

file = open("ulamki.txt", "r")
numbers = file.read().splitlines()

# a) Liczba ulamkow, ktora jest skracalna

count = 0
for number in numbers:
    meter = number.split(" ")[0]
    denominator = number.split(" ")[1]

    if math.gcd(int(meter), int(denominator)) > 1:
        count += 1

print("Liczba ulamkow, która jest skracalna:", count)

# b) Cyfry wystepujace w liczniku i mianowniku

digits = {}

for number in numbers:
    meter = number.split(" ")[0]
    denominator = number.split(" ")[1]

    for digit in meter:
        if digit in digits:
            digits[digit] += 1
        else:
            digits[digit] = 1

    for digit in denominator:
        if digit in digits:
            digits[digit] += 1
        else:
            digits[digit] = 1
        
print("Cyfry występujące w liczniku i mianowniku:", digits)
    