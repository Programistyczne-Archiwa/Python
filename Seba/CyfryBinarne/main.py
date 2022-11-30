# a)

file = open("liczby.txt", "r")
ns = file.read().splitlines()

count = 0
for bin_number in ns:
    count_digit = {"1": 0, "0": 0}
    for bin_digit in str(bin_number):
        if bin_digit == "1":
            count_digit["1"] += 1
        else:
            count_digit["0"] += 1
    count += 1 if count_digit["0"] > count_digit["1"] else 0

print("a) Liczba binarnych liczb, w których liczba zer od liczby jedynek wynosi:", count)

# b)

ns=open("liczby.txt", "r").read().splitlines(); d=0; o=0
for n in ns:
    if n[-1]=="0":d+=1
    if n[-3:]=="000":o+=1
print(d,o)