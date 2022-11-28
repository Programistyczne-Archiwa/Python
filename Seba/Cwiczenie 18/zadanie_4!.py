# Zadanie 4 X
print("Zadanie 4")
text = "asdasdas"
for char in text:
  for i in range(1, text.count(char)):
    print(char, end="") 
    print(text.find(char, i))