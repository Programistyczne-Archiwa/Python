# Zadanie 1
a = 5
b = 10
if a > b:
  a, b = b, a
for i in range(a, b + 1):
  print(i, end=" ")
for i in range(b, a - 1, -1):
  print(i, end=" ")

# Zadanie 2
print("\nZadanie 2")
a = 5
square = 2
while square ** 2 < a:
  square = square ** 2
  print(square)

# Zadanie 3
print("\nZadanie 3")
a = 5
b = 6
xp = 10
xk = 15
for i in range(xp, xk):
  print(f"{a} * {i} + {b} = {(a*i)+b}")

# Zadanie 4
print("\nZadanie 4")
a = 5
silnia = 1
for i in range(1, a+1):
  silnia *= i
print(f"Silnia: {silnia}")

# Zadanie 5
print("\nZadanie 5")
a = [i for i in range(5, 0, -1)]
sum = 0
for i in a:
  sum += i
print(f"Srednia: {sum / len(a)}")

# Zadanie 6
print("\nZadanie 6")
x = 5
y = 2
if y > 0 < x:
  print(x ** y)

# Zadanie 7
print("\nZadanie 7")
a = 60
square = 3
while square < a:
  square = square * 3
  print(square)

