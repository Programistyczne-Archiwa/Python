def saveToFile(fileName, data):
    with open(fileName, "w") as file:
        file.write(data)

# 6.1 Szyfr Cezara
# Napisz program, który zaszyfruje słowa z pliku dane_6_1.txt z użyciem klucza
# k = 107. Wynik zapisz do pliku wyniki_6_1.txt, każde słowo w osobnym wierszu,
# w porządku odpowiadającym kolejności słów z pliku z danymi. 

print("Zadanie 6.1")

alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plain, key):
    cipher = ""
    for c in plain:
        if c in alf:
            cipher += alf[(alf.index(c) + key) % len(alf)]
        else:
            cipher += c
    return cipher

data = ""
for line in open("dane_6_1.txt"):
    # add data
    data += f"{encrypt(line.strip(), 107)}\n"
# save data to file
saveToFile("wyniki_6_1.txt", data)

# 6.2 Szyfr Cezara
# W pliku dane_6_2.txt zapisano 3 000 szyfrogramów i odpowiadające im klucze
# szyfrujące. W każdym wierszu znajduje się jeden szyfrogram (zaszyfrowane słowo)
# i po pojedynczym znaku odstępu odpowiadający mu klucz (maksymalnie czterocyfrowa
# liczba). 

print("Zadanie 6.2")

alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(cipher, key):
    plain = ""
    for c in cipher:
        if c in alf:
            plain += alf[(alf.index(c) - key) % len(alf)]
        else:
            plain += c
    return plain

data = ""
for line in open("dane_6_2.txt"):
    if len(line.split()) == 2:
        cipher, key = line.split()
        # add data
        data += f"{decrypt(cipher, int(key))}\n"
# save data to file
saveToFile("wyniki_6_2.txt", data)

# 6.3 Szyfr Cezara
# W pliku dane_6_3.txt zapisano 3 000 par słów, po jednej parze w wierszu, oddzielonych
# pojedynczym znakiem odstępu. Drugie słowo w każdej parze jest szyfrogramem pierwszego
# z nieznanym kluczem. 

print("Zadanie 6.3")

alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def compare(plain, cipher):
    for i in range(len(plain)):
        if plain[i] != cipher[i]:
            return False
    return True

data = ""
for line in open("dane_6_3.txt"):
    if len(line.split()) == 2:
        plain, cipher = line.split()
        isGood = True
        for key in range(len(alf)):
            if compare(plain, decrypt(cipher, key)) == False:
                isGood = False
            else:
                isGood = True
                break
        if isGood == False:
            data += f"{plain} {cipher}\n"
# save data to file
saveToFile("wyniki_6_3.txt", data)
                