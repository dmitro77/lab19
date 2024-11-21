import pickle

with open("words.bin", "rb") as f:
    result = pickle.load(file=f)
    print(result)
