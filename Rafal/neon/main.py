f = open("instrukcje.txt", "r")

lines = f.read().splitlines()
alfabet = "ABCDEFGHIJKLMNOPRSTUWXYZ"
napis = ""

for line in lines:
    line1 = line.split(" ")
    if "DOPISZ" in line:
        napis += line1[1]
    elif "ZMIEN" in line:
        str = "".join([*napis][:-1]) + line1[1]
    elif "USUN" in line:
        napis = "".join([*napis][:-1])
    elif "PRZESUN" in line:
        napis = napis.replace(line1[1], alfabet[(alfabet.find(napis[0]) + 1) % len(alfabet)], 1)
print(len(napis))


