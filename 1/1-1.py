import pickle

wordString = input("Input string of words, divided by spaces: ")

words = wordString.split(" ")
Sortedwords = sorted(words)

with open("words.bin", "wb") as f:
    pickle.dump(obj=Sortedwords, file=f)
