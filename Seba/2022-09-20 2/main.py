# Zadanie 1
print("Zadanie 1")

def nwd(a, b):
  if a % b == 0:
    return b
  else:
    return nwd(b, a % b)
s = 0
for i in range(1000):
  if nwd(random.randrange(1, 1000000), random.randrange(1, 1000000)) == 1:
    s += 1
print(f"P = {s}/1000 = {s/1000}")