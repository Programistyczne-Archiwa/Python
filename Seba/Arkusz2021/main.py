# This code is used to decode a message
# The code is not very efficient, but it should work
file = open("instrukcje.txt", "r")
lines = file.read().splitlines()

# 4.1

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

# 4.2
last = ""
count = 0
max = {"count": 0, "last": ""}
for line in lines:
    funct = line.split(" ")[0]
    value = line.split(" ")[1]
    if last == "":
        last = funct
        count = 1
    else:
        if last == funct:
            count += 1
        else:
            last = funct
            count = 1
    if count > max["count"]:
        max["count"] = count
        max["last"] = last

print(max["last"], max["count"])
