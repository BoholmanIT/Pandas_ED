import pandas

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3,7,2],
    "Number" : ["This one", "This two", "This three"]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)



