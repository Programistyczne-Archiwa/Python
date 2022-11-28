# Zadanie 1
print("Zadanie 1")
k = 5
x = 50
y = 100

for i in range(x, y):
  if i % k == 0:
    print(f"{i}")

# Zadanie 2
print("\nZadanie 2")
x = 5
for i in range(x, 0, -1):
  if i % 2 == 0:
    print(f"{i}")

# Zadanie 3
print("\nZadanie 3")
n = 2
for i in range(1, n + 1):
  print(i ** 2)

# Zadanie 4
print("\nZadanie 4")
sum = 0
n = 5
for i in range(1, n + 1):
  sum += i
print(f"Suma liczb: {sum}")