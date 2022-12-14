file = open("napisy.txt", "r")
texts = file.read().splitlines()

# a)
count = 0
for text in texts:
    if len(text) % 2 == 0:
        count += 1
print("a)", count)

# b)
count = {"0": 0, "1": 0}
sameCount = 0
for text in texts:
    for letter in text:
        if letter == "0": count["0"] += 1
        else: count["1"] += 1
    if count["0"] == count["1"]:
        sameCount += 1
    count["0"], count["1"] = 0, 0
print("b)", sameCount)

# c)
for text in texts:
    if "0" not in text:
        count["1"] += 1
    elif "1" not in text:
        count["0"] += 1
print("c)", count)
#seba nie zdasz egzaminu na prawko huehuebeuehheuueheuhe
# d)
count = {}
for i in range(1, 17):
    count[str(i)] = 0
    for text in texts:
        if len(text) == i:
            count[str(i)] += 1
print("d)", count)