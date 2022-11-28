print("Zadanie 12")
text = "Lubie programować w Pythonie"
text = [*text]
for char in sorted(text, key=str.lower):
    if char != " ":
        print(char, end="")