# Zadanie 22
print("Zadanie 22")
text = "asdas dasda dasd"
text = text.split(" ")
MaxAndMin = ["", ""]
for sentence in text:
    if MaxAndMin[0] == "" or len(MaxAndMin[0]) > len(sentence) :
        MaxAndMin[0] = sentence
    if MaxAndMin[1] == "" or len(MaxAndMin[1]) < len(sentence):
        MaxAndMin[1] = sentence
print(f"Min: {MaxAndMin[0]}, Max: {MaxAndMin[1]}")