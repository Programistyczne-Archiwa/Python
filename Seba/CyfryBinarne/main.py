# a)

file = open("liczby.txt", "r")
bin_numbers = file.read().splitlines()

count = 0
for bin_number in bin_numbers:
    count_digit = {"1": 0, "0": 0}
    for bin_digit in str(bin_number):
        if bin_digit == "1":
            count_digit["1"] += 1
        else:
            count_digit["0"] += 1
    count += 1 if count_digit["0"] > count_digit["1"] else 0

print("a) Liczba binarnych liczb, w których liczba zer od liczby jedynek wynosi:", count)

# b)

count = {"2": 0, "8": 0}
for bin_number in bin_numbers:
    if bin_number[-1] == "0":
        count["2"] += 1
    if len(bin_number) > 4:
        if bin_number[-3:] == "000":
            count["8"] += 1

print(f"b) Liczby podzielne przez 2: {count['2']}, liczby podzielne przez 8: {count['8']}")