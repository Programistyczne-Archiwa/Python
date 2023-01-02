# Zadanie 73.1 Oblicz, ile jest w tekście słów, w których występują dwie kolejne takie same litery
import math


file = open("C:/Users/Egzamin/Documents/GitHub/Python/Seba/Zbior 73/tekst.txt", "r")
words = file.read().split()
for word in words:
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            print(word)
            break

# Zadanie 73.2 Sporządź statystykę częstotliwości występowania liter w tekście: dla każdej litery podaj liczbę jej wystąpień we wszystkich słowach tekstu oraz jej procentowy udział wśród wystąpień wszystkich liter w tekście(do statystyki nie wliczaj spacji). Odpowiedź zapisz w następującej postaci

alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count_alf = {}
count_all = 0
for word in words:
    for letter in word:
        if letter in alf:
            if letter in count_alf:
                count_alf[letter] += 1
            else:
                count_alf[letter] = 1
            count_all += 1
for letter in alf:
    if letter in count_alf:
        print(f"{letter}: {count_alf[letter]} ({round(count_alf[letter] / count_all * 100, 2)}%)")
