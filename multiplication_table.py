#given an input integer return a nested list of n by n multiplication table

def multiplication_table(number):
    #loop of n number of lists appended to the main list
    i=1
    main=[]
    while i<=number:
        j=1
        nested=[]
        while j<=number:
            nested.append(i*j)
            j+=1
        main.append(nested)
        i+=1
    return main

if __name__=="__main__":
    print(multiplication_table(5))
    print(multiplication_table(8)) 