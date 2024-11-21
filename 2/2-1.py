import pickle

dict = dict([("a",0),("b",0),("c",0)])

for key in dict.keys():
    dict[key] = float(input("Enter value for " + key + " : "))

with open("triangle.bin", "wb") as f:
    pickle.dump(dict, f)
