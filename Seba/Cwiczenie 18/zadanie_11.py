# Zadanie 11
print("Zadanie 11")
text = "Lubiee programować w Pythoniee"
for sentence in text.split(' '):
    if len(sentence) % 3 == 0:
        print(sentence[::-1], end=" ")
    else:
        print(sentence, end=" ")
