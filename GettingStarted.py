import pandas as pd

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3,7,2],
    "Number" : ["This one", "This two", "This three"]
}

myvar = pd.DataFrame(mydataset)

print(myvar)



