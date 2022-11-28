# Zadanie 19
print("Zadanie 19")
text = "asdasdasdasd"
text = [*text]
lastA = -1
if text[0] == "a":
    lastA = 0
for i in range(1, len(text)):
    if text[i] == "a":
        temp = text[lastA + 1]
        text[lastA + 1] = text[i]
        text[i] = temp
        lastA = lastA + 1
print(text)