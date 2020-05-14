def myfunc(arg1, arg2, arg3="Foo"):
    print(arg1, arg2, arg3)

myfunc(1, 2)
myfunc(1, 2, 3)

def myfunc(arg1, arg2, *,  arg3="Foo"):
    print(arg1, arg2, arg3)

myfunc(1,2, arg3=3)
myfunc(1, 2, 3)