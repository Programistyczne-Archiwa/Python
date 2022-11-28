from datetime import datetime, timedelta, date

# Zadanie 1
print("\nZadanie 1")
a = 1600
if a % 4 == 0 and a % 100 == 0 or a % 400 == 0:
    print("Rok jest przestępny")
else:
    print("Rok nie jest przestępny")

# Zadanie 2
print("\nZadanie 2")
d = datetime.today() - timedelta(days=7)
print(d.strftime("%Y-%m-%d"))

# Zadanie 3
print("\nZadanie 3")
d = datetime.today() + timedelta(minutes=25)
print(d.strftime("%Y-%m-%d %H:%M"))

# Zadanie 4
print("\nZadanie 4")
print(datetime.weekday(datetime.today()))

# Zadamie 5
print("\nZadanie 5")
year = datetime.today().year
date_object = date(year, 1, 1)
date_object += timedelta(days=1)
while date_object.year == year:
    print(date_object)
    date_object += timedelta(days=7)


# Zadanie 6
print("\nZadanie 6")
d = date(2002, 2, 22) - date(2001, 2, 22)
print(d.days)

# Zadanie 7 in progress
print("\nZadanie 7")
d = date((datetime.now() - timedelta(year=3)).year, datetime.now().month, datetime.now().day)
for i in d:
    print(i)

# Zadanie 8 in progress
print("\nZadanie 8")