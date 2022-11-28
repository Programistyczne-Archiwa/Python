# Zadanie 20
print("Zadanie 20")
text = "asdasdasd asd asda sdas da s"
text = text.split(" ")
for sentence in text:
    for idx, char in enumerate(sentence):
        if idx == 0:
            print(char.upper(), end="")
        elif idx == len(sentence) - 1:
            print(char.upper(), end="")
        else:
            print(char, end="")
    print(end=" ")