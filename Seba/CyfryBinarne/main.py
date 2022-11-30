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