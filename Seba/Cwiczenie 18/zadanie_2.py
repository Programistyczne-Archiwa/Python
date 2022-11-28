# Zadanie 2 X
print("Zadanie 2")
text = "asdasda"
for char in text:
  if text.count(char) != 0:
    print(text.count(char))
  text = text.replace(char, '')