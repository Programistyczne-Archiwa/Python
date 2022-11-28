import math

# Zadanie 1
print("Zadanie 1")
a = 10
if a < 0:
    a * -1
print(a)

# Zadanie 2
print("\nZadanie 2")
a = 10
if a > 0:
    print("Wieksza od 0")
elif a < 0:
    print("Mniejsza od 0")
else:
    print("Równa 0")

# Zadanie 3
print("\nZadanie 3")
a = 10
if a % 2 == 0:
    print("Parzysta")
else:
    print("Nieparzysta")

# Zadanie 4
print("\nZadanie 4")
a = 2
b = 1
c = 5
if a < b:
    if a < c:
        print(f"Liczba a jest najmniejsza ({a})")
    elif c < a:
        print(f"Liczba c jest najmniejsza ({c})")
elif c < b:
    print(f"Liczba c jest najmniejsza ({c})")
else:
    print(f"Liczba b jest najmniejsza ({b})")

# Zadanie 5
print("\nZadanie 5")
a = 5
b = 5
c = 2
if a == b or a == c or c == b:
    print("Dwie takie same liczby")

# Zadanie 6
print("\nZadanie 6")
a = 2
b = 3
c = 4
if a < b < c:
    print("Są ustawione w porządku rosnącym")

# Zadanie 7
print("\nZadanie 7")
a = 18
if a >= 17 and a <= 21:
    print("Jest w przedziale")

# Zadanie 8
print("\nZadanie 8")
a = 10
b = 8
c = 15
if a + b > c and b + c > a and a + c > b:
    print("Z tych boków można stowrzyć trójkąt")

# Zadanie 9
print("\nZadanie 9")
a = 2
b = -4
c = 2
delta = (b**2) - (4 * a * c)
if delta > 0:
    print(f"x1 = {(-b-math.sqrt(delta))/(2 * a)}")
    print(f"x2 = {(-b+math.sqrt(delta))/(2 * a)}")
elif delta == 0:
    print(f"x1 = {-b/(2 * a)}")
else:
    print("Brak pierwiastków")

# Zadanie 10
print("\nZadanie 10")
a = 5
b = 10
if a % b == 0:
    print("Liczba b jest wielokrotnością liczby a")
elif b % a == 0:
    print("Liczba a jest wielokrotnością liczby b")

# Zadanie 11
print("\nZadanie 11")
day = 30
month = 5
year = 2010
if day < 1 or day > 31 or day is None:
    exit()
elif month < 1 or month > 12 or month is None:
    exit()
elif year < 1900 or year > 2050 or year is None:
    exit()
print(f"{day}.{month}.{year}")
