# Palindrom
word = "kajak"
if word == word[::-1]:
    print(f"Słowo {word} jest palindromem")
else:
    print(f"Słowo {word} nie jest palindromem")

# Podawanie liczb podzielnych przez 10 jak nie będzie przez 10 to liczy srednia z tych liczb przez 10
numbers = []
while True:
    a = int(input("Podaj liczbe (podzielna przez 10, inne liczby kończą program): "))
    if a % 10 == 0:
        numbers.append(a)
    else:
        break
print(f"Podane liczby: {numbers}")
print(f"Średnia z liczb podzielnych przez 10: {sum(numbers)/len(numbers)}")

# Równanie s(3) = 1/3 + 1/3*6 + 1/3*6*9
a = 3
sum = 0
for x in range(0, a + 1):
    num = 1
    for y in range(x):
        num *= (y + 1) * 3
    sum += 1 / num
print(f"Suma wyrażenia: {sum}")
