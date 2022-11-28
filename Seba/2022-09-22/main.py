# Zadanie 1
print("Zadanie 1")
def wielokrotnosc(num):
  arr = []
  for i in range(0, num):
    arr.append((i + 1) * 3)
  return arr
print(wielokrotnosc(5))

# Zadanie 2
print("\nZadanie 2")
def parzyste(x, y):
  arr = []
  for i in range(x, y):
    if i % 2 == 0 and i != 0:
      arr.append(i)
  return arr
print(parzyste(0, 5))

# Zadanie 3
print("\nZadanie 3")
def nieparzyste(x, y):
  arr = []
  for i in range(x, y):
    if i % 2 == 1:
      arr.append(i)
  arr.sort(reverse=True)
  return arr
print(nieparzyste(0, 5))

# Zadanie 4
print("\nZadanie 4")
def kwadraty(n):
  if n == 1:
    return []
  else:
    arr = []
    for i in range(1, n + 1):
      arr.append(i**2)
    return arr
print(kwadraty(5))

# Zadanie 5
print("\nZadanie 5")
def dzielniki(n):
  arr = []
  for i in range(1, n + 1):
    if n % i == 0:
      arr.append(i)
  return arr
print(dzielniki(15))
