# Zadanie 7
print("Zadanie 7")
text = "Tak siema ty panie kowalski"
text = text.split(" ")
longestWord = ["", 0]
for sentence in text:
  if len(sentence) > longestWord[1]:
    longestWord[0], longestWord[1] = sentence, len(sentence)
print(longestWord)