#given an input value, determine if it is a prime number or not( can be divided by only 1 and itself)

def is_prime(number):
    if number==0 or number == 1:
        return False 
    elif number==2:
        return True
    else:
        i=2
        while i<number:
            remainder = number%i
            i+=1
            if remainder == 0:
                return False
            else:
                return True

if __name__=="__main__":
    print(is_prime(122))
