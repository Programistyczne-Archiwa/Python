import random

# Zadanie 1
print("Zadanie 1")
dict = {"1": "text"}
dict["2"] = "text2"
print(dict)

# Zadanie 2
print("\nZadanie 2")
dict1 = {"1": "text"}
dict2 = {"2": "text"}
dict3 = {"3": "text"}
dict4 = {**dict1, **dict2, **dict3}
print(dict4)

# Zadanie 3
print("\nZadanie 3")
dict = {"1": "text", "2": "text2"}
if "1" in dict:
  print("this key exist in dict")

# Zadanie 4
print("\nZadanie 4")
n = 10
dict = {}
for i in range(0, 10):
  dict[i] = i**2
print(dict)

# Zadanie 5
print("\nZadanie 5")
dict = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
max = 0
for i in range(0, 10):
  if dict[i] > max:
    max = dict[i]
print(max)

# Zadanie 6
print("\nZadanie 6")
dictMax = {}
dictMin = {}
dict = {'produkt0': 41.68, 'produkt1': 12.18, 'produkt2': 74.63, 'produkt3': 98.55, 'produkt4': 91.12, 'produkt5': 64.16, 'produkt6': 95.73, 'produkt7': 23.56, 'produkt8': 4.02, 'produkt9': 45.27}

# Zadanie 7

