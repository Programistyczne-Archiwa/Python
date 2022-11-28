# Zadanie 9
print("Zadanie 9")
text = "Tak siema ty panie kowalski"
for idx, char in enumerate(text):
  if idx % 2 == 1:
    text = text.replace(char, "", 1)
print(text)