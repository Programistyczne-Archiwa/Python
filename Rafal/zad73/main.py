f = open("tekst.txt","r")
words = f.read().split(" ")
# 73.1
count = 0
for word in words:
    for letter in word:
        try:
            # rint(letter, word[word.index(letter)+1])
            if letter == word[word.index(letter)+1]:
                count += 1
                break
        except IndexError:
            count = count
print(count)

# 73.2

alf = {"A":0, "B":0, "C":0, "D":0,  "E":0,  "F":0,  "G":0,  "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "R":0, "S":0, "T":0, "Q":0, "U":0, "W":0, "V":0, "X":0, "Y":0, "Z":0}
percent = {"A":0, "B":0, "C":0, "D":0,  "E":0,  "F":0,  "G":0,  "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "R":0, "S":0, "T":0, "Q":0, "U":0, "W":0, "V":0, "X":0, "Y":0, "Z":0}
length = len(words)
for word in words:
    for letter in word:
        if letter == '\n':
            pass
        else:
            alf[f"{letter}"] += 1
for i in percent:
    percent[f"{i}"] = (alf[f"{i}"] / length)

print(alf)
print(percent)
