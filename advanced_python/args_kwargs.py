def func(*args):
    # *args means for however many arguments you take in, it will catch them all
 
    for arg in args:
        print(arg)
         
l = [11,3,4,5,"tuts"]
 
print(func(*l))


def capital_cities(**kwargs): 
    # initialize an empty list to store the result
    result = []
    for key, value in kwargs.items():
        result.append("{} is the capital city of {}".format (key,value))
 
    return result

print(capital_cities(China = "Beijing",Cairo = "Egypt",Rome = "Italy"))