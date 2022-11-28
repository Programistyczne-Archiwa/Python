a = 1
b = 5
c = 2

try:
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("Delta mniejsza od zera")
    elif delta == 0:
        x1 = -b / (2*a)
        print("x0 = ", x1)
    elif delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print("x1 = ", round(x1, 2))
        print("x2 = ", round(x2, 2))
except ValueError:
    print("Delta mniejsza od zera")
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Niepoprawny typ danych")