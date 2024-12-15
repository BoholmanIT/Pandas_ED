import pandas as pd


a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar)

print(myvar[0])

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)

print(myvar["y"])


calories = {"day1" : 420, "day2" : 380, "day3" : 390}

CaloriesTable = pd.Series(calories)

print(CaloriesTable)

Only12day = pd.Series(calories, index=["day1", "day2"])
print(Only12day)