import pickle
import math

with open("triangle.bin", "rb") as f:
    dict = dict(pickle.load(f))
    
permiter = sum(dict.values())
semiPerimeter = permiter / 2
area = math.sqrt(semiPerimeter * (semiPerimeter - dict["a"]) * (semiPerimeter - dict["b"]) * (semiPerimeter - dict["c"]))

print("Area = {A}\nPerimiter = {P}".format(A=area, P=permiter))
