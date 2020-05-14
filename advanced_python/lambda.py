#used when defining a full function is more effort than it is worth

def square_function(x):
    return x**2

nums = [213, 514, 6, 235 ,6 ,26 ,783 ,32 ,5]

squared_numbers = list(map(square_function, nums))
print(squared_numbers)

#now using the lambda function instead
print(list(map(lambda x: x**2, nums)))