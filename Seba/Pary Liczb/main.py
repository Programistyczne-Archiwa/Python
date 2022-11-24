import math

file = open(r"C:\Users\Egzamin\Documents\Python\Pary Liczb\liczby.txt", "r")
lines = file.readlines()

# a) Ile jest wierszy, w których jedna z występującycjh w nich liczb jest wielokrotnością drugiej?
count = 0
for line in lines:
    numbers = line.split(" ")
    first_num = int(numbers[0])
    second_num = int(numbers[1])
    if first_num % second_num == 0 or second_num % first_num == 0:
        count += 1
print(f"Wierszy, w których jedna z liczb jest wielokrotnością drugiej jest {count}")

# b) Ile jest wierszy, zawierających parę liczb, które są względnie pierwsze?
count = 0
for line in lines:
    numbers = line.split(" ")
    first_num = int(numbers[0])
    second_num = int(numbers[1])
    if math.gcd(first_num, second_num) == 1:
        count += 1
print(f"Wierszy, w których liczby są względnie pierwsze jest {count}")

# c) Ile jest wierszy, dla których suma cyfr pierwszej liczby jest równa sumie cyfr drugiej liczby?

def sum_digits(num):
    sum = 0
    for char in [*str(num)]:
        sum += int(char)
    return sum

count = 0
for line in lines:
    numbers = line.split(" ")
    first_num = int(numbers[0])
    second_num = int(numbers[1])
    if sum_digits(first_num) == sum_digits(second_num):
        count += 1
print(f"Wierszy, w których suma cyfr pierwszej liczby jest równa sumie cyfr drugiej liczby jest {count}")
    