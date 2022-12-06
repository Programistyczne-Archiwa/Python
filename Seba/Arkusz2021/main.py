# This code is used to decode a message
# The code is not very efficient, but it should work
file = open("instrukcje.txt", "r")
lines = file.read().splitlines()

str = ""
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for line in lines:
    funct = line.split(" ")[0]
    value = line.split(" ")[1]

    if funct == "DOPISZ":
        str += value
    elif funct == "ZMIEN":
        str = "".join([*str][:-1]) + value
    elif funct == "USUN":
        str = "".join([*str][:-1])
    elif funct == "PRZESUN":
        str = str.replace(value, alf[(alf.find(str[0]) + 1) % len(alf)], 1)

print(len(str))