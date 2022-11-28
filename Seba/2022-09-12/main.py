# Zadanie 1

isValid = False
while isValid is False:
  a = int(input())

  if a > 0:
    isValid = True

# Zadanie 2

x = 0
y = 5
sum = 0
for i in range(x,y+1):
  if i % 2 == 1:
    sum += i
print(f"Suma: {sum}")