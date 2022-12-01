# a)

def compere_bin_numbers(bin_1, bin_2):
    bin_1 = str(bin_1)
    bin_2 = str(bin_2)
    if len(bin_1) > len(bin_2):
        return {"max": bin_1, "min": bin_2}
    elif len(bin_1) < len(bin_2):
        return {"max": bin_2, "min": bin_1}
    else:
        for i in range(len(bin_1)):
            if bin_1[i] > bin_2[i]:
                return {"max": bin_1, "min": bin_2}
            elif bin_1[i] < bin_2[i]:
                return {"max": bin_2, "min": bin_1}
    return {"max": bin_1, "min": bin_2}

file = open("liczby.txt", "r")
numbers = file.read().splitlines()

max_number = {"number": 0, "idx": 0}
min_number = {"number": 0, "idx": 0}
for idx, number in enumerate(numbers):
    print(number)
    if min_number["number"] == 0:
        min_number["number"] = number
        min_number["idx"] = idx
    elif number == compere_bin_numbers(min_number["number"], number)["min"]:
        min_number["number"] = number
        min_number["idx"] = idx

    if number == compere_bin_numbers(max_number["number"], number)["max"]:
        max_number["number"] = number
        max_number["idx"] = idx

print("Max number:", max_number["number"], " idx:", max_number["idx"] + 1)
print("Min number:", min_number["number"], " idx:", min_number["idx"] + 1)