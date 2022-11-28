alf = "abcdefghijklmnprstuwxyz"
key = 5
text_to_encrypt = "e"
decrypted_text = ""

for char in text_to_encrypt:
    decrypted_text += alf[(alf.index(char) + key) % len(alf)]

print(decrypted_text)