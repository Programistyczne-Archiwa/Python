# Zadanie 1

print("Zadanie 1")
def oblicz_pole_trojkata(a, h):
  return (a * h) / 2
print(oblicz_pole_trojkata(2, 5))

# Zadanie 2

print("\nZadanie 2")
def oblicz_cene_brutto(netto):
  return netto + (netto * 0.22)
print(oblicz_cene_brutto(200))

# Zadanie 3

print("\nZadanie 3")
def wyswietl_nazwisko(nazwisko):
  for i in range(0, len([*nazwisko])):
    print(nazwisko)
wyswietl_nazwisko("Us")

# Zadanie 4

print("\nZadanie 4")
def oblicz_iloraz(a, b):
  if a < b:
    a, b = b, a
  return a / b
print(oblicz_iloraz(2, 5))

# Zadanie 5

print("\nZadanie 5")
def oblicz_sume(n):
  sum = 0
  for i in range(1, n + 1):
    sum += i ** 2
  return sum
print(oblicz_sume(2))

# Zadanie 6

print("\nZadanie 6")
def oblicz_wyrazenie(n):
  if n == 1:
    return 1
  else:
    wyrazenie = 1
    for i in range(1, n):
      mnozenie = 1
      for j in range(1, i + 1):
        mnozenie *= 3
      wyrazenie += 1 / mnozenie
    return wyrazenie
print(oblicz_wyrazenie(2))