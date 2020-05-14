def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(addition(3, 5, 2, 5, 1 ,6))

nums = [1 ,2 ,4 ,6 ,8 ,9]

print(addition(*nums))

def addition2(base, *args):
    result = 0
    for arg in args:
        result += arg
    return result

print(addition2(3, 5, 2, 5, 1 ,6))

nums = [1 ,2 ,4 ,6 ,8 ,9]

print(addition2(*nums))
print(addition2(2, *nums))