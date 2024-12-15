import pandas as pd


a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar)

print(myvar[0])

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)