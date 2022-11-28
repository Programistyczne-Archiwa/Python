# Zadanie 1
print("Zadanie 1")
liczby = {"jeden": 1, "dwa": 2, "trzy": 3}
print(liczby["dwa"])

# Zadanie 2
print("\nZadanie 2")
liczby = {"jeden": 1, "dwa": 2}
# print(liczba[2])
print("error")

# Zadanie 3
print("\nZadanie 3")
liczby = {"jeden": "one", "dwa": "two", "trzy": "three"}
print("dwa" in liczby)

# Zadanie 4
print("\nZadanie 4")
liczby={"jeden": "one", "dwa": "two", "trzy": "three"}
print ("one" in liczby)

# Zadanie 5
print("\nZadanie 5")
liczby = {"jeden": "one", "dwa": "two"}
liczby["dwa"] = 1
# print(liczby["two"])
print("error")

# Zadanie 6
print("\nZadanie 6")
liczby = {"jeden": "one", "dwa": "two"}
liczby["two"] = "dwa"
print(liczby["dwa"])

# Zadanie 7
print("\nZadanie 7")
liczby = {"jeden": 1, "dwa": [7, 2, 9], "trzy": 3}
x = (liczby["dwa"])
x.sort()
print(x)
