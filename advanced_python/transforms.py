def odd_only(x):
    if x%2 == 0:
        return False
    else: 
        return True

def lower_case_filter(x):
    if x.isupper():
        return False
    return True

def square_function(x):
    return x**2

nums = [213, 514, 6, 235 ,6 ,26 ,783 ,32 ,5]
chars = "dsafFdaFagHNWacFFAscdaDFA"

#filtering a list of numbers
odd_filter_list= list(filter(odd_only, nums))
print(odd_filter_list)

#filtering a list of letters
lower_case_filtered = list(filter(lower_case_filter, chars))
print(lower_case_filtered)

#mapping - squaring the numbers in the list to form a list with new values
squared_numbers = list(map(square_function, nums))
print(squared_numbers)

print(next(filter(lower_case_filter, chars)))
print(next(filter(lower_case_filter, chars)))
