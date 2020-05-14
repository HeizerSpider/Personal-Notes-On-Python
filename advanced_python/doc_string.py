def randomFunction(arg1, arg2=None):
    """
    randomFunction(arg1, arg2=None):
    Doesnt do much other than to print the arguments given.
    First argument to be given, second argument defaults to None.
    """
    print(arg1, arg2)

randomFunction(1, 2)

print(randomFunction.__doc__)