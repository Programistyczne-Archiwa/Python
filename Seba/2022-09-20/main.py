import random, math

# Zadanie 1
print("Zadanie 1")
max = 0
min = 100
for i in range(10):
  random_num = random.randrange(20, 100)
  if random_num > max:
    max = random_num
  if min == 100 or min > random_num:
    min = random_num
  print(f"Random: {random_num}, max: {max}, min:{min}")

# Zadanie 2
print("\nZadanie 2")
random_num = random.randrange(1, 1000)
print(random_num)
a = 0
while a != random_num:
  a = int(input())
  if a > random_num:
    print("Za duża")
  elif a < random_num:
    print("Za mała")

# Zadanie 3
print("\nZadanie 3")
s = 0
for i in range(1000):
  if math.gcd(random.randrange(1, 1000000), random.randrange(1, 1000000)) == 1:
    s += 1
print(f"P = {s}/1000 = {s/1000 * 100}")
