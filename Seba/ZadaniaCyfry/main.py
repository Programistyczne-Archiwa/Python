file = open("cyfry.txt", "r")
numbers = file.read().splitlines()

# a)
count = 0
for number in numbers:
    if int(number) % 2 == 0:
        count += 1
print(f"Liczb parzystych jest {count}")

# b)
def sum_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum
max = 0
min = 0
for number in numbers:
    if sum_digits(int(number)) > sum_digits(max):
        max = number
    if sum_digits(int(number)) < sum_digits(min) or min == 0:
        min = number
print(f"min: {min}\nmax: {max}")

# c)
for number in numbers:
    isAscending = True
    for idx in range(0, len(number) - 1):
        if number[idx] > number[idx + 1]:
            isAscending = False
    if isAscending == True:
        print(number)