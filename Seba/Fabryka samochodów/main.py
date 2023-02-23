# 2005
dama = 237
granta = 198
dorkas = 207
lodera = 312

produkcja_dama = 237
produkcja_granta = 198
produkcja_dorkas = 207
produkcja_lodera = 312

for i in range(2005, 2010):
    for j in range(4):
        if(i == 2005 and j == 0):
            pass
        produkcja_dama = round(produkcja_dama * 1.02)
        produkcja_granta = round(produkcja_granta * 1.027)
        produkcja_dorkas = round(produkcja_dorkas * 1.03)
        produkcja_lodera = round(produkcja_lodera * 1.02)

        dama += produkcja_dama
        granta += produkcja_granta
        dorkas += produkcja_dorkas
        lodera += produkcja_lodera
    print("Rok", i, "Dama", dama, "Granta", granta, "Dorkas", dorkas, "Lodera", lodera)

dama += produkcja_dama
granta += produkcja_granta
dorkas += produkcja_dorkas
lodera += produkcja_lodera
print("Rok", 20010, "Dama", dama, "Granta", granta, "Dorkas", dorkas, "Lodera", lodera)

